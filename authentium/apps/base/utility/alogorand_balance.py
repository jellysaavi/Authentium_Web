from algosdk import algod


def check_account_balance(address):

    algod_address = "https://testnet-algorand.api.purestake.io/ps1"
    algod_token = ""
    headers = {
        "X-API-Key": "N36xvmEIH77LfMvUsQNoh87CXH6SXXZLazaHLJYY",
    }

    algod_client = algod.AlgodClient(algod_token, algod_address, headers)
    account_info = algod_client.account_info(address)

    account_balance = account_info.get('amount')

    return account_balance