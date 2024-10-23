import socket

def handle(req):
    ip = req.strip()
    openports = []
    for port in range(0, 500):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.02)
            res = s.connect_ex((ip, port))
            if res == 0:
                openports.append(port)
    if openports:
        return f"Open Ports are {openports}"
    else:
        return "No open ports found"
