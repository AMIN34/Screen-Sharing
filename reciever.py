from vidstream import StreamingServer
import threading


recv = StreamingServer("192.168.1.7",8888)

recv.start_server()


while input("")!="STOP":
    continue

recv.stop_server()
