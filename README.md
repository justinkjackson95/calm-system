# Calm Alley Speed Monitoring System (Radar-Based)

This is a radar-based speed detection system using an HB100 Doppler radar module and Raspberry Pi. The system captures vehicle speeds and streams the data to AWS Kinesis. AWS Lambda filters the incoming data before it's stored or visualized.

## Components

- **HB100 Radar Sensor**
- **Raspberry Pi (3/4)**
- **AWS Kinesis (for data ingestion)**
- **AWS Lambda (for data filtering)**
- **Optional: S3, QuickSight, DynamoDB**

## Key Files

- `main.py`: Main loop that reads speed and publishes it.
- `radar_module.py`: Measures speed using GPIO input.
- `aws_publisher.py`: Sends data to AWS Kinesis.
- `lambda_handler.py`: AWS Lambda function for real-time data filtering.
- `config.py`: Stores GPIO pin and AWS settings.

## Setup

1. Install required packages:
    ```
    pip install -r requirements.txt
    ```

2. Run the main script on your Raspberry Pi:
    ```
    python3 main.py
    ```

3. Deploy `lambda_handler.py` as a Lambda function connected to your Kinesis stream.

## Notes

- Conversion factor for HB100 is ~0.062 (MHz to MPH).
- Radar signal is read via GPIO pin 17 by default.
