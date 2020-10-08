
from azure.storage.blob import ContainerClient, \
    BlobServiceClient, BlobClient, StandardBlobTier, PremiumPageBlobTier

cs = "DefaultEndpointsProtocol=https;AccountName="

blob_service_client : BlobServiceClient  = BlobServiceClient.from_connection_string(cs)
account_info = blob_service_client.get_account_information()
print(account_info)

# tworzenie kontenera dla blobow
container_client : ContainerClient = ContainerClient.from_connection_string(
    conn_str=cs, container_name="kontener1")
try:
    container_client.create_container()
    metadata = { "type" : "test", "owner" : "mw" }
    container_client.set_container_metadata(metadata=metadata)
    props = container_client.get_container_properties().metadata
    print(props)

    # upload do kontenera
    blob : BlobClient = BlobClient.from_connection_string(conn_str=cs,
                                             container_name="kontener1",
                                             blob_name="obraz.jpg")
    with open("../Dzien03/tablice/DW501XX.jpg", "rb") as fd:
        blob.upload_blob(fd, overwrite=True)
        #blob.set_standard_blob_tier(StandardBlobTier.Archive)
        #blob.set_premium_page_blob_tier(PremiumPageBlobTier.P6)

    # pobierz blob
    blob_client = blob_service_client.get_blob_client(
        container="kontener1", blob="obraz.jpg")
    with open("blob.jpg", "wb") as fd:
        fd.write( blob_client.download_blob().readall() )
        blob_client.delete_blob()

    print("="*80)
    for blob in container_client.list_blobs():
        print(blob)

    containers = blob_service_client.list_containers(include_metadata=True)
    for c in containers:
        print(c)


except Exception as exc:
    print(exc)
finally:
    blob_service_client.delete_container("kontener1")