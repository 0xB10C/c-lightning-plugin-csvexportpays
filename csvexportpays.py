#!/usr/bin/env python3
"""
This plugin exports all payments you've made with your c-lightning
node to a .csv file.

Start `lightningd` with the plugin specified as:
`lightningd --plugin=path/to/csvexportpays.py`

To export your payments run: 
`lightning-cli csvexportpays <output_file> [seperator] [headers]`
where `<>` is required and `[]` is optional.

Example:
`lightning-cli csvexportpays ~/export.csv , True`

Author: 0xb10c

This script is partly based on Rene Pickhardt's simpleFundsOverview.
form https://github.com/renepickhardt/c-lightning-plugin-collection

"""

import csv
from os.path import join
from lightning import Plugin, LightningRpc

plugin = Plugin()

HEADER = ["status", "description", "amount", "paid amount",
          "creation time", "payee", "original invoice as bolt11"]


@plugin.method("csvexportpays")
def hello(plugin, output_file, seperator=",", headers=False):
    """Export all payments to a csv file {output_file} seperated by {seperator}.
    Providing a value for {headers} enables csv file headers. 

    """
    exportpays = plugin.get_option('csvexportpays')

    if output_file is None:
        return "Error: No output file specified"

    payments = rpc_interface.listpays()['pays']

    try:
        with open(output_file, "w") as csv_file:
            writer = csv.writer(csv_file, delimiter=seperator,
                                quoting=csv.QUOTE_MINIMAL)
            num_exported = 0

            if headers:
                writer.writerow(HEADER)

            for payment in payments:
                inv = payment.get("bolt11", None)
                if inv != None:

                    # decode the original invoice for more information
                    dec_inv = rpc_interface.decodepay(payment.get("bolt11"))

                    row = [
                        # 1 status
                        payment.get('status', ""),              
                        # 2 description                       
                        dec_inv.get('description', ""),         
                        # 3 invoice amount
                        dec_inv.get('amount_msat', ""),
                        # 4 total paid with fees
                        payment.get('amount_sent_msat', ""),
                        # 5 invoice creation
                        dec_inv.get('created_at', ""),
                        # 6 payee
                        dec_inv.get('payee', ""),               
                        # 7 original invoice
                        payment.get('bolt11', "")
                    ]

                    writer.writerow(row)
                    num_exported += 1

            return ("Exported %i payments to %s" % (num_exported, output_file))

    except Exception as error:
        print(error)
        return "Export failed: " + str(error)


@plugin.init()
def init(options, configuration, plugin):
    global rpc_interface

    # connect to the rpc interface
    rpc_interface = LightningRpc(
        join(configuration['lightning-dir'], configuration['rpc-file']))
    plugin.log("Plugin csvexportpays.py initialized")


plugin.run()
