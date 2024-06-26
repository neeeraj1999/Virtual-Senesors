import network
import time
import urandom
from umqtt.simple import MQTTClient

# Configuration constants
MQTT_CLIENT_ID = 'AjkeGBwdIhc9Hw83DCY4EBQ'
MQTT_USER = 'AjkeGBwdIhc9Hw83DCY4EBQ'
MQTT_PWD = 'zXo7U1+l7iE7WUJCLXAE1sdT'
MQTT_SERVER = 'mqtt3.thingspeak.com'
MQTT_PORT = 1883
CHANNEL_ID = '2488599'
WIFI_NET = 'Wokwi-GUEST'
WIFI_PASS = ""

# MQTT topics for each field
MQTT_TOPIC_TEMPERATURE = f"channels/{CHANNEL_ID}/publish/fields/field1"
MQTT_TOPIC_HUMIDITY = f"channels/{CHANNEL_ID}/publish/fields/field2"
MQTT_TOPIC_CO2 = f"channels/{CHANNEL_ID}/publish/fields/field3"

# Initialize the MQTT client
mq_client = MQTTClient(MQTT_CLIENT_ID, MQTT_SERVER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PWD)

# Connect to WiFi
def connect_wifi(ssid, password):
    wifi_sta = network.WLAN(network.STA_IF)
    wifi_sta.active(True)
    wifi_sta.connect(ssid, password)

    # Wait for connection
    while not wifi_sta.isconnected():
        time.sleep(0.5)
    print("Connected to WiFi")

# Generate random sensor data
def get_sensor_data():
    temp = urandom.uniform(-50, 50)
    humid = urandom.uniform(0, 100)
    co2 = urandom.uniform(300, 2000)
    return temp, humid, co2

# Publish sensor data to ThingSpeak
def publish_sensor_data(mq_client, temp, humid, co2):
    mq_client.connect()
    mq_client.publish(MQTT_TOPIC_TEMPERATURE, str(temp))
    mq_client.publish(MQTT_TOPIC_HUMIDITY, str(humid))
    mq_client.publish(MQTT_TOPIC_CO2, str(co2))
    mq_client.disconnect()

# Main execution function
def run():
    connect_wifi(WIFI_NET, WIFI_PASS)

    while True:
        temp, humid, co2 = get_sensor_data()
        publish_sensor_data(mq_client, temp, humid, co2)
        print(f'Data Sent: Temp={temp:.1f}C, Humidity={humid:.1f}%, CO2={co2:.1f}ppm')
        time.sleep(20)  # Publish every 20 seconds to comply with ThingSpeak's rate limit

if __name__ == '__main__':
    run()