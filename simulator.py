import yaml
import random
from generators.ssh_generator import generate_ssh_log
from generators.utils import wait_interval

def load_config(path='config.yaml'):
    with open(path, 'r') as file:
        return yaml.safe_load(file)

def simulate_ssh_logs(config):
    total = config.get('total_events', 50)
    rate = config.get('rate_per_minute', 10)
    output_file = config.get('output_file', 'logs/ssh_simulation.log')
    success_rate = config.get('success_rate', 0.7)

    with open(output_file, 'w') as f:
        for _ in range(total):
            success = random.random() < success_rate
            log = generate_ssh_log(success)
            print(log)
            f.write(log + '\n')
            wait_interval(rate)

if __name__ == '__main__':
    config = load_config()
    if config['event_type'] == 'ssh':
        simulate_ssh_logs(config)
    else:
        print("Only SSH event simulation is implemented.")
