
#  pip install azure-mgmt-compute
#  pip install azure-identity

# VM w Azurze
from azure.identity import ClientSecretCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.compute.models import VirtualMachine
import os, json
from pprint import pprint

SUBSCRIPTION_ID = "fd6954c4-2b2067e5"
CLIENT_ID = "914edb1343db7"
CLIENT_SECRET = "F1~QVAKdM4z5r"
TENANT_ID = "0ae705ecaf731"

# pobieranie wartości ze zmiennej środowiskowej
result = os.environ.get("SUBSCRIPTION_ID", "")

credentials = ClientSecretCredential(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    tenant_id=TENANT_ID
)
compute_client : ComputeManagementClient = \
    ComputeManagementClient(credentials, SUBSCRIPTION_ID)

for vm in compute_client.virtual_machines.list_all():
    pprint(json.dumps(vm.as_dict()), indent=4)

compute_client.virtual_machines.begin_create_or_update(
    "test", "linux-marian",
    VirtualMachine(location="westeurope", tags={
        "departament" : "IT", "location" : "Warsaw"
    })
).wait()

print("="*80)
print("Poczatek restartu")
event = compute_client.virtual_machines.begin_restart("test","linux-marian")
event.wait()
print("Koniec restartu")

print("="*80)
print("Poczatek shutdown")
event = compute_client.virtual_machines.begin_power_off("test","linux-marian")
event.wait()
print("Koniec shutdown")

print("="*80)
print("Poczatek start")
event = compute_client.virtual_machines.begin_start("test","linux-marian")
event.wait()
print("Koniec start")
