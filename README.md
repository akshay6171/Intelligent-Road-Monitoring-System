🚦 Intelligent Road Monitoring System
AI-Based Object Detection with Conditional Geo-Location Logging
➤Project Overview:

The Intelligent Road Monitoring System is an AI-powered application designed to detect road objects such as vehicles and pedestrians in real time using a pre-trained deep learning model. The system conditionally logs geographic location data (latitude & longitude) only when valid object detections occur, ensuring efficient and meaningful data storage.

➤Project Structure
Intelligent-Road-Monitoring-System/
│
├── detect.py          # Main detection and logging script
├── gps.py             # GPS location generator
├── database.py        # Database and table creation
├── road.db            # SQLite database
├── road_video.mp4     # Sample road traffic video
├── new1.mp4           # Additional demo video
├── yolov8n.pt         # YOLOv8 model weights
├── README.md


⚙️ Setup Instructions:-
1️⃣ Clone the Repository:
git clone https://github.com/akshay6171/Intelligent-Road-Monitoring-System.git
cd Intelligent-Road-Monitoring-System

2️⃣ Install Required Libraries:
pip install ultralytics opencv-python

3️⃣ Create Database:
Run the database setup script once:
python database.py
(This will create road.db and the required table.)

🚀 How to Run the Project
▶️ Run Using Video File:
cap = cv2.VideoCapture("road_video.mp4")

▶️ Run Using Webcam:
cap = cv2.VideoCapture(0)

▶️ Start detection:
python detect.py

🛢Database Schema:

| Column      | Description                |
| ----------- | -------------------------- |
| id          | Auto-increment primary key |
| object_type | Detected object class      |
| confidence  | Detection confidence score |
| timestamp   | Detection time             |
| latitude    | Latitude value             |
| longitude   | Longitude value            |
