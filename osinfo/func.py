import io
import json
import subprocess

from fdk import response


def handler(ctx, data: io.BytesIO=None):
    MyOut = subprocess.Popen(['uname', '-a'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
    stdout,stderr = MyOut.communicate()

    return response.Response(
        ctx,
        response_data=stdout,
        headers={"Content-Type": "application/json"}
    )
