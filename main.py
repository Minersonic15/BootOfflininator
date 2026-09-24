import socket
import time
ip = "43.134.189.46"
port = 53
Message = b"Pythonfan32"

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.settimeout(3.0)
    try:
        sock.connect((ip, port))
        print("Heck yes")
        sock.sendto(Message, (ip, port))
        
    except socket.timeout:
        print("closed/blocked")
    except Exception:
        print("fuck")

    #time.sleep(0.001)
        
    
    

