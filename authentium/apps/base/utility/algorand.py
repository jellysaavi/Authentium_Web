from algosdk import account

import json


#  ---------------------------------------------------------------
# create_algorand_account
#  ---------------------------------------------------------------
def create_algorand_account():
    private_key, public_address = account.generate_account()
    return private_key, public_address