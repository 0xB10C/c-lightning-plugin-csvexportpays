# c-ligthning-plugin-csvexportpays
This plugin exports all payments you've made with your c-lighting
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
