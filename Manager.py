from datetime import datetime

from include import Assistant_Settings as settings
from include import Connection_Header as msg_hdr
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
from rasa_core.utils import EndpointConfig

import re
import speech_recognition
import zmq
import time


class Pixy():

    def __init__(self):
        print("Pixy Started", datetime.now())
        try:
            self.context = zmq.Context()
            self.socket = self.context.socket(zmq.REQ)
            self.socket.connect("tcp://localhost:3978")
            self.poller = zmq.Poller()
            self.poller.register(self.socket, zmq.POLLIN)
            self.poll_timeout = settings.POLL_TIMEOUT
            self.sr = speech_recognition.Recognizer()
            self.mic = speech_recognition.Microphone()
            self.interpreter = RasaNLUInterpreter('./RASA/models/nlu/default/Assistant')
            self.action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
            self.agent = Agent.load('./RASA/models/dialogue', interpreter=self.interpreter,
                                    action_endpoint=self.action_endpoint)

            self.firstRun()

        except zmq.ZMQError as e:
            # Terminate the Application and Notify the Unity to terminate.
            self.send_frame(msg_hdr.ERROR_INIT)

    def receive_frame(self):
        print("Reciving Frame...")
        events = dict(self.poller.poll(self.poll_timeout))
        if events.get(self.socket) == zmq.POLLIN:
            message = self.socket.recv_string()
            if message:
                print("Received:" + message)
                return message
        print("No Message Received.")
        return None

    def run(self):
        msg = self.receive_frame()

        if msg == msg_hdr.ACK_RECOGNIZE_SPEECH:

            user_input = self.listen_speech()

            if user_input not in [msg_hdr.ERROR_STT_FAIL_TO_RECOGNIZE, msg_hdr.ERROR_NETWORK_CONNECTIVITY]:
                output = self.process_user_input(user_input)
            else:
                output = user_input

            self.send_frame(output)

        if msg == msg_hdr.ACK_RECEIVED:
            print("We are all good")

    def send_frame(self, message):
        print("Sending Frame...")
        self.socket.send_string(message)

    def firstRun(self):
        """
        PROBLEM: If ResponseSocket is offline even after the Poll Timeout, then RequestSocket wait for infinite amount of time because of the zmq message queue being loaded with initial message.
                Message Queue need to be Flushed in order to terminate python safely.
        TODO: Add a check to see if ResponseSocket is Running Before RequestSocket.
        :return:
        """
        self.send_frame(msg_hdr.ACK_FIRST_RUN)

    def listen_speech(self):
        '''
        TODO: Play Beep Sound when start listening
        TODO: Stop the Assistant when google error
        TODO: IF Number of Timeout greater then 10, Power OFF
        :return:
        '''
        hypothesis = None

        with self.mic as self.source:
            self.sr.adjust_for_ambient_noise(self.source)

            try:
                print("Listening...")
                audio = self.sr.listen(self.source, timeout=3, phrase_time_limit=7)
                hypothesis = self.sr.recognize_google(audio)
                print("You Spoke ..." + hypothesis)
            except speech_recognition.UnknownValueError:
                print(msg_hdr.ERROR_STT_FAIL_TO_RECOGNIZE)
                hypothesis = msg_hdr.ERROR_STT_FAIL_TO_RECOGNIZE
            except speech_recognition.WaitTimeoutError:
                print(msg_hdr.ERROR_STT_FAIL_TO_RECOGNIZE)
                hypothesis = msg_hdr.ERROR_STT_FAIL_TO_RECOGNIZE
            except speech_recognition.RequestError:
                print(msg_hdr.ERROR_NETWORK_CONNECTIVITY)
                hypothesis = msg_hdr.ERROR_NETWORK_CONNECTIVITY

        return hypothesis

    def process_user_input(self, input):
        intent = self.interpreter.parse(input)
        custom_action_pattern = re.compile("get_[a-z][A-Z]]")
        custom_action = re.match(custom_action_pattern, intent['intent']['name'])

        predict = self.agent.handle_text(str(input))
        print(predict[0]['text'])
        return predict[0]['text']


if __name__ == "__main__":

    pixy = Pixy()

    while True:
        pixy.run()
