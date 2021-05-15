========================
Attachment On S3 Storage
========================

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://raster.shields.io/badge/github-ganarganar%2Fsaas--odoo-lightgray.png?logo=github
    :target: https://github.com/ganarganar/saas-odoo/tree/13.0/attachment_s3
    :alt: ganarganar/saas-odoo

|badge1| |badge2| |badge3|

This addon allows to store the attachments (documents and assets) on S3 or any
other S3-compatible Object Storage.

**Table of contents**

.. contents::
   :local:

Configuration
=============

Activate S3 storage:

* Create or set the system parameter with the key ``ir_attachment.location``
  and the value in the form ``s3``.

Configure accesses with environment variables:

* ``AWS_HOST`` (not required if using AWS services)
* ``AWS_REGION`` (required if using AWS services)
* ``AWS_ACCESS_KEY_ID``
* ``AWS_SECRET_ACCESS_KEY``
* ``AWS_BUCKETNAME``

Read-only mode:

The bucket and the file key are stored in the attachment. So if you change the
``AWS_BUCKETNAME`` or the ``ir_attachment.location``, the existing attachments
will still be read on their former bucket. But as soon as they are written over
or new attachments are created, they will be created on the new bucket or on
the other location (db or filesystem). This is a convenient way to be able to
read the production attachments on a replication (since you have the
credentials) without any risk to alter the production data.

This addon must be added in the server wide addons with (``--load`` option):

``--load=web,attachment_s3``

The System Parameter ``ir_attachment.storage.force.database`` can be customized to
force storage of files in the database. See the documentation of the module
``base_attachment_object_storage``.

Known issues / Roadmap
======================

* You need to call ``env['ir.attachment'].force_storage()`` after
  having changed the ``ir_attachment.location`` configuration in order to
  migrate the existing attachments to S3.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/ganarganar/saas-odoo/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`feedback <https://github.com/ganarganar/saas-odoo/issues/new?body=module:%20attachment_s3%0Aversion:%2013.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

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

* `Camptocamp <https://www.camptocamp.com/>`_:

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

This module is part of the `ganarganar/saas-odoo <https://github.com/ganarganar/saas-odoo/tree/13.0/attachment_s3>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
