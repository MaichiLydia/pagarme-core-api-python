# -*- coding: utf-8 -*-

"""
    pagarmecoreapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from pagarmecoreapi.api_helper import APIHelper
import pagarmecoreapi.models.create_address_request

class CreateShippingRequest(object):

    """Implementation of the 'CreateShippingRequest' model.

    Shipping data

    Attributes:
        amount (int): Shipping amount
        description (string): Description
        recipient_name (string): Recipient name
        recipient_phone (string): Recipient phone number
        address_id (string): The id of the address that will be used for
            shipping
        address (CreateAddressRequest): Address data
        max_delivery_date (datetime): Data máxima de entrega
        estimated_delivery_date (datetime): Prazo estimado de entrega
        mtype (string): Shipping type

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount":'amount',
        "description":'description',
        "recipient_name":'recipient_name',
        "recipient_phone":'recipient_phone',
        "address_id":'address_id',
        "address":'address',
        "mtype":'type',
        "max_delivery_date":'max_delivery_date',
        "estimated_delivery_date":'estimated_delivery_date'
    }

    def __init__(self,
                 amount=None,
                 description=None,
                 recipient_name=None,
                 recipient_phone=None,
                 address_id=None,
                 address=None,
                 mtype=None,
                 max_delivery_date=None,
                 estimated_delivery_date=None):
        """Constructor for the CreateShippingRequest class"""

        # Initialize members of the class
        self.amount = amount
        self.description = description
        self.recipient_name = recipient_name
        self.recipient_phone = recipient_phone
        self.address_id = address_id
        self.address = address
        self.max_delivery_date = APIHelper.RFC3339DateTime(max_delivery_date) if max_delivery_date else None
        self.estimated_delivery_date = APIHelper.RFC3339DateTime(estimated_delivery_date) if estimated_delivery_date else None
        self.mtype = mtype


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
        amount = dictionary.get('amount')
        description = dictionary.get('description')
        recipient_name = dictionary.get('recipient_name')
        recipient_phone = dictionary.get('recipient_phone')
        address_id = dictionary.get('address_id')
        address = pagarmecoreapi.models.create_address_request.CreateAddressRequest.from_dictionary(dictionary.get('address')) if dictionary.get('address') else None
        mtype = dictionary.get('type')
        max_delivery_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("max_delivery_date")).datetime if dictionary.get("max_delivery_date") else None
        estimated_delivery_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("estimated_delivery_date")).datetime if dictionary.get("estimated_delivery_date") else None

        # Return an object of this model
        return cls(amount,
                   description,
                   recipient_name,
                   recipient_phone,
                   address_id,
                   address,
                   mtype,
                   max_delivery_date,
                   estimated_delivery_date)


