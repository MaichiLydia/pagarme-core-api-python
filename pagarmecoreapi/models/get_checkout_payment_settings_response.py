# -*- coding: utf-8 -*-

"""
    pagarmecoreapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import pagarmecoreapi.models.get_customer_response

class GetCheckoutPaymentSettingsResponse(object):

    """Implementation of the 'GetCheckoutPaymentSettingsResponse' model.

    Checkout Payment Settings Response

    Attributes:
        success_url (string): Success Url
        payment_url (string): Payment Url
        accepted_payment_methods (list of string): Accepted Payment Methods
        status (string): Status
        customer (GetCustomerResponse): Customer
        amount (int): Payment amount
        default_payment_method (string): Default Payment Method
        gateway_affiliation_id (string): Gateway Affiliation Id

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "success_url":'success_url',
        "payment_url":'payment_url',
        "accepted_payment_methods":'accepted_payment_methods',
        "status":'status',
        "customer":'customer',
        "amount":'amount',
        "default_payment_method":'default_payment_method',
        "gateway_affiliation_id":'gateway_affiliation_id'
    }

    def __init__(self,
                 success_url=None,
                 payment_url=None,
                 accepted_payment_methods=None,
                 status=None,
                 customer=None,
                 amount=None,
                 default_payment_method=None,
                 gateway_affiliation_id=None):
        """Constructor for the GetCheckoutPaymentSettingsResponse class"""

        # Initialize members of the class
        self.success_url = success_url
        self.payment_url = payment_url
        self.accepted_payment_methods = accepted_payment_methods
        self.status = status
        self.customer = customer
        self.amount = amount
        self.default_payment_method = default_payment_method
        self.gateway_affiliation_id = gateway_affiliation_id


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
        success_url = dictionary.get('success_url')
        payment_url = dictionary.get('payment_url')
        accepted_payment_methods = dictionary.get('accepted_payment_methods')
        status = dictionary.get('status')
        customer = pagarmecoreapi.models.get_customer_response.GetCustomerResponse.from_dictionary(dictionary.get('customer')) if dictionary.get('customer') else None
        amount = dictionary.get('amount')
        default_payment_method = dictionary.get('default_payment_method')
        gateway_affiliation_id = dictionary.get('gateway_affiliation_id')

        # Return an object of this model
        return cls(success_url,
                   payment_url,
                   accepted_payment_methods,
                   status,
                   customer,
                   amount,
                   default_payment_method,
                   gateway_affiliation_id)


