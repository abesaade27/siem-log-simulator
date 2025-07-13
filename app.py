from flask import Flask, render_template, request, redirect, url_for, send_file
from simulator import simulate_ssh_logs, load_config
import threading

app = Flask(__name__)

simulation_thread = None
stop_event = threading.Event()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_simulation():
    global simulation_thread, stop_event
    config = load_config()

    # Reset event before starting new simulation
    stop_event.clear()
    simulation_thread = threading.Thread(target=simulate_ssh_logs, args=(config, stop_event))
    simulation_thread.start()
    return redirect(url_for('index'))

@app.route('/stop', methods=['POST'])
def stop():
    global stop_event
    stop_event.set()
    return redirect(url_for('index'))

@app.route('/download')
def download_logs():
    return send_file('logs/ssh_simulation.log', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
