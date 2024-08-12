from pompa import pompa_apa_on, pompa_apa_off
import paho.mqtt.client as mqtt
from time import sleep
import json

def on_message(client, userdata, msg):
    print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")
    message = json.loads(msg.payload.decode())
    command = message.get("Pump")
    
    if command == "ON":
        print("Turning the Pump on for 3 seconds")
        pompa_apa_on()
        sleep(3)
        pompa_apa_off()
    elif command == "OFF":
        print("Turning the Pump off")
        pompa_apa_off()
    else:
        print("Invalid command! Try ON or OFF")

mqtt_ip = "mqtt.beia-telemetrie.ro"
mqtt_port = 1883
mqtt_topic = "meshlium3d4c/Gabi/TC"

client = mqtt.Client()
client.connect(mqtt_ip, mqtt_port)
client.subscribe(mqtt_topic)
client.on_message = on_message

def main():
    try:
        client.loop_start()
        
    except KeyboardInterrupt:
        print("Exiting...")
        client.loop_stop()
        client.disconnect()
        
if __name__ == "__main__":
    main()