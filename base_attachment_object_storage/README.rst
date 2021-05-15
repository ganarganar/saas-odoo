===================================================
Base Class For Attachments On External Object Store
===================================================

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://raster.shields.io/badge/github-ganarganar%2Fsaas--odoo-lightgray.png?logo=github
    :target: https://github.com/ganarganar/saas-odoo/tree/13.0/base_attachment_object_storage
    :alt: ganarganar/saas-odoo

|badge1| |badge2| |badge3|

This is a base addon that regroup common code used by addons targeting specific object store.

**Table of contents**

.. contents::
   :local:

Configuration
=============

Object storage may be slow, and for this reason, we want to store
some files in the database whatever.

Small images (128, 256) are used in Odoo in list / kanban views. We
want them to be fast to read.
They are generally < 50KB (default configuration) so they don't take
that much space in database, but they'll be read much faster than from
the object storage.

The assets (application/javascript, text/css) are stored in database
as well whatever their size is:

* a database doesn't have thousands of them
* of course better for performance
* better portability of a database: when replicating a production
  instance for dev, the assets are included

This storage configuration can be modified in the system parameter
``ir_attachment.storage.force.database``, as a JSON value, for instance::

    {"image/": 51200, "application/javascript": 0, "text/css": 0}

Where the key is the beginning of the mimetype to configure and the
value is the limit in size below which attachments are kept in DB.
0 means no limit.

Default configuration means:

* images mimetypes (image/png, image/jpeg, ...) below 50KB are
  stored in database
* application/javascript are stored in database whatever their size
* text/css are stored in database whatever their size

Known issues / Roadmap
======================

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/ganarganar/saas-odoo/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`feedback <https://github.com/ganarganar/saas-odoo/issues/new?body=module:%20base_attachment_object_storage%0Aversion:%2013.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Ganar Ganar
* Camptocamp

Contributors
~~~~~~~~~~~~

* `Ganar Ganar <https://ganargan.ar/>`_:

  * Lucas Soto <lsoto@ganargan.ar>
  * Leandro Ramírez <lramirez@ganargan.ar>

* `Camptocamp <https://www.camptocamp.com/>`_

Maintainers
~~~~~~~~~~~

This module is maintained by Ganar Ganar.

.. image:: https://ganargan.ar/web/image?model=res.partner&id=1&field=image_128
    :alt: Ganar Ganar
    :target: https://ganargan.ar

.. |maintainer-sotolucas| image:: https://github.com/sotolucas.png?size=40px
    :target: https://github.com/sotolucas
    :alt: sotolucas

Current `maintainer <https://odoo-community.org/page/maintainer-role>`__:

|maintainer-sotolucas| 

This module is part of the `ganarganar/saas-odoo <https://github.com/ganarganar/saas-odoo/tree/13.0/base_attachment_object_storage>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
