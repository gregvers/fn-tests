import io
import json
from requests import get

from fdk import response

def handler(ctx, data: io.BytesIO=None):
    ext_ip = get('https://api.ipify.org').text

    return response.Response(
        ctx,
        response_data=json.dumps({"IP": ext_ip}),
        headers={"Content-Type": "application/json"}
    )
