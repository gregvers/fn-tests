import io
import json
import oci
import os
import shutil
import logging
from zipfile import ZipFile

from fdk import response


def handler(ctx, data: io.BytesIO=None):

    # authentication based on instance principal
    signer = oci.auth.signers.get_resource_principals_signer()
    object_storage_client = oci.object_storage.ObjectStorageClient(config={}, signer=signer)
    # authentication based on oci config
    #config = oci.config.from_file(file_location=OCI_CONFIG_LOC)
    #object_storage_client = oci.object_storage.ObjectStorageClient(config)
    
    # common
    obj = object_storage_client.get_object(
        object_storage_client.get_namespace().data, bucket_name, object_name)
    dbwallet_dir = os.environ['TNS_ADMIN']
    dbwalletzip_location = os.path.join(dbwallet_dir, object_name)
    if os.path.exists(dbwallet_dir):
        shutil.rmtree(dbwallet_dir)
    os.mkdir(dbwallet_dir)
    with open(dbwalletzip_location, 'w+b') as f:
        for chunk in obj.data.raw.stream(1024 * 1024, decode_content=False):
            f.write(chunk)

    return response.Response(
        ctx, response_data=json.dumps(
            {"message": "Hello {0}".format(name)}),
        headers={"Content-Type": "application/json"}
    )
