# -*- coding: utf-8 -*-

"""
    pagarmecoreapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import pagarmecoreapi.models.create_plan_item_request
import pagarmecoreapi.models.create_pricing_scheme_request

class CreatePlanRequest(object):

    """Implementation of the 'CreatePlanRequest' model.

    Request for creating a plan

    Attributes:
        name (string): Plan's name
        description (string): Description
        statement_descriptor (string): Text that will be printed on the credit
            card's statement
        items (list of CreatePlanItemRequest): Plan items
        shippable (bool): Indicates if the plan is shippable
        payment_methods (list of string): Allowed payment methods for the
            plan
        installments (list of int): Number of installments
        currency (string): Currency
        interval (string): Interval
        interval_count (int): Interval counts between two charges. For
            instance, if the interval is 'month' and count is 2, the customer
            will be charged once every two months.
        billing_days (list of int): Allowed billings days for the
            subscription, in case the plan type is 'exact_day'
        billing_type (string): Billing type
        pricing_scheme (CreatePricingSchemeRequest): Plan's pricing scheme
        metadata (dict<object, string>): Metadata
        minimum_price (int): Minimum price that will be charged
        cycles (int): Number of cycles
        quantity (int): Quantity
        trial_period_days (int): Trial period, where the customer will not be
            charged.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "description":'description',
        "statement_descriptor":'statement_descriptor',
        "items":'items',
        "shippable":'shippable',
        "payment_methods":'payment_methods',
        "installments":'installments',
        "currency":'currency',
        "interval":'interval',
        "interval_count":'interval_count',
        "billing_days":'billing_days',
        "billing_type":'billing_type',
        "pricing_scheme":'pricing_scheme',
        "metadata":'metadata',
        "minimum_price":'minimum_price',
        "cycles":'cycles',
        "quantity":'quantity',
        "trial_period_days":'trial_period_days'
    }

    def __init__(self,
                 name=None,
                 description=None,
                 statement_descriptor=None,
                 items=None,
                 shippable=None,
                 payment_methods=None,
                 installments=None,
                 currency=None,
                 interval=None,
                 interval_count=None,
                 billing_days=None,
                 billing_type=None,
                 pricing_scheme=None,
                 metadata=None,
                 minimum_price=None,
                 cycles=None,
                 quantity=None,
                 trial_period_days=None):
        """Constructor for the CreatePlanRequest class"""

        # Initialize members of the class
        self.name = name
        self.description = description
        self.statement_descriptor = statement_descriptor
        self.items = items
        self.shippable = shippable
        self.payment_methods = payment_methods
        self.installments = installments
        self.currency = currency
        self.interval = interval
        self.interval_count = interval_count
        self.billing_days = billing_days
        self.billing_type = billing_type
        self.pricing_scheme = pricing_scheme
        self.metadata = metadata
        self.minimum_price = minimum_price
        self.cycles = cycles
        self.quantity = quantity
        self.trial_period_days = trial_period_days


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
        statement_descriptor = dictionary.get('statement_descriptor')
        items = None
        if dictionary.get('items') != None:
            items = list()
            for structure in dictionary.get('items'):
                items.append(pagarmecoreapi.models.create_plan_item_request.CreatePlanItemRequest.from_dictionary(structure))
        shippable = dictionary.get('shippable')
        payment_methods = dictionary.get('payment_methods')
        installments = dictionary.get('installments')
        currency = dictionary.get('currency')
        interval = dictionary.get('interval')
        interval_count = dictionary.get('interval_count')
        billing_days = dictionary.get('billing_days')
        billing_type = dictionary.get('billing_type')
        pricing_scheme = pagarmecoreapi.models.create_pricing_scheme_request.CreatePricingSchemeRequest.from_dictionary(dictionary.get('pricing_scheme')) if dictionary.get('pricing_scheme') else None
        metadata = dictionary.get('metadata')
        minimum_price = dictionary.get('minimum_price')
        cycles = dictionary.get('cycles')
        quantity = dictionary.get('quantity')
        trial_period_days = dictionary.get('trial_period_days')

        # Return an object of this model
        return cls(name,
                   description,
                   statement_descriptor,
                   items,
                   shippable,
                   payment_methods,
                   installments,
                   currency,
                   interval,
                   interval_count,
                   billing_days,
                   billing_type,
                   pricing_scheme,
                   metadata,
                   minimum_price,
                   cycles,
                   quantity,
                   trial_period_days)


