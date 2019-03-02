# A c-lightning plugin to export your payments as csv

This plugin exports all payments you've made with your c-lightning node to a CSV file.
```bash
# Start `lightningd` with the plugin specified as: 
lightningd --plugin=path/to/csvexportpays.py

# To export your payments run:
lightning-cli csvexportpays <output_file> [seperator] [headers]
# where `<>` is required and `[]` is optional.

# Example: 
lightning-cli csvexportpays ~/export.csv , True

# The CSV file contains the columns 
["status", "description", "amount", "paid amount", "creation time", "payee", "invoice as bolt11"]
```
![screenshot](https://raw.githubusercontent.com/0xB10C/c-lightning-plugin-csvexportpays/6461045b3dc1fe371b19045e4647eeb6c9e0ebaf/screenshot.png)

This plugin is partly based on Rene Pickhardt's [simpleFundsOverview](https://github.com/renepickhardt/c-lightning-plugin-collection)
