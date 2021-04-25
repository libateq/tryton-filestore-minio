************
Installation
************

Prerequisites
=============

* Python 3.6 or later (http://www.python.org/)
* See the :file:`setup.py` file for Python package dependencies.

Using ``pip``
=============

The easiest way to install this package and it's dependencies is directly from
the Python Package Index:

.. code-block:: bash

   pip3 install tryton_filestore_minio

Using sources
=============

Alternatively, you can clone the *tryton-filestore-minio* repository, and
install the package from there:

.. code-block:: bash

   git clone https://bitbucket.org/libateq/tryton-filestore-minio
   cd tryton-filestore-minio
   python3 setup.py install

Other information
=================

You may need administrator/root privileges to perform the installation, as the
install commands will by default attempt to install the package to the system
wide Python site-packages directory on your system.

For advanced options, please refer to the standard Python packaging and
installation documentation:

* https://docs.python.org/3/installing/index.html
