#!/usr/bin/env python3
# This file is part of the filestore-minio package.
# Please see the COPYRIGHT and README.rst files at the top level of this
# package for full copyright notices, license terms and support information.
from io import open
from os.path import dirname, join
from re import sub

from setuptools import setup


def read(fname):
    content = open(
        join(dirname(__file__), fname), 'r', encoding='utf-8').read()
    content = sub(r'(?m)^\.\. toctree::\r?\n((^$|^\s.*$)\r?\n)*', '', content)
    return content


setup(
    name='tryton-filestore-minio',
    version='0.2.2',
    description=(
        "Uses the Python MinIO client to store Tryton files in S3 compatible "
        "object storage services"),
    long_description=read('README.rst'),
    long_description_content_type='text/x-rst',
    author='David Harper',
    author_email='tryton@libateq.org',
    url='https://bitbucket.org/libateq/tryton-filestore-minio',
    project_urls={
        "Bug Tracker": (
            'https://bitbucket.org/libateq/tryton-filestore-minio/issues'),
        "Source Code": 'https://bitbucket.org/libateq/tryton-filestore-minio',
        "Documentation": (
            'https://tryton-filestore-minio.readthedocs.io/en/latest/'),
        },
    keywords='tryton filestore s3 storage minio',
    classifiers=[
        'Framework :: Tryton',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',  # noqa: E501
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet',
        ],
    py_modules=['tryton_filestore_minio'],
    python_requires='>=3.7',
    install_requires=[
        'minio',
        'urllib3',
        ],
    extras_require={
        'tryton': ['trytond>=5.0'],
        },
    zip_safe=False,
    )
