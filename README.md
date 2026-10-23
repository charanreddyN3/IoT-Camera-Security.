# AI-Based Intrusion Detection for IoT Camera Networks

## Project Overview
This project focuses on improving the security of IoT camera networks using AI-based person detection, event monitoring, and a web-based surveillance dashboard. It aims to identify relevant security events, capture evidence, and help users monitor activity through a centralized interface.

## Objectives
- Detect people using computer vision.
- Monitor camera activity and record security events.
- Store event details in a database.
- Display events and evidence through a Flask dashboard.
- Explore edge computing and blockchain for secure IoT event management.

## Technologies Used
- **Programming Language:** Python
- **Computer Vision:** OpenCV, YOLOv8
- **Backend:** Flask
- **Frontend:** HTML, CSS
- **Database:** SQLite
- **Tools:** VS Code, Git, GitHub

## Key Features
- Real-time camera stream and person detection.
- Detection evidence image capture.
- Security event storage and viewing.
- Web-based surveillance dashboard.
- Event database management.

## Project Structure
```text
IoT-Camera-Security/
├── app.py
├── camera_stream.py
├── camera_test.py
├── person_detection.py
├── check_db.py
├── clear_db.py
├── create_db.py
├── fix_paths.py
├── save_events.py
├── upgrade_db.py
├── view_events.py
├── static/
├── templates/
└── README.md
```

## Installation and Setup

### 1. Clone the repository
```bash
git clone https://github.com/charanreddyN3/IoT-Camera-Security..git
cd IoT-Camera-Security
```

### 2. Install dependencies
Install the required Python packages used by the project. For example:
```bash
pip install flask opencv-python ultralytics
```

### 3. Run the application
Run the Flask application:
```bash
python app.py
```

Open the local URL shown in your terminal in your browser. It is commonly `http://127.0.0.1:5000/`.

**Note:** Camera access, model files, database setup, and any additional dependencies must be configured for your environment.

## Future Enhancements
- Integrate edge computing for local processing.
- Explore blockchain-based integrity and verification of security events.
- Improve intrusion classification and alerting.
- Enhance authentication and dashboard security.

## Project Status
Academic project — development and testing.

## Author
Charan Reddy N
