from scapy.all import IP,ICMP,Raw
packet = IP(dst="8.8.8.8")/ ICMP() / Raw(load="payloading")
packet.show()
print(packet[IP].src)

