import sys
import paho.mqtt.client as mqtt
server = "3.234.227.54" 

client = mqtt.Client()
client.connect(server, 1883, 60)

if len(sys.argv) <= 1:
    print("Usage : "+sys.argv[0]+" on/off")
    exit()
else:
    client.publish("id/wook/switch/evt", str(sys.argv[1]))