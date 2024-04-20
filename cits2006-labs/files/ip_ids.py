# you will need pyshark library for this code to work
# pip install pyshark

import pyshark

def live_monitoring():
    while True:
        capture = pyshark.LiveCapture(interface='eth0')
        for packet in capture.sniff_continuously(packet_count=1):
            print('Just arrived:', packet)

    
def process_pcap(file_path):
    cap = pyshark.FileCapture(file_path, display_filter='ip')
    for packet in cap:
        #alert if destination ip is 52.8.178.58
        try: #ip may not exist
            if packet.ip.dst == '52.8.178.58':
                print('Alert! accessed malicious IP')
        except:
            pass
    print("Done!")


def live_alert():
    print("Live monitoring started...")
    counter = 1
    while True:
        #update your interface as needed
        #check ipconfig/ifconfig and use the name that has an ip address
        capture = pyshark.LiveCapture(interface='enth', bpf_filter='tcp')
        for packet in capture.sniff_continuously(packet_count=2000):
            try: #not all packets have ip
                if packet.ip.dst in ['31.3.96.40', '104.154.89.105']:
                    print(f'Alert! accessed malicious site! {counter}')
                    counter += 1
            except:
                pass

# 31.3.96.40 - www.itsecgames.com
# 104.154.89.105 - badssl.com

def main():
    live_monitoring() # ctrl + C to stop
    # process_pcap('test.pcap')
    # live_alert() # ctrl + C to stop

if __name__ == '__main__':
    main()


