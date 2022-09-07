import scapy.all as scapy


def scanner(ip):
    req = scapy.ARP(pdst=ip)
    # req.show()
    # making ARP request
    broadcast = scapy.Ether()
    broadcast.dst = "ff:ff:ff:ff:ff:ff"
    # scapy.ls(scapy.Ether()) #lists the attributes of the broadcast mac address; dst, src, type using  the
    # ether module

    # broadcast.show()
    # Ether framework creates the broadcast mac address
    req_broadcast = broadcast / req
    # req_broadcast.show()

    res1 = scapy.srp(req_broadcast, timeout=1)[0]

    for x in res1:
        print(x[1].psrc)  # for the ip address for clients in the network
        print(x[1].hwsrc)  # for the mac address for clients in the network


scanner("192.168.0.1/24")

# /24 to include every client in the network
