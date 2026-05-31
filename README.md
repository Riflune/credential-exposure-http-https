Analysis of Credential Exposure in HTTP and Protection Through HTTPS


Overview

This project demonstrates how login credentials transmitted over HTTP can be intercepted and viewed in plaintext using Wireshark, and how TLS encryption protects application-layer data during HTTPS communication.
A custom HTML login page and Python HTTP server were used to simulate credential submission in a controlled lab environment.



Objectives

- Analyze HTTP traffic
- Observe plaintext credential transmission
- Use Wireshark packet inspection
- Study TLS handshake behavior
- Compare HTTP and HTTPS security



Tools Used

- Wireshark
- Python 3
- HTML
- HTTP Protocol
- TLS Protocol



Lab Setup

![Lab Setup Diagram](lab_setup_diagram.jpeg)


Client Browser (192.168.1.4)
↓
HTTP Request
↓
Python HTTP Server (192.168.1.5:8000)
↓
Wireshark Packet Capture


## Project Evidence

### HTTP Follow TCP Stream

![HTTP Follow TCP Stream](HTTP_tcpstream.png)

### HTTP Form URL Encoded Data

![HTTP Form Data](http_url.png)

### Plaintext Credentials

![Plaintext Credentials](plaintext_credentials.png)

### TLS Server Hello

![TLS Server Hello](tls_server_hello.png)

### TLS Encrypted Traffic

![TLS Encrypted Traffic](tls_ciphertext.png)

### Python Server

![Python Server](server.py_image.png)

### Login Page

![Login Page](index.html_image.png)

### Protocol Hierarchy

![Protocol Hierarchy](protocol_hierarchy.png)

### Statistics

![Statistics](statistics.png)



Key Findings

HTTP Analysis
     Credentials submitted through HTTP were visible in plaintext.
     Wireshark's Follow TCP Stream feature reconstructed the complete login request.

TLS Analysis
    TLS handshake packets were visible during session establishment.
    Application-layer data remained encrypted and could not be inspected directly.



Security Implications

HTTP is vulnerable to:
- Packet sniffing
- Credential exposure
- Man-in-the-middle attacks

TLS encryption significantly improves confidentiality by protecting application data from packet-level inspection.



Skills Demonstrated

- Packet Analysis
- Wireshark
- HTTP Protocol Analysis
- TLS Inspection
- Network Security Fundamentals
- Cybersecurity Documentation

