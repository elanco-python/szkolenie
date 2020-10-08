# pip install opencensus-ext-azure
# pip install opencensus-ext-requests
# pip install psutil

import requests
import logging

from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.trace import config_integration
from opencensus.ext.azure.log_exporter import AzureLogHandler
from opencensus.trace.tracer import Tracer
from opencensus.ext.azure import metrics_exporter
from opencensus.trace.samplers import ProbabilitySampler

import time

import psutil

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# dodaj suffix do wysylanych danych
def callback_function(envelope):
    envelope.data.baseData.message += '_mw'
    return True


cs = 'InstrumentationKey=5d1bc94f-8358-4acf-bfe0-2c4f396e92fd;IngestionEndpoint=https://westeurope-1.in.applicationinsights.azure.com/'

# TODO: replace  with your instrumentation key.
handler = AzureLogHandler(connection_string=cs)
handler.add_telemetry_processor(callback_function) # wysyłanie telemetrii do Insight

logger.addHandler(handler)

exporter = metrics_exporter.new_metrics_exporter(connection_string=cs)

config_integration.trace_integrations(['requests'])
tracer = Tracer(exporter=AzureExporter( connection_string=cs), sampler=ProbabilitySampler(1.0), )
logger.error("Ale błąd")

for i in range(10):
        print(psutil.virtual_memory())
        time.sleep(5)
        with tracer.span(name='parent'):
            response = requests.get(url='https://www.wikipedia.org/wiki/Rabbit')
            print(response.status_code)

            properties = {'custom_dimensions': {'key_1': 'value_1', 'key_2': 'value_2'}}
            try:
                result = 1 / 0  # generate a ZeroDivisionError
            except Exception as exc:
                logger.exception(exc, extra=properties)


logger.warning("Komunikat WARNING")
logger.error("Komunikat ERROR")
logger.info("Komunikat INFO")


