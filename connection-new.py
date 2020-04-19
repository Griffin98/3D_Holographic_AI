from datetime import datetime
import zmq
import time
# Poll Timeout in millisec
TIMEOUT = 10000

class Manager:

    def __init__(self):
        print("Manager Service Started at: ", datetime.now())
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect("tcp://localhost:3978")
        self.poller = zmq.Poller()
        self.poller.register(self.socket, zmq.POLLIN)
        self.poll_timeout = TIMEOUT
        self.firstRun()

    def send_frame(self,message):
        print("Sending Frame...")
        self.socket.send_string(message)

    def recv_frame(self):
        print("Reciving Frame...")
        events = dict(self.poller.poll(self.poll_timeout))
        if events.get(self.socket) == zmq.POLLIN:
            message = self.socket.recv_string()
            if message:
                print("Received: " + message)
                return message
        return None



    def firstRun(self):
        """
        PROBLEM: If ResponseSocket is offline even after the Poll Timeout, then RequestSocket wait for infinite amount of time because of the zmq message queue being loaded with initial message.
                Message Queue need to be Flushed in order to terminate python safely.
        TODO: Add a check to see if ResponseSocket is Running Before RequestSocket.
        :return:
        """
        self.send_frame("firstRun")
        status = self.recv_frame()
        if status == 'Started':
            self.send_frame("Status")
            status = self.recv_frame()

    def startSpeechRecognize(self):
        print("hi")



if __name__ == "__main__":

    Manager()