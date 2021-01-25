import logging

from django.views.generic.base import TemplateView
from pyteal import *

logger = logging.getLogger(__name__)


#  ---------------------------------------------------------------
# ViewAccountTest
#  ---------------------------------------------------------------
class ViewAccountTest(TemplateView):
    template_name = 'account/test.html'


    
    #  ---------------------------------------------------------------
    # get_context_data
    #  ---------------------------------------------------------------
    def get_context_data(self, **kwargs):

        alice = Addr("CQSV7LBWAXZW5K7ZVDOYAIDMEKC4SAZV7NWEHZBYV3GPNKT67KM4MV6XRY")
        bob = Addr("4K6D2LRGAQA4TYFYELAJSNVVIJZZX5EDAJTUUJ7EZXCGHDINR7TRR4MJKM")
        secret = Bytes("base32", "23232323232323")
        timeout = 3000

        def htlc(tmpl_seller=alice,
            tmpl_buyer=bob,
            tmpl_fee=1000,
            tmpl_secret=secret,
            tmpl_hash_fn=Sha256,
            tmpl_timeout=timeout):
        
            fee_cond = Txn.fee() < Int(tmpl_fee)
            safety_cond = And(
                Txn.type_enum() == TxnType.Payment,
                Txn.close_remainder_to() == Global.zero_address(),
                Txn.rekey_to() == Global.zero_address(),
            )

            recv_cond = And(
                Txn.receiver() == tmpl_seller,
                tmpl_hash_fn(Arg(0)) == tmpl_secret
            )
            
            esc_cond = And(
                Txn.receiver() == tmpl_buyer,
                Txn.first_valid() > Int(tmpl_timeout)
            )

            return And(
                fee_cond,
                safety_cond,
                Or(recv_cond, esc_cond)
            )
        
        print(compileTeal(htlc(), Mode.Signature))

        

        context = TemplateView.get_context_data(self, **kwargs)
        return context