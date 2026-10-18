
from datetime import datetime
from scapy.all import sniff, IP, TCP, UDP, ICMP


def show_packet(packet):
    """Display basic metadata for an observed IP packet."""

    if IP not in packet:
        return

    ip = packet[IP]

    if TCP in packet:
        protocol = "TCP"
        ports = f"{packet[TCP].sport} -> {packet[TCP].dport}"
    elif UDP in packet:
        protocol = "UDP"
        ports = f"{packet[UDP].sport} -> {packet[UDP].dport}"
    elif ICMP in packet:
        protocol = "ICMP"
        ports = "N/A"
    else:
        protocol = str(ip.proto)
        ports = "N/A"

    timestamp = datetime.now().strftime("%H:%M:%S")

    print("-" * 60)
    print(f"Time:        {timestamp}")
    print(f"Source IP:   {ip.src}")
    print(f"Destination: {ip.dst}")
    print(f"Protocol:    {protocol}")
    print(f"Ports:       {ports}")
    print(f"IP Length:   {ip.len} bytes")


def main():
    print("Basic Network Sniffer")
    print("Capturing authorized traffic only.")
    print("Press Ctrl+C to stop.")
    print("-" * 60)

    try:
        sniff(
            filter="ip",
            prn=show_packet,
            store=False
        )
    except KeyboardInterrupt:
        print("\nCapture stopped.")
    except Exception as error:
        print(f"Capture error: {error}")
        print("Check Npcap, permissions, and the selected interface.")


if __name__ == "__main__":
    main()