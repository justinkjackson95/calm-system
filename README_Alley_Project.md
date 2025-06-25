# 🛣️ Residential Alley Speed Monitoring System

A custom Python-based IoT system designed to monitor vehicle speeds in residential alleys using a radar sensor and send telemetry data to the cloud for real-time analysis and visualization. Built with affordability and privacy in mind, this project offers a scalable solution for neighborhood traffic enforcement, urban planning, or citizen science initiatives.

---

## 🎯 Purpose

The goal of this project is to detect and log vehicle speeds in a residential alleyway using a low-cost, non-invasive radar sensor. Collected data is sent to AWS (Kinesis → S3) for centralized storage, and can be used to:
- Identify speeding trends
- Visualize traffic flow
- Inform speed bump or enforcement decisions
- Create a data-driven case for municipal support

---

## 🧰 Tech Stack

| Component            | Description                                                  |
|----------------------|--------------------------------------------------------------|
| **Python 3**         | Primary language for sensor logic and cloud integration      |
| **Radar Sensor**     | Replaced earlier camera-based detection (privacy-respecting) |
| **AWS Kinesis**      | Real-time data ingestion stream                              |
| **AWS S3**           | Persistent cloud storage for telemetry logs                  |
| **AWS SageMaker**    | (Planned) Model training for anomaly detection               |
| **AWS QuickSight**   | (Planned) Data visualization dashboards                      |

---

## 🏗️ System Architecture

```
[ Radar Sensor ]
      ↓
[ Python Edge Script ]
      ↓
[ AWS Kinesis Data Stream ]
      ↓
[ AWS S3 Bucket ]
      ↓
[ (Optional) SageMaker Model ]
      ↓
[ (Optional) QuickSight Dashboard ]
```

---

## 📦 Project Structure

```
alley-monitor/
├── radar_interface.py       # Captures and parses radar output
├── kinesis_sender.py        # Sends data to AWS Kinesis
├── config.py                # Stores API keys, region, and stream info
├── utils.py                 # Timestamping, error logging, and formatting
├── s3_backup.py             # (Optional) Pushes local logs to S3
└── main.py                  # Orchestrates the full system loop
```

---

## 🚀 How to Run Locally

### 1. Install Dependencies

```bash
pip install boto3
```

You may also need sensor-specific drivers depending on your radar hardware.

### 2. Configure AWS Credentials

Set AWS credentials via `~/.aws/credentials` or directly in `config.py`:

```python
AWS_REGION = 'us-east-1'
KINESIS_STREAM_NAME = 'alley-speed-stream'
```

### 3. Run the System

```bash
python main.py
```

The script will begin reading radar input and streaming results to AWS Kinesis.

---

## 📊 Sample Data Format

```json
{
  "timestamp": "2025-06-25T14:05:17Z",
  "speed_mph": 18.6,
  "direction": "approaching",
  "device_id": "ALLEY001"
}
```

---

## 🔒 Privacy Considerations

- ✅ Uses radar instead of video to avoid capturing personal images
- ✅ Data contains only speed, direction, timestamp, and device ID
- ✅ Suitable for privacy-compliant public or residential deployments

---

## 🧠 Design Rationale

| Decision                 | Rationale                                                    |
|--------------------------|--------------------------------------------------------------|
| **Radar over camera**    | Avoids privacy concerns and is more accurate for speed       |
| **Edge device processing**| Minimizes bandwidth and enables local storage fallback       |
| **AWS Kinesis**          | Enables scalable, real-time streaming ingestion              |
| **S3 + JSON**            | Simple, portable storage for further analysis or ML          |

---

## 🔭 Future Enhancements

| Feature                   | Description                                                 |
|---------------------------|-------------------------------------------------------------|
| 📊 QuickSight Dashboard   | Visualize peak hours, average speeds, violation frequency   |
| 🧠 ML-based Anomaly Detection | Flag unusually fast vehicles or faulty readings using SageMaker |
| 🔋 Solar/Battery Power    | Enable fully wireless outdoor deployments                   |
| 📡 Wi-Fi/LTE Gateway      | Eliminate need for wired internet                           |
| 🌐 Local Web UI           | Browse local logs and stats from a browser interface        |

---

## 🧪 Example Use Case

> A homeowner installs this system facing the alley behind their property. Over the course of a week, the system logs dozens of vehicles and shows that 25% exceed 15 mph. This data is used to justify a traffic calming request to the city.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🤝 Contributions Welcome

Have an idea for a dashboard, new radar sensor integration, or alerting system?  
Open an issue or submit a pull request. Community-driven improvements are welcome!
