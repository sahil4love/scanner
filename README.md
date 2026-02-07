# Sahiko Port Scanner & Banner Grabber

A fast, multi-threaded **TCP port scanner** written in Python that scans for open ports and attempts to **grab service banners** (“manners”). Built using only the Python standard library and designed for clean, readable terminal output.

```
███████╗ █████╗ ██╗  ██╗██╗██╗  ██╗ ██████╗ 
██╔════╝██╔══██╗██║  ██║██║██║ ██╔╝██╔═══██╗
███████╗███████║███████║██║█████╔╝ ██║   ██║
╚════██║██╔══██║██╔══██║██║██╔═██╗ ██║   ██║
███████║██║  ██║██║  ██║██║██║  ██╗╚██████╔╝
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝ ╚═════╝ 
        Port Scanner & Banner Grabber
```

---

## Features

- Multi-threaded TCP port scanning
- Banner (service response) grabbing
- Uses `ThreadPoolExecutor` (max 100 threads)
- Colorized terminal output
- Displays:
  - Open port number
  - Detected service name (if available)
  - First response line from the service
- No third-party dependencies

---

## Requirements

- Python 3.7 or higher
- Works on Linux, macOS, and Windows (ANSI color support required)

---

## Usage

```bash
python scanner.py <host> <start_port> <end_port>
```

### Examples

Scan default ports (1–1024):
```bash
python scanner.py example.com
```

Scan a custom range:
```bash
python scanner.py 192.168.1.1 20 500
```

---

## Output Example

```text
[+] Port 22    | ssh      | SSH-2.0-OpenSSH_8.2p1
[+] Port 80    | http     | HTTP/1.1 200 OK
[+] Port 443   | https   | Connected (No Manner)
```

---

## How It Works

1. Resolves the target hostname to an IP address
2. Iterates through the specified port range
3. Uses a thread pool to scan ports concurrently
4. For each open port:
   - Attempts to identify the service using `getservbyport`
   - Sends a basic HTTP GET request to grab a banner
5. Prints results in real time

---

## Notes & Limitations

- Banner grabbing uses a simple HTTP request
- Non-HTTP services may not return meaningful data
- Closed or filtered ports are silently ignored
- This is not a stealth scanner
- Intended for learning and basic reconnaissance

---

## Legal Disclaimer

This tool is intended for **educational purposes and authorized testing only**.  
Scanning systems or networks without permission may be illegal.

**Use responsibly.**

---

## License

MIT License
