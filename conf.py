# basedir is set by <lang>/conf.py
"""
Use "-D language=<LANG>" option to build a localized tvtk document.
For example::

    sphinx-build -D language=ja -b html . _build/html

This conf.py do:

- Specify `locale_dirs` and `gettext_compact`.
- Overrides source directory as 'mayavi/docs/source/tvtk`.

"""
import os
from sphinx.util.pycompat import execfile_

basedir = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "mayavi/docs/source/tvtk"
)

execfile_(os.path.join(basedir, "conf.py"), globals())

locale_dirs = [os.path.join(basedir, "../../../../locale/")]


def setup(app):
    from sphinx.util.docfields import GroupedField

    app.srcdir = basedir
    app.confdir = app.srcdir
    app.add_object_type(
        "confval",
        "confval",
        objname="configuration value",
        indextemplate="pair: %s; configuration value",
    )
    fdesc = GroupedField(
        "parameter", label="Parameters", names=["param"], can_collapse=True
    )

    # workaround for RTD
    from sphinx.util import logging

    logger = logging.getLogger(__name__)
    app.info = lambda *args, **kwargs: logger.info(*args, **kwargs)
    app.warn = lambda *args, **kwargs: logger.warning(*args, **kwargs)
    app.debug = lambda *args, **kwargs: logger.debug(*args, **kwargs)
