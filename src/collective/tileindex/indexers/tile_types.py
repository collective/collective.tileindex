# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

# from plone.app.contenttypes.interfaces import IDocument
from plone.dexterity.interfaces import IDexterityContent
from plone.indexer.decorator import indexer


@indexer(IDexterityContent)  # ADJUST THIS!
def tile_types(obj):
    """Calculate and return the value for the indexer"""

    return []
    import pdb

    pdb.set_trace()
    # Check if the object has a getLayout method (supports tiles)
    if hasattr(obj, "getLayout"):
        # Get the tiles (collection of tiles)
        content_layout = obj.getLayout()
        if content_layout:
            soup = BeautifulSoup(content_layout, features="lxml")
            divs = soup.find_all(attrs={"data-tile": True})
            mapping = {}
            for dt in [d["data-tile"] for d in divs]:
                items = dt.split("/")
                if len(items) == 3:
                    mapping[items[2]] = items[1]
                else:
                    # This tile has no annotation, so it might be a richtext tile showing the text field
                    continue
            return set(mapping.keys())

    return []
