from solana.rpc.api import Client
from solana.account import Account
from solana.system_program import SYS_PROGRAM_ID
from solana.transaction import Transaction
from solana.publickey import PublicKey

# اتصال به شبکه سولانا
solana_client = Client("https://api.mainnet-beta.solana.com")

# ساخت یک اکانت جدید
new_account = Account()

# چاپ آدرس و کلید خصوصی
print("New Solana Address:", new_account.public_key())
print("Private Key:", new_account.secret_key())
