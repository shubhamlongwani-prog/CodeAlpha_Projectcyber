from scapy.all import Ether, IP, TCP,sniff,Raw

p = Ether()/IP(dst="www.secdev.org")/TCP()/Raw(load="working")
p.summary()
print(p.summary)
print(p.dst)  # first layer that has an src field, here Ether
print(p[IP].src)  # explicitly access the src field of the IP layer

# sprintf() is a useful method to display fields
print(p.sprintf("%Ether.src% > %Ether.dst%\n%IP.src% > %IP.dst%"))
s = sniff(count=2)
print(s)
sniff(count=2, prn=lambda p: p.summary())
