import yaml
import random
from generators.ssh_generator import generate_ssh_log
from generators.utils import wait_interval
import threading

stop_event = threading.Event()

def load_config(path='config.yaml'):
    with open(path, 'r') as file:
        return yaml.safe_load(file)
    
def load_config(path='config.yaml'):
    try:
        with open(path, 'r') as file:
            config = yaml.safe_load(file)
            print("Loaded Config:", config)
            return config
    except Exception as e:
        print(f"Failed to load config: {e}")
        return None

def simulate_ssh_logs(config, stop_event):
    total = config.get('total_events', 50)
    rate = config.get('rate_per_minute', 10)
    output_file = config.get('output_file', 'logs/ssh_simulation.log')
    success_rate = config.get('success_rate', 0.7)

    print("[Simulator] Starting Simulation...")
    with open(output_file, 'w') as f:
        for _ in range(total):
            if stop_event.is_set():
                print("[Simulator] Simulation stopped.")
                break

            success = random.random() < success_rate
            log = generate_ssh_log(success)
            print(log)
            f.write(log + '\n')
            wait_interval(rate)


def stop_simulation():
    stop_event.set()
    print("Simulation stopped.")

def reset_simulation():
    global stop_event
    stop_event = threading.Event()
    print("Simulation reset.")

if __name__ == '__main__':
    config = load_config()
    if config['event_type'] == 'ssh':
        simulate_ssh_logs(config)
    else:
        print("Only SSH event simulation is implemented.")
