"""
This File Contains Communication Headers used in ZMQ Connectivity between Unity and Python.
"""

# Acknowledgement
ACK_CUSTOM_ACTION = "customaction"
ACK_FIRST_RUN = "firstrun"
ACK_PLAY_PROGRESS_ANIM = "playprogressanim"
ACK_PLAYING_PROGRESS_ANIM = "playprogressanim"
ACK_RECEIVED = "received"
ACK_RECOGNIZE_SPEECH = "recognizespeech"
ACK_SMALL_TALK = "smalltalk"

# Error
ERROR_CUSTOM_ACTION = "failtoreachapi"
ERROR_STT_FAIL_TO_RECOGNIZE = "failtorecognize"
ERROR_STT_WAIT_TIMEOUT = "waittimeout"
ERROR_INIT = "initerror"
ERROR_PCM_LIB = "fatalerror"
ERROR_UNITY = "unityerror"
ERROR_NETWORK_CONNECTIVITY = "nonetwork"

# Message
MESSAGE_FAIL_TO_RECOGNIZE = "Sorry! I didn't Get You, Would you speak again."