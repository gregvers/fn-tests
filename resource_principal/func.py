import io
import json
import oci
import logging


from fdk import response


def handler(ctx, data: io.BytesIO=None):

    logging.info('Getting signer...')
    signer = oci.auth.signers.ResourcePrincipalsSecurityTokenSigner()
    logging.info('Got signer: ' + str(signer))
    object_storage_client = oci.object_storage.ObjectStorageClient(config={}, signer=signer)
    logging.info('Got object storage client: ' + str(object_storage_client))

    return response.Response(
        ctx,
        response_data=json.dumps({}),
        headers={"Content-Type": "application/json"}
    )
