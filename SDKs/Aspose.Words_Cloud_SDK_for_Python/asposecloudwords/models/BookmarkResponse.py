#!/usr/bin/env python

class BookmarkResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            'Bookmark': 'Bookmark',
            'Code': 'str',
            'Status': 'str'

        }

        self.attributeMap = {
            'Bookmark': 'Bookmark','Code': 'Code','Status': 'Status'}       

        self.Bookmark = None # Bookmark
        self.Code = None # str
        self.Status = None # str
        