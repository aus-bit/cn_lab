
import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

host = socket.gethostbyname(socket.gethostname())

s.bind((host, 0))

s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

print("Packet capturing started...")

try:
    while True:
        
        packet, addr = s.recvfrom(65565)

        ip_header = packet[0:20]

        iph = struct.unpack('!BBHHHBBH4s4s', ip_header)

        version_ihl = iph[0]
        ihl = (version_ihl & 15) * 4

        ttl = iph[5]
        protocol = iph[6]

        src_ip = socket.inet_ntoa(iph[8])
        dest_ip = socket.inet_ntoa(iph[9])

        if protocol == 1:
            protocol_name = "ICMP"
        elif protocol == 6:
            protocol_name = "TCP"
        elif protocol == 17:
            protocol_name = "UDP"
        else:
            protocol_name = "Other"

        print("\nPacket Captured")
        print("Source IP:", src_ip)
        print("Destination IP:", dest_ip)
        print("Protocol:", protocol_name)
        print("Packet Size:", len(packet))
        print("TTL:", ttl)

except KeyboardInterrupt:
    print("\nPacket capturing stopped.")

    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
    s.close()
