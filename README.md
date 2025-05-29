# CALM System (v1)

**Community Alleyway Low-speed Monitoring System**

This is version 1 of the CALM System running on a Raspberry Pi. It:
- Reads vehicle speed (simulated or from radar sensor)
- Calculates average speed
- Recommends speed bump spacing based on observed data
- Accounts for the radar's fixed position in the alley
- Sends telemetry to AWS IoT Core (MQTT)

---

## 🔧 Setup

### Hardware
- Raspberry Pi with Wi-Fi
- Optional: Doppler radar sensor

### AWS Services
- IoT Core (secure MQTT broker)
- Optional downstream: Lambda → DynamoDB → QuickSight (not included here)

### File Structure
calm-system-v1/
├── calm_system.py
├── certs/
│ ├── AmazonRootCA1.pem
│ ├── cert.pem.crt
│ └── private.pem.key
