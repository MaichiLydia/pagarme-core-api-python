# -*- coding: utf-8 -*-

"""
    pagarmecoreapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import pagarmecoreapi.models.create_credit_card_payment_request
import pagarmecoreapi.models.create_debit_card_payment_request
import pagarmecoreapi.models.create_boleto_payment_request
import pagarmecoreapi.models.create_voucher_payment_request
import pagarmecoreapi.models.create_split_request
import pagarmecoreapi.models.create_bank_transfer_payment_request
import pagarmecoreapi.models.create_checkout_payment_request
import pagarmecoreapi.models.create_customer_request
import pagarmecoreapi.models.create_cash_payment_request
import pagarmecoreapi.models.create_private_label_payment_request
import pagarmecoreapi.models.create_pix_payment_request

class CreatePaymentRequest(object):

    """Implementation of the 'CreatePaymentRequest' model.

    Payment data

    Attributes:
        payment_method (string): Payment method
        credit_card (CreateCreditCardPaymentRequest): Settings for credit card
            payment
        debit_card (CreateDebitCardPaymentRequest): Settings for debit card
            payment
        boleto (CreateBoletoPaymentRequest): Settings for boleto payment
        currency (string): Currency. Must be informed using 3 characters
        voucher (CreateVoucherPaymentRequest): Settings for voucher payment
        split (list of CreateSplitRequest): Splits
        bank_transfer (CreateBankTransferPaymentRequest): Settings for bank
            transfer payment
        gateway_affiliation_id (string): Gateway affiliation code
        amount (int): The amount of the payment, in cents
        checkout (CreateCheckoutPaymentRequest): Settings for checkout
            payment
        customer_id (string): Customer Id
        customer (CreateCustomerRequest): Customer
        metadata (dict<object, string>): Metadata
        cash (CreateCashPaymentRequest): Settings for cash payment
        private_label (CreatePrivateLabelPaymentRequest): Settings for private
            label payment
        pix (CreatePixPaymentRequest): Settings for pix payment

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payment_method":'payment_method',
        "private_label":'private_label',
        "credit_card":'credit_card',
        "debit_card":'debit_card',
        "boleto":'boleto',
        "currency":'currency',
        "voucher":'voucher',
        "split":'split',
        "bank_transfer":'bank_transfer',
        "gateway_affiliation_id":'gateway_affiliation_id',
        "amount":'amount',
        "checkout":'checkout',
        "customer_id":'customer_id',
        "customer":'customer',
        "metadata":'metadata',
        "cash":'cash',
        "pix":'pix'
    }

    def __init__(self,
                 payment_method=None,
                 private_label=None,
                 credit_card=None,
                 debit_card=None,
                 boleto=None,
                 currency=None,
                 voucher=None,
                 split=None,
                 bank_transfer=None,
                 gateway_affiliation_id=None,
                 amount=None,
                 checkout=None,
                 customer_id=None,
                 customer=None,
                 metadata=None,
                 cash=None,
                 pix=None):
        """Constructor for the CreatePaymentRequest class"""

        # Initialize members of the class
        self.payment_method = payment_method
        self.credit_card = credit_card
        self.debit_card = debit_card
        self.boleto = boleto
        self.currency = currency
        self.voucher = voucher
        self.split = split
        self.bank_transfer = bank_transfer
        self.gateway_affiliation_id = gateway_affiliation_id
        self.amount = amount
        self.checkout = checkout
        self.customer_id = customer_id
        self.customer = customer
        self.metadata = metadata
        self.cash = cash
        self.private_label = private_label
        self.pix = pix


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        payment_method = dictionary.get('payment_method')
        private_label = pagarmecoreapi.models.create_private_label_payment_request.CreatePrivateLabelPaymentRequest.from_dictionary(dictionary.get('private_label')) if dictionary.get('private_label') else None
        credit_card = pagarmecoreapi.models.create_credit_card_payment_request.CreateCreditCardPaymentRequest.from_dictionary(dictionary.get('credit_card')) if dictionary.get('credit_card') else None
        debit_card = pagarmecoreapi.models.create_debit_card_payment_request.CreateDebitCardPaymentRequest.from_dictionary(dictionary.get('debit_card')) if dictionary.get('debit_card') else None
        boleto = pagarmecoreapi.models.create_boleto_payment_request.CreateBoletoPaymentRequest.from_dictionary(dictionary.get('boleto')) if dictionary.get('boleto') else None
        currency = dictionary.get('currency')
        voucher = pagarmecoreapi.models.create_voucher_payment_request.CreateVoucherPaymentRequest.from_dictionary(dictionary.get('voucher')) if dictionary.get('voucher') else None
        split = None
        if dictionary.get('split') != None:
            split = list()
            for structure in dictionary.get('split'):
                split.append(pagarmecoreapi.models.create_split_request.CreateSplitRequest.from_dictionary(structure))
        bank_transfer = pagarmecoreapi.models.create_bank_transfer_payment_request.CreateBankTransferPaymentRequest.from_dictionary(dictionary.get('bank_transfer')) if dictionary.get('bank_transfer') else None
        gateway_affiliation_id = dictionary.get('gateway_affiliation_id')
        amount = dictionary.get('amount')
        checkout = pagarmecoreapi.models.create_checkout_payment_request.CreateCheckoutPaymentRequest.from_dictionary(dictionary.get('checkout')) if dictionary.get('checkout') else None
        customer_id = dictionary.get('customer_id')
        customer = pagarmecoreapi.models.create_customer_request.CreateCustomerRequest.from_dictionary(dictionary.get('customer')) if dictionary.get('customer') else None
        metadata = dictionary.get('metadata')
        cash = pagarmecoreapi.models.create_cash_payment_request.CreateCashPaymentRequest.from_dictionary(dictionary.get('cash')) if dictionary.get('cash') else None
        pix = pagarmecoreapi.models.create_pix_payment_request.CreatePixPaymentRequest.from_dictionary(dictionary.get('pix')) if dictionary.get('pix') else None

        # Return an object of this model
        return cls(payment_method,
                   private_label,
                   credit_card,
                   debit_card,
                   boleto,
                   currency,
                   voucher,
                   split,
                   bank_transfer,
                   gateway_affiliation_id,
                   amount,
                   checkout,
                   customer_id,
                   customer,
                   metadata,
                   cash,
                   pix)


