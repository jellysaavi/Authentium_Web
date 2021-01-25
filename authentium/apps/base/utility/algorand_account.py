
# from algosdk import account
# from algosdk import mnemonic
# from algosdk import transaction
# from algosdk.wallet import Wallet

# import json


# def create_account(self):
#     private_key, public_address = account.generate_account()


# def create_transactions(self, amount, from_address, to_address):
#     algod_address = "https://testnet-algorand.api.purestake.io/ps1"
#     algod_token = ""
#     headers = {
#         "X-API-Key": "N36xvmEIH77LfMvUsQNoh87CXH6SXXZLazaHLJYY",
#     }

#     algod_client = account.AlgodClient(algod_token, algod_address, headers)


#     params = algod_client.suggested_params()
#     gen = params["genesisID"]
#     gh = params["genesishashb64"]
#     first_valid_round = params["lastRound"]
#     last_valid_round = first_valid_round + 1000
#     fee = params["fee"]
#     send_amount = amount
#     existing_account = from_address
#     send_to_address = to_address

#     # Create and sign transaction
#     tx = transaction.PaymentTxn(existing_account, fee, first_valid_round, last_valid_round, gh, send_to_address, send_amount)
#     signed_tx = tx.sign(self.request.session['private_key_account_a'])

#     # Function from Algorand Inc. - utility for waiting on a transaction confirmation
#     def wait_for_confirmation( algod_client, txid ):
#         last_round = algod_client.status().get('lastRound')
#         while True:
#             txinfo = algod_client.pending_transaction_info(txid)
#             if txinfo.get('round') and txinfo.get('round') > 0:
#                 print("Transaction {} confirmed in round {}.".format(txid, txinfo.get('round')))
#                 break
#             else:
#                 print("Waiting for confirmation...")
#                 last_round += 1
#                 algod_client.status_after_block(last_round)

#     try:
#         tx_confirm = algod_client.send_transaction(signed_tx, headers={'content-type': 'application/x-binary'})
#         wait_for_confirmation(algod_client, txid = signed_tx.transaction.get_txid())
#     except Exception as e:
#         print(e)

#     def create_wallet (self, address):    
#         pass