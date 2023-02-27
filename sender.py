from vidstream import ScreenShareClient
import threading


sender = ScreenShareClient("192.168.1.7",8888)

sender.start_stream()

while input("")!="STOP":
    continue

sender.stop_stream()
