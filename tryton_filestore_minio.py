# This file is part of the filestore-minio package.
# Please see the COPYRIGHT and README.rst files at the top level of this
# package for full copyright notices, license terms and support information.
from io import BytesIO
from minio import Minio
from trytond.config import config
from trytond.filestore import FileStore
from uuid import uuid4


def get_name(id, prefix=''):
    return '/'.join(filter(None, [prefix, id]))


class FileStoreMinIO(FileStore):

    def __init__(self):
        self._client = None

    @property
    def client(self):
        if not self._client:
            self._client = Minio(
                config.get('minio', 'endpoint', default='s3.amazonaws.com'),
                secure=config.getboolean('minio', 'secure', default=True),
                access_key=config.get('minio', 'access_key', default=None),
                secret_key=config.get('minio', 'secret_key', default=None),
                region=config.get('minio', 'region', default=None),
                )
        return self._client

    @property
    def bucket(self):
        return config.get('minio', 'bucket', default='tryton')

    def get(self, id, prefix=''):
        name = get_name(id, prefix)
        try:
            response = self.client.get_object(self.bucket, name)
            return response.data
        finally:
            response.close()
            response.release_conn()

    def set(self, data, prefix=''):
        id = uuid4().hex
        name = get_name(id, prefix)
        self.client.put_object(self.bucket, name, BytesIO(data), len(data))
        return id

    def size(self, id, prefix=''):
        name = get_name(id, prefix)
        result = self.client.stat_object(self.bucket, name)
        return result.size
