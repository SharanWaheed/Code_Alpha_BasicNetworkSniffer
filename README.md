Overview
This project is a basic Network Sniffer built in Python that captures and analyzes network traffic. It helps you understand how data flows on a network and how network packets are structured.

Features
Captures live network traffic.
Displays details about network packets including source IP, destination IP, protocol, and packet size.
Can be customized to capture specific types of traffic (e.g., TCP, UDP, HTTP).
Provides a user-friendly interface for real-time packet capture and analysis.
Requirements
Python 3.x
Scapy library for packet capturing and analysis
You can install Scapy using pip:
pip install scapy
How to Run
Clone the repository to your local machine:
git clone https://github.com/YOUR_GITHUB_USERNAME/Code_Alpha_BasicNetworkSniffer.git
Navigate to the project directory:
bash
Copy code
cd Code_Alpha_BasicNetworkSniffer/task1
Run the network_sniffer.py script:
bash
Copy code
sudo python3 network_sniffer.py
Note: You need sudo to capture packets on certain interfaces, as this requires administrative privileges.
