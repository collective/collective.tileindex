# -*- coding: utf-8 -*-
from collective.tileindex.testing import COLLECTIVE_TILEINDEX_FUNCTIONAL_TESTING
from collective.tileindex.testing import COLLECTIVE_TILEINDEX_INTEGRATION_TESTING
from collective.tileindex.views.tile_types_test_view import ITileTypesTestView
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from zope.component import getMultiAdapter
from zope.interface.interfaces import ComponentLookupError

import unittest


class ViewsIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_TILEINDEX_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        api.content.create(self.portal, "Folder", "other-folder")
        api.content.create(self.portal, "Document", "front-page")

    def test_tile_types_is_registered(self):
        view = getMultiAdapter(
            (self.portal["other-folder"], self.portal.REQUEST), name="tile-types"
        )
        self.assertTrue(ITileTypesTestView.providedBy(view))

    def test_tile_types_not_matching_interface(self):
        view_found = True
        try:
            view = getMultiAdapter(
                (self.portal["front-page"], self.portal.REQUEST), name="tile-types"
            )
        except ComponentLookupError:
            view_found = False
        else:
            view_found = ITileTypesTestView.providedBy(view)
        self.assertFalse(view_found)


class ViewsFunctionalTest(unittest.TestCase):

    layer = COLLECTIVE_TILEINDEX_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
