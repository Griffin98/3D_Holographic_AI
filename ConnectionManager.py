import zmq
import multiprocessing
import SpeechRecognizer
from datetime import datetime

def worker(message):

    if(message == "FirstRun"):
        """"
        manager = multiprocessing.Manager()
        return_string = manager.dict()
        recognize_worker = multiprocessing.Process(target=SpeechRecognizer.recognize(),args=(return_string,))
        recognize_worker.start()
        recognize_worker.join()
        print(return_string.values())
        """
        send_frame("Greetings")

    if(message == "First Stage"):
        output = "hi"#input()
        send_frame(output)


def send_frame(string):
    """
    Function will Send Response to Client.Response can be Single Frame or Multipart Message.
    TODO: Handling Multipart Messages.
    :param string: Response to be sent.
    :return: null
    """
    ServerSocket.send_string(string)
    print("Send Successfull")

def receive_frame():
    """
    It will Receive Frames(Strings) from the client and pass it to manager function to handle.
    :return: NULL
    """
    while True:
        message: str = ServerSocket.recv_string()
        print("Message: %s" % message)
        worker(message)


if __name__ == "__main__":
    """
    Main Function will Bind ZMQ Server to port 3978.And Start Receiving Request from the client.
    """
    context = zmq.Context()
    ServerSocket = context.socket(zmq.REP)
    ServerSocket.bind("tcp://*:3978")

    print("ConnectionManager: Started at",datetime.now())

    conection_manager = multiprocessing.Process(target=receive_frame())


    conection_manager.start()
    conection_manager.join()