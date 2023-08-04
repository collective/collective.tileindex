# -*- coding: utf-8 -*-

# from collective.tileindex import _
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class ITileTypesTestView(Interface):
    """Marker Interface for ITileTypesTestView"""


@implementer(ITileTypesTestView)
class TileTypesTestView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('tile_types_test_view.pt')

    def __call__(self):
        # Implement your own actions:
        return self.index()
