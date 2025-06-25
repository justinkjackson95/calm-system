from radar_module import measure_speed
from aws_publisher import publish_data
import time

def main():
    while True:
        speed = measure_speed(sample_time=1.0)
        print(f"Measured Speed: {speed} mph")

        if speed > 0:
            data = {
                "speed": speed,
                "timestamp": time.time()
            }
            publish_data(data)

        time.sleep(1)

if __name__ == "__main__":
    main()
