from faker import Faker
import random
from datetime import datetime

fake = Faker()

def generate_ssh_log(success=True):
    timestamp = datetime.now().strftime('%b %d %H:%M:%S')
    hostname = fake.hostname()
    ip_address = fake.ipv4_public()
    port = random.randint(1024, 65535)
    username = fake.user_name()
    pid = random.randint(1000, 9999)

    if success:
        message = f"Accepted password for {username} from {ip_address} port {port} ssh2"
    else:
        message = f"Failed password for invalid user {username} from {ip_address} port {port} ssh2"

    log_entry = f"{timestamp} {hostname} sshd[{pid}]: {message}"
    return log_entry
