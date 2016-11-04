c.NotebookApp.server_extensions = [
    'ganymede.ganymede',
]

from ganymede.ganymede import GanymedeHandler
import logstash
import os
if {"L41_LOGSTASH_HOST", "L41_LOGSTASH_PORT"} < set(os.environ):
    GanymedeHandler.handlers = [
        logstash.TCPLogstashHandler(
            os.environ["L41_LOGSTASH_HOST"],
            os.environ["L41_LOGSTASH_PORT"],
            version=1,
        )
    ]
