# -*- coding: utf-8 -*-

"""
    pagarmecoreapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from pagarmecoreapi.api_helper import APIHelper
import pagarmecoreapi.models.get_transaction_response
import pagarmecoreapi.models.get_invoice_response
import pagarmecoreapi.models.get_order_response
import pagarmecoreapi.models.get_customer_response

class GetChargeResponse(object):

    """Implementation of the 'GetChargeResponse' model.

    Response object for getting a charge

    Attributes:
        id (string): TODO: type description here.
        code (string): TODO: type description here.
        gateway_id (string): TODO: type description here.
        amount (int): TODO: type description here.
        status (string): TODO: type description here.
        currency (string): TODO: type description here.
        payment_method (string): TODO: type description here.
        due_at (datetime): TODO: type description here.
        created_at (datetime): TODO: type description here.
        updated_at (datetime): TODO: type description here.
        last_transaction (GetTransactionResponse): TODO: type description
            here.
        invoice (GetInvoiceResponse): TODO: type description here.
        order (GetOrderResponse): TODO: type description here.
        customer (GetCustomerResponse): TODO: type description here.
        metadata (dict<object, string>): TODO: type description here.
        paid_at (datetime): TODO: type description here.
        canceled_at (datetime): TODO: type description here.
        canceled_amount (int): Canceled Amount
        paid_amount (int): Paid amount

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "code":'code',
        "gateway_id":'gateway_id',
        "amount":'amount',
        "status":'status',
        "currency":'currency',
        "payment_method":'payment_method',
        "due_at":'due_at',
        "created_at":'created_at',
        "updated_at":'updated_at',
        "metadata":'metadata',
        "canceled_amount":'canceled_amount',
        "paid_amount":'paid_amount',
        "last_transaction":'last_transaction',
        "invoice":'invoice',
        "order":'order',
        "customer":'customer',
        "paid_at":'paid_at',
        "canceled_at":'canceled_at'
    }

    def __init__(self,
                 id=None,
                 code=None,
                 gateway_id=None,
                 amount=None,
                 status=None,
                 currency=None,
                 payment_method=None,
                 due_at=None,
                 created_at=None,
                 updated_at=None,
                 metadata=None,
                 canceled_amount=None,
                 paid_amount=None,
                 last_transaction=None,
                 invoice=None,
                 order=None,
                 customer=None,
                 paid_at=None,
                 canceled_at=None):
        """Constructor for the GetChargeResponse class"""

        # Initialize members of the class
        self.id = id
        self.code = code
        self.gateway_id = gateway_id
        self.amount = amount
        self.status = status
        self.currency = currency
        self.payment_method = payment_method
        self.due_at = APIHelper.RFC3339DateTime(due_at) if due_at else None
        self.created_at = APIHelper.RFC3339DateTime(created_at) if created_at else None
        self.updated_at = APIHelper.RFC3339DateTime(updated_at) if updated_at else None
        self.last_transaction = last_transaction
        self.invoice = invoice
        self.order = order
        self.customer = customer
        self.metadata = metadata
        self.paid_at = APIHelper.RFC3339DateTime(paid_at) if paid_at else None
        self.canceled_at = APIHelper.RFC3339DateTime(canceled_at) if canceled_at else None
        self.canceled_amount = canceled_amount
        self.paid_amount = paid_amount


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
        id = dictionary.get('id')
        code = dictionary.get('code')
        gateway_id = dictionary.get('gateway_id')
        amount = dictionary.get('amount')
        status = dictionary.get('status')
        currency = dictionary.get('currency')
        payment_method = dictionary.get('payment_method')
        due_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("due_at")).datetime if dictionary.get("due_at") else None
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else None
        metadata = dictionary.get('metadata')
        canceled_amount = dictionary.get('canceled_amount')
        paid_amount = dictionary.get('paid_amount')
        last_transaction = pagarmecoreapi.models.get_transaction_response.GetTransactionResponse.from_dictionary(dictionary.get('last_transaction')) if dictionary.get('last_transaction') else None
        invoice = pagarmecoreapi.models.get_invoice_response.GetInvoiceResponse.from_dictionary(dictionary.get('invoice')) if dictionary.get('invoice') else None
        order = pagarmecoreapi.models.get_order_response.GetOrderResponse.from_dictionary(dictionary.get('order')) if dictionary.get('order') else None
        customer = pagarmecoreapi.models.get_customer_response.GetCustomerResponse.from_dictionary(dictionary.get('customer')) if dictionary.get('customer') else None
        paid_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("paid_at")).datetime if dictionary.get("paid_at") else None
        canceled_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("canceled_at")).datetime if dictionary.get("canceled_at") else None

        # Return an object of this model
        return cls(id,
                   code,
                   gateway_id,
                   amount,
                   status,
                   currency,
                   payment_method,
                   due_at,
                   created_at,
                   updated_at,
                   metadata,
                   canceled_amount,
                   paid_amount,
                   last_transaction,
                   invoice,
                   order,
                   customer,
                   paid_at,
                   canceled_at)


