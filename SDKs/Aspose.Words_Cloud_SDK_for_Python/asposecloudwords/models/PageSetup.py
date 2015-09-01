#!/usr/bin/env python

class PageSetup(object):
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            'Bidi': 'bool',
            'BorderAlwaysInFront': 'bool',
            'BorderAppliesTo': 'str',
            'BorderDistanceFrom': 'str',
            'BottomMargin': 'float',
            'DifferentFirstPageHeaderFooter': 'bool',
            'FirstPageTray': 'int',
            'FooterDistance': 'float',
            'Gutter': 'float',
            'HeaderDistance': 'float',
            'LeftMargin': 'float',
            'LineNumberCountBy': 'int',
            'LineNumberDistanceFromText': 'float',
            'LineNumberRestartMode': 'str',
            'LineStartingNumber': 'int',
            'Orientation': 'str',
            'OtherPagesTray': 'int',
            'PageHeight': 'float',
            'PageNumberStyle': 'str',
            'PageStartingNumber': 'int',
            'PageWidth': 'float',
            'PaperSize': 'str',
            'RestartPageNumbering': 'bool',
            'RightMargin': 'float',
            'RtlGutter': 'bool',
            'SectionStart': 'str',
            'SuppressEndnotes': 'bool',
            'TopMargin': 'float',
            'VerticalAlignment': 'str',
            'link': 'Link'

        }

        self.attributeMap = {
            'Bidi': 'Bidi','BorderAlwaysInFront': 'BorderAlwaysInFront','BorderAppliesTo': 'BorderAppliesTo','BorderDistanceFrom': 'BorderDistanceFrom','BottomMargin': 'BottomMargin','DifferentFirstPageHeaderFooter': 'DifferentFirstPageHeaderFooter','FirstPageTray': 'FirstPageTray','FooterDistance': 'FooterDistance','Gutter': 'Gutter','HeaderDistance': 'HeaderDistance','LeftMargin': 'LeftMargin','LineNumberCountBy': 'LineNumberCountBy','LineNumberDistanceFromText': 'LineNumberDistanceFromText','LineNumberRestartMode': 'LineNumberRestartMode','LineStartingNumber': 'LineStartingNumber','Orientation': 'Orientation','OtherPagesTray': 'OtherPagesTray','PageHeight': 'PageHeight','PageNumberStyle': 'PageNumberStyle','PageStartingNumber': 'PageStartingNumber','PageWidth': 'PageWidth','PaperSize': 'PaperSize','RestartPageNumbering': 'RestartPageNumbering','RightMargin': 'RightMargin','RtlGutter': 'RtlGutter','SectionStart': 'SectionStart','SuppressEndnotes': 'SuppressEndnotes','TopMargin': 'TopMargin','VerticalAlignment': 'VerticalAlignment','link': 'link'}       

        self.Bidi = None # bool
        self.BorderAlwaysInFront = None # bool
        self.BorderAppliesTo = None # PageBorderAppliesTo
        self.BorderDistanceFrom = None # PageBorderDistanceFrom
        self.BottomMargin = None # float
        self.DifferentFirstPageHeaderFooter = None # bool
        self.FirstPageTray = None # int
        self.FooterDistance = None # float
        self.Gutter = None # float
        self.HeaderDistance = None # float
        self.LeftMargin = None # float
        self.LineNumberCountBy = None # int
        self.LineNumberDistanceFromText = None # float
        self.LineNumberRestartMode = None # LineNumberRestartMode
        self.LineStartingNumber = None # int
        self.Orientation = None # Orientation
        self.OtherPagesTray = None # int
        self.PageHeight = None # float
        self.PageNumberStyle = None # NumberStyle
        self.PageStartingNumber = None # int
        self.PageWidth = None # float
        self.PaperSize = None # PaperSize
        self.RestartPageNumbering = None # bool
        self.RightMargin = None # float
        self.RtlGutter = None # bool
        self.SectionStart = None # SectionStart
        self.SuppressEndnotes = None # bool
        self.TopMargin = None # float
        self.VerticalAlignment = None # PageVerticalAlignment
        self.link = None # Link
        
