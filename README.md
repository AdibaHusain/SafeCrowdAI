# SafeCrowdAI
About
SafeCrowdAI is an advanced AI-driven crowd management solution designed to prevent disasters in public gatherings through real-time people counting, emotion monitoring, and automated early warnings. By combining computer vision, audio analysis, and IoT integration, SafeCrowdAI empowers venue managers, authorities, and event organizers to detect and respond to hazardous situations—before they become critical.

# Main Features:
🎥 Real-Time People Counting: Uses CCTV feeds and intelligent computer vision to monitor crowd density and movements.

🔊 Audio Emotion Analysis: Integrates Whisper API and emotion detection to sense panic, agitation, or conflict from crowd sounds.

⏰ 10-Minute Early Warnings: Predicts high-risk situations and sends alerts at least 10 minutes ahead, improving response times.

🏃‍♂️ Automated Risk Alerts: Notifies authorities/staff in case of abnormal crowd surges, aggression, or rising distress levels.

📊 Dashboard Visualization: Provides actionable insights, crowd heatmaps, and incident logs in an intuitive interface.

🛠️ Modular & Scalable: Easily adapts to stadiums, festivals, rallies, metro stations, and more.

# System Architecture
CCTV Module: Real-time image processing, crowd counting, anomaly detection.

Microphone Audio Stream: Whisper API, emotion classifier, stress/panic scoring.

Decision Engine: Risk evaluation, trigger warnings, visualization.

Notification Layer: SMS, app push, dashboard alerts to authorities.

# How It Works
Connect CCTV & Microphones ➔ 2. Run SafeCrowdAI pipeline ➔ 3. Receive live analytics & alerts

# Technologies Used
Python, OpenCV, PyTorch, Whisper API

React/Dashboard front-end

WebSocket/REST APIs for data flow

Optional: Kafka/RabbitMQ for real-time streaming
