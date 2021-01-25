from algosdk.v2client import algod
from algosdk import mnemonic
from algosdk import transaction

#  ---------------------------------------------------------------
# create_transactions
#  ---------------------------------------------------------------
def create_transactions(amount, from_address, to_address, from_key):
    # Setup HTTP client w/guest key provided by PureStake
    algod_token = 'N36xvmEIH77LfMvUsQNoh87CXH6SXXZLazaHLJYY'
    algod_address = 'https://testnet-algorand.api.purestake.io/ps2'
    purestake_token = {'X-Api-key': algod_token}

    algodclient = algod.AlgodClient(algod_token, algod_address, headers=purestake_token)

    # get suggested parameters from Algod
    params = algodclient.suggested_params()

    # gh = params.gh
    # first_valid_round = params.first
    # last_valid_round = params.last
    #fee = params.min_fee
    send_amount = amount
    note = "Hello World".encode()
    existing_account = from_address
    send_to_address = to_address

    # Create and sign transaction
    tx = transaction.PaymentTxn(existing_account, params, send_to_address, send_amount, None, note)
    signed_tx = tx.sign(from_key)

    try:
        tx_confirm = algodclient.send_transaction(signed_tx, headers={'content-type': 'application/x-binary'})
        print('Transaction sent with ID', signed_tx.transaction.get_txid())
        wait_for_confirmation(algodclient, txid=signed_tx.transaction.get_txid())
    except Exception as e:
        print(e)

def wait_for_confirmation(client, txid):
    last_round = client.status().get('last-round')
    txinfo = client.pending_transaction_info(txid)
    while not (txinfo.get('confirmed-round') and txinfo.get('confirmed-round') > 0):
        print('Waiting for confirmation')
        last_round += 1
        client.status_after_block(last_round)
        txinfo = client.pending_transaction_info(txid)
    print('Transaction confirmed in round', txinfo.get('confirmed-round'))
    return txinfo