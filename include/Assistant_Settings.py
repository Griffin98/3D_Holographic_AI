"""
This File Contains Configurable Settings of HVA Server.
"""


# Configure RASA
RASA_NLU_MODEL="./RASA/models/nlu/default/Assistant"


# API KEYS
ZOMATO_API = "df4b95e9cbcc6a7c090647586f563d23"


# Configure ZMQ
POLL_TIMEOUT = 60000 # in milliseconds
NUMBER_OF_CONNECTION_RETRIES = 20
