import json
from collections import OrderedDict

file_data = OrderedDict()
file_data['address'] = '0x200be26d4f6c5e99959d63bce52fd86c7a699f86'
file_data['xpublic_key'] = b'xpub6FW1Jbvr4MBXLSVxq1b8ZFPWynLGgtoemZksHWgPJiMk8ZkcJrhGc9P6pDGQXztgregvBAhbMKjqC6eQvURgSnyW5FzLRMLHPmVpTaKvpdE'
file_data['path'] = 'm/0'
file_data['bip32_path'] = "m/44'/60'/0'/0"

with open('a.json', 'w', encoding="utf-8") as f:
    json.dump(file_data, f, ensure_ascii=False, indent="\t")
