# -*- coding: utf-8 -*-

"""
    pagarmecoreapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import pagarmecoreapi.models.update_pricing_scheme_request

class UpdatePlanItemRequest(object):

    """Implementation of the 'UpdatePlanItemRequest' model.

    Request for updating a plan item

    Attributes:
        name (string): Item name
        description (string): Description
        status (string): Item status
        pricing_scheme (UpdatePricingSchemeRequest): Pricing scheme
        quantity (int): Quantity
        cycles (int): Number of cycles that the item will be charged

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "description":'description',
        "status":'status',
        "pricing_scheme":'pricing_scheme',
        "quantity":'quantity',
        "cycles":'cycles'
    }

    def __init__(self,
                 name=None,
                 description=None,
                 status=None,
                 pricing_scheme=None,
                 quantity=None,
                 cycles=None):
        """Constructor for the UpdatePlanItemRequest class"""

        # Initialize members of the class
        self.name = name
        self.description = description
        self.status = status
        self.pricing_scheme = pricing_scheme
        self.quantity = quantity
        self.cycles = cycles


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
        name = dictionary.get('name')
        description = dictionary.get('description')
        status = dictionary.get('status')
        pricing_scheme = pagarmecoreapi.models.update_pricing_scheme_request.UpdatePricingSchemeRequest.from_dictionary(dictionary.get('pricing_scheme')) if dictionary.get('pricing_scheme') else None
        quantity = dictionary.get('quantity')
        cycles = dictionary.get('cycles')

        # Return an object of this model
        return cls(name,
                   description,
                   status,
                   pricing_scheme,
                   quantity,
                   cycles)


