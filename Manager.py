import ConnectionManager as Conn


def listener_service():
    print("x")

def pixy():
    while Conn.Trigger_Message!=None:
        print()
    print("Received",Conn.Trigger_Message)
    Conn.Trigger_Message = ""
    Conn.send_frame("Hi")


if __name__ == "__main__":
    pixy()