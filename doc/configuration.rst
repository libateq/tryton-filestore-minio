*************
Configuration
*************

In order to make Tryton's :py:mod:`~trytond.filestore` use S3 object storage
the ``class`` option must be set to ``tryton_filestore_minio.FileStoreMinIO``
in the ``[database]`` section of the
:doc:`configuration file <trytond:topics/configuration>`.

The connection settings must also be configured in the ``[minio]`` section of
the configuration file.

.. _config-minio.endpoint:

``endpoint``
============

The hostname for the S3 service to use.
The port can also be specified by including it at the end after
a colon (``:``).

The default value is: ``s3.amazonaws.com``

.. _config-minio.secure:

``secure``
==========

Indicates whether to connect using a secure (TLS) connection or not.

The default value is: ``True``

.. _config-minio.access_key:

``access_key``
==============

The access key (sometimes also called the user id) for the account that Tryton
should use when connecting to the S3 service.

If not specified connections will be attempted anonymously.

.. _config-minio.secret_key:

``secret_key``
==============

The secret key (sometimes also referred to as the password) for the account
that Tryton should use when connecting to the S3 service.

.. _config-minio.region:

``region``
==========

The name of the region where the buckets can be found in the S3 service.

This value is optional.

.. _config-minio.bucket:

``bucket``
==========

The name of the bucket that Tryton should use to store the files in.

The default value is: ``tryton``
