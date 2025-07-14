# SIEM Log Simulator with Web GUI

A Python-based SIEM log simulator that generates synthetic SSH logs, wrapped in a Flask web application with a modern, styled GUI for controlling the simulation.

---

## 🚀 Features

- **Simulate SSH Logs:** Generates successful and failed SSH login attempts in syslog format.
- **Configurable via YAML:** Easily adjust the number of events, rate per minute, success rate, and output file.
- **Web-based Control:** Start and stop the simulation from a web interface.
- **Download Logs:** Download generated logs directly from the interface.
- **Stylish UI:** Clean, glowing, and modern styled buttons with status indications.

---

## 🛠️ Technologies Used

- **Python 3**
- **Flask**
- **Threading**
- **HTML + CSS (Custom styling with Google Fonts)**

---

## 📁 Project Structure

siem-log-simulator/
- │
- ├── simulator.py # Simulation core logic
- ├── app.py # Flask application (Web UI)
- ├── config.yaml # Simulation configuration
- ├── logs/ # Output directory for generated logs
- │
- ├── templates/
- │ └── index.html # Web GUI frontend
- │
- ├── static/
- │ └── style.css # CSS for GUI styling
- │
- ├── generators/
- │ ├── ssh_generator.py # SSH log generator
- │ └── utils.py # Utility functions (wait interval)
- │
- └── README.md # Project documentation

## ⚙️ Setup Instructions

1. **Clone the Repository**
```bash
git clone https://github.com/<your-username>/siem-log-simulator.git
cd siem-log-simulator

2. **Install Dependencies**
```bash
pip install Flask PyYAML

3. **Run the Flask Web App**
```bash
python app.py

4. **Access the Web Interface**
```bash
http://127.0.0.1:5000

---

⚡ Web Interface Features
Start Simulation: Begin log generation in the background.

Stop Simulation: Gracefully stop the simulation.

Download Logs: Get the generated SSH logs as a .log file.

Stylized UI: Bold fonts, glowing buttons, and modern interface.

---

## **Developed by `Saad Bin Arif Muhammad`**

Let me know if you want me to add:
- Contribution guidelines
- Screenshots of the interface
- Badges for GitHub (stars, forks, issues)

I can generate that too!
