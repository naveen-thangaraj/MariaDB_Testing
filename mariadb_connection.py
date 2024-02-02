# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 11:29:24 2024

@author: naveen
"""

import mariadb
import base64

    
host_name=b'MTAuMTA3LjQ4LjQy'
user_name=b'cm9vdA=='
passphrase=b'U3Vuc2hpbmVAMzIxIw=='
db=b'Y2hvbGFtcw=='

db_connection = mariadb.connect(
     host=base64.b64decode(host_name).decode('utf-8'),
     port=3306,
     username=base64.b64decode(user_name).decode('utf-8'),
     password=base64.b64decode(passphrase).decode('utf-8'),
     database=base64.b64decode(db).decode('utf-8')
)
    
        