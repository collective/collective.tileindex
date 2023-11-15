# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from plone.app.blocks.layoutbehavior import ILayoutBehaviorAdaptable
from plone.app.blocks.layoutbehavior import ILayoutAware
from plone.indexer.decorator import indexer

try:
    from plone.base.utils import base_hasattr
except ImportError:
    # BBB Plone 5.2
    from Products.CMFPlone.utils import base_hasattr


@indexer(ILayoutBehaviorAdaptable)
def tile_types(obj):
    """Calculate and return the value for the indexer"""
    if not base_hasattr(obj, "__annotations__"):
        return
    if obj.getProperty("layout", "") != "layout_view":
        return

    # Get the tiles from the content layout.
    layout = ILayoutAware(obj)
    content_layout = layout.content_layout()
    if not content_layout:
        return
    soup = BeautifulSoup(content_layout, features="lxml")
    # We search for content like this.
    # Persistent tile:
    # <div data-tile="./@@plone.app.standardtiles.html/some-tile-uid"></div>
    # Transient tile:
    # <div data-tile="./@@plone.app.standardtiles.field?field=IDublinCore-title"></div>
    divs = soup.find_all(attrs={"data-tile": True})
    tile_types = set()
    for dt in [d["data-tile"] for d in divs]:
        items = dt.split("/")
        if len(items) == 3:
            tile = items[1]
        elif len(items) == 2:
            tile = items[1].split("?")[0]
        else:
            continue
        tile = tile.strip("@")
        if not tile:
            continue
        tile_types.add(tile)

    return tile_types
