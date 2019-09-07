#!/usr/bin/env python3
import oci
from zipfile import ZipFile

OCI_CONFIG_LOC = "~/.oci/config"
adb_id = 'ocid1.autonomousdatabase.oc1.phx.abyhqljsxf2lq2biffqoxb3izvwtiddwxv6cumyy76axxcexqalcri77jjzq'
adb_wallet_pwd = 'W64*Jim.4tmojXqc'
dbwalletzip_location = "/Users/gverstra/Downloads/wallet.zip"
dbwallet_dir = "/Users/gverstra/Downloads/"

# authentication based on instance principal
#signer = oci.auth.signers.get_resource_principals_signer()
#object_storage_client = oci.object_storage.ObjectStorageClient(config={}, signer=signer)
# authentication based on oci config
config = oci.config.from_file(file_location=OCI_CONFIG_LOC)
adb_client = oci.database.DatabaseClient(config)
adb_wallet_details = oci.database.models.GenerateAutonomousDatabaseWalletDetails(password=adb_wallet_pwd)
print(adb_wallet_details)
obj = adb_client.generate_autonomous_database_wallet(adb_id, adb_wallet_details)
with open(dbwalletzip_location, 'w+b') as f:
    for chunk in obj.data.raw.stream(1024 * 1024, decode_content=False):
        f.write(chunk)
with ZipFile(dbwalletzip_location, 'r') as zipObj:
        zipObj.extractall(dbwallet_dir)

print("done.")
