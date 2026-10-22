"""Configuration for the Fantasia ECG stream."""
import os

# QuestDB ILP (line protocol) — ingestion path, 9009
ILP_CONFIG = {
    'host': os.getenv('QDB_ILP_HOST', os.getenv('QDB_PG_HOST', 'localhost')),
    'port': int(os.getenv('QDB_ILP_PORT', '9009')),
}

# QuestDB pg-wire — queries and DDL, 8812
QDB_CONFIG = {
    'dbname': os.getenv('QDB_PG_NAME', 'qdb'),
    'user': os.getenv('QDB_PG_USER', 'admin'),
    'password': os.getenv('QDB_PG_PASSWORD', 'quest'),
    'host': os.getenv('QDB_PG_HOST', 'localhost'),
    'port': os.getenv('QDB_PG_PORT', '8812'),
}

# ECG Stream Configuration
ECG_CONFIG = {
    'table': 'ecg_fantasia_steps',
    'data_dir': os.getenv('ECG_DATA', 'data'),
    'records': 'records.txt',        # Fantasia record names and IDs, in order
    'dataset': 'fantasia/1.0.0',
    'channel': 'ECG',                # the ECG signal of every record
    # Fantasia records were sampled at 250 Hz and last about 120 minutes; each is
    # streamed at the native rate: 1 sample = 1/250 s. No resampling.
    'rate_hz': 250.0,
    'packet_steps': 250,             # one packet per second
    'max_steps': None,               # None = every record, whole length
}

# Logging Configuration
LOG_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s %(levelname)s %(message)s',
    'file': 'logs/ecg_validation.log',
}
