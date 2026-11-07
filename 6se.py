
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 1278))

print("Server waiting......")

while True:
    data, addr = s.recvfrom(1024)
    msg = data.decode()

    words = {
        "tbh": "to be honest",
        "ig": "I guess",
        "tbf": "to be fair",
        "irl": "in real life",
        "lol": "laughing out loud",
        "asap": "as soon as possible",
        "omg": "oh my god",
        "ttyl": "talk to you later",
        "idk": "I don't know",
        "nvm": "never mind"
    }

    for a, b in words.items():
        msg = msg.replace(a, b)

    s.sendto(msg.encode(), addr)
