# This file is part of the filestore-minio package.
# Please see the COPYRIGHT and README.rst files at the top level of this
# package for full copyright notices, license terms and support information.
from io import BytesIO
from minio import Minio
from trytond.config import config
from trytond.filestore import FileStore
from uuid import uuid4


def get_service_filename(id, prefix=None):
    filename = ''.join(filter(None, [prefix, id]))
    if ':' in filename:
        return filename.split(':', 1)
    return None, filename


def get_client_bucket(service):
    section = '_'.join(filter(None, ['minio', service]))
    client = Minio(
        config.get(section, 'endpoint', default='s3.amazonaws.com'),
        secure=config.getboolean(section, 'secure', default=True),
        access_key=config.get(section, 'access_key', default=None),
        secret_key=config.get(section, 'secret_key', default=None),
        region=config.get(section, 'region', default=None),
        )
    bucket = config.get(section, 'bucket', default='tryton')
    return client, bucket


class FileStoreMinIO(FileStore):

    def __init__(self):
        self._services = {}

    def _get_client_bucket_filename(self, id, prefix):
        service, filename = get_service_filename(id, prefix)
        if service not in self._services:
            client_bucket = get_client_bucket(service)
            self._services[service] = client_bucket
        return self._services[service] + (filename,)

    def get(self, id, prefix=''):
        client, bucket, name = self._get_client_bucket_filename(id, prefix)
        response = None
        try:
            response = client.get_object(bucket, name)
            return response.data
        finally:
            if response:
                response.close()
                response.release_conn()

    def set(self, data, prefix=''):
        id = uuid4().hex
        client, bucket, name = self._get_client_bucket_filename(id, prefix)
        client.put_object(bucket, name, BytesIO(data), len(data))
        return id

    def size(self, id, prefix=''):
        client, bucket, name = self._get_client_bucket_filename(id, prefix)
        result = client.stat_object(bucket, name)
        return result.size
