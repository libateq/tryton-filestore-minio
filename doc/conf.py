# This file is part of the filestore-minio package.
# Please see the COPYRIGHT and README.rst files at the top level of this
# package for full copyright notices, license terms and support information.

trytond_url = 'https://docs.tryton.org/projects/server/en/{series}/'


def get_copyright(first_year, author):
    import datetime

    current_year = datetime.date.today().year
    if first_year == current_year:
        return '{}, {}'.format(first_year, author)
    return '{}-{}, {}'.format(first_year, current_year, author)


def get_info():
    import os
    import subprocess
    import sys

    package_dir = os.path.dirname(os.path.dirname(__file__))

    info = {}
    for name in {'name', 'author', 'version'}:
        result = subprocess.run(
            [sys.executable, 'setup.py', '--{}'.format(name)],
            stdout=subprocess.PIPE, check=True, cwd=package_dir)
        info[name] = result.stdout.decode('utf-8').strip()
    info['release'] = info['version']

    return info


info = get_info()

project = info['name']
version = info['version']
release = info['release']
author = info['author']
copyright = get_copyright(2021, author)
default_role = 'ref'
highlight_language = 'none'
extensions = [
    'sphinx.ext.intersphinx',
    ]
intersphinx_mapping = {
    'trytond': (trytond_url.format(series='latest'), None),
    }

del get_copyright, get_info, info, trytond_url
