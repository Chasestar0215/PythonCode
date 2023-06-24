from scapy.all import *
import csv

packets = rdpcap(r'C:\Users\逐星i\OneDrive\桌面\vm-2.pcap')

with open(r'C:\Users\逐星i\OneDrive\桌面\vm-2.csv', 'w', newline='') as csvfile:
    fieldnames = ['Source_IP', 'Dest_IP', 'Protocol', 'Length']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for packet in packets:
        src_ip = packet['IP'].src
        dst_ip = packet['IP'].dst
        proto = packet['IP'].proto
        length = len(packet)

        writer.writerow({'Source_IP': src_ip, 'Dest_IP': dst_ip, 'Protocol': proto, 'Length': length})

print("Done!")
