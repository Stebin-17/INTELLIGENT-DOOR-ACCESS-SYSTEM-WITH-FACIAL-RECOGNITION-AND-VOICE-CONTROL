# Servo-Motor-Using pico and MQTT 
# Contents:
## Introduction
### MQTT 
MQTT is the most commonly used messaging protocol for the Internet of Things (IoT). MQTT stands for MQ Telemetry Transport. The protocol is a set of rules that defines how IoT devices can publish and subscribe to data over the Internet. MQTT is used for messaging and data exchange between IoT and industrial IoT (IIoT) devices, such as embedded devices, sensors, industrial PLCs, etc. The protocol is event driven and connects devices using the publish /subscribe (Pub/Sub) pattern. The sender (Publisher) and the receiver (Subscriber) communicate via Topics and are decoupled from each other. The connection between them is handled by the MQTT broker. The MQTT broker filters all incoming messages and distributes them correctly to the Subscribers.

### Micro Servo Motor
Micro Servo Motor SG90 is a tiny and lightweight server motor with high output power. Servo can rotate approximately 180 degrees (90 in each direction), and works just like the standard kinds but smaller. You can use any servo code, hardware or library to control these servos. Good for beginners who want to make stuff move without building a motor controller with feedback & gear box, especially since it will fit in small places. It comes with a 3 horns (arms) and hardware.

### W5100S-EVB-Pico
W5100S-EVB-Pico is a microcontroller evaluation board based on the Raspberry Pi RP2040 and fully hardwired TCP/IP controller W5100S – and basically works the same as Raspberry Pi Pico board but with additional Ethernet via W5100S.


## Components Required (Hardware)
### 1) W5100S-EVB-Pico
![image](https://user-images.githubusercontent.com/111410933/221851568-1dfdd9f7-a120-4a78-ab7e-92e8145ba1cb.png)

W5500-EVB-Pico is a microcontroller evaluation board based on the Raspberry Pi RP2040 and fully hardwired TCP/IP controller W5500 – and basically works the same as Raspberry Pi Pico board but with additional Ethernet via W5500.

Link - https://www.wiznet.io/product-item/w5100s-evb-pico/

### 2) Micro / Servo motor
![image](https://user-images.githubusercontent.com/111410933/221851773-00299ac2-cdeb-4794-a7f2-239a3a4b7f87.png)

Servomotor is a rotary actuator or linear actuator that allows for precise control of angular or linear position, velocity and acceleration. It consists of a suitable motor coupled to a sensor for position feedback.

Link - https://www.electronicscomp.com/towerpro-sg90-9gm-micro-servo-motor?gclid=Cj0KCQiA6fafBhC1ARIsAIJjL8nZRtyF7YeaT5uO7s0qk9FI9KMbXIBMKWj7_ll-bMF4txElqaWqOgYaAqfREALw_wcB

### 3) External Power(USB cable )
![image](https://user-images.githubusercontent.com/111410933/222065255-a61d4f6e-5df0-4a2e-be79-d4fd98c6239a.png)

For extra power you can use the USB cable.

Link - https://roboticsdna.in/product/usb-to-3-5mm-x-1-35mm-5v-dc-power-cable-1mtr/?src=google&kwd=&adgroup={adgroup}&device=c&campaign={campaign}&adgroup={adgroup}&keyword=&matchtype=&gclid=Cj0KCQiA6fafBhC1ARIsAIJjL8lAuVm-zxVtA3ScGqfVGwwsKvICMqizXX1yM3Iji2708N7PKRv7HegaAkcjEALw_wcB

### 3) Jumper Wires
![image](https://user-images.githubusercontent.com/111410933/221851888-dcf54f80-c817-4390-af81-fe1721f7459f.png)
A jumper wire is an electric wire that connects remote electric circuits used for printed circuit boards. By attaching a jumper wire on the circuit, it can be short-circuited and short-cut (jump) to the electric circuit.

Link - https://robu.in/product/20cm-dupont-wire-color-jumper-cable-2-54mm-1p-1p-female-female-40pcs/?gclid=Cj0KCQiA6fafBhC1ARIsAIJjL8l8BOKENvfk_mQtsBnBd2z6vnY6-ZWEvvBiyZfEeeVca0mG0jsC7ccaAtCUEALw_wcB

## Software 
### 1) Arduino IDE 
The Arduino Integrated Development Environment - or Arduino Software (IDE) - contains a text editor for writing code, a message area, a text console, a toolbar with buttons for common functions and a series of menus. It connects to the Arduino hardware to upload programs and communicate with them.

Link - https://docs.arduino.cc/software/ide-v1/tutorials/Windows

### 2) MQTT LENS 
MQTT Lens is an add-on for the chrome browser that lets you publish messages to an MQTT broker, subscribe to MQTT topics, and receive messages using the chrome web browser.

Link - http://www.steves-internet-guide.com/using-mqtt-lens/#:~:text=MQTT%20Lens%20is%20an%20add,should%20see%20a%20blank%20screen.


## Steps 

To control a servo motor with an MQTT server using the Wiznet 5100 Ethernet module, you will need to write a program that subscribes to an MQTT topic and listens for incoming messages that contain servo motor control commands.

1)  Include the Servo library in your code and create a Servo object.

```
#include <Servo.h>

Servo myservo;  // create servo object
```
In the MQTT message callback function, parse the incoming message and use it to control the servo motor. For example, you could define a message format that specifies the servo angle in degrees, such as "servo/angle/set". When a message is received on this topic, you can extract the angle value from the payload and set the servo motor to that angle.

```
void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  char incomingMessage[length + 1];
  for (int i = 0; i < length; i++) {
    incomingMessage[i] = (char)payload[i];
  }
  incomingMessage[length] = '\0';

  Serial.println(incomingMessage);

if(incomingMessage == "OPEN THE DOOR"){
  myservo.write(0); // Rotate the servo to 0 degrees
  delay(1000); // Wait for 1 second
}
if(incomingMessage == "CLOSE THE DOOR")
  myservo.write(180); // Rotate the servo to 0 degrees
  delay(1000); // Wait for 1 second
}
```
3) In the setup() function, attach the servo object to the appropriate GPIO pin.

```
void setup()
{
  myservo.attach(9);
  Ethernet.init(17);  // WIZnet W5100S-EVB-Pico W5500-EVB-Pico W6100-EVB-Pico
  
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  
```
4) The servo motor may require additional power beyond what the Wiznet 5100 Ethernet module can provide, so be sure to power the servo motor separately if necessary. Also, make sure to test your program thoroughly to ensure that it responds correctly to incoming MQTT messages and controls the servo motor as expected.


# Circuit Diagram

![image](https://user-images.githubusercontent.com/111410933/221853283-9815608e-8aa9-4570-99ed-f0f328c79bd7.png)


To connect the servo motor to the Wiznet W5100, you will need to connect the wire (usually orange or yellow) of the servo motor to one of the PWM pins on the W5100. You will also need to connect the ground wire (usually brown or black) of the servo motor to the ground pin on the W5100.

You can then use a suitable library or code to control the servo motor using the PWM pin. The exact code or library you use will depend on your specific microcontroller or development board, as well as the programming language you are using.

![Circuit](https://user-images.githubusercontent.com/111410933/222051566-3e3c9944-20db-4100-910e-691fab4441ca.jpg)

# Conclusion 
Connecting an MQTT server with the Wiznet 5100 to control servo motors is a viable and effective solution for remote control of servo motors. The Wiznet 5100 allows for easy integration of Ethernet connectivity to devices, while MQTT provides a lightweight and efficient messaging protocol for communication between devices.

By using an MQTT client library, the Wiznet 5100 can easily subscribe to topics and receive commands from an MQTT broker. These commands can be used to control the servo motors connected to the Wiznet 5100, allowing for remote control of the motors from anywhere in the world.

Overall, connecting an MQTT server with the Wiznet 5100 to control servo motors is a great solution for anyone looking to remotely control devices. It is simple to set up, reliable, and provides an efficient way to communicate with devices over a network.

# References 

- https://www.hivemq.com/mqtt-essentials/
- https://howtomechatronics.com/how-it-works/how-servo-motors-work-how-to-control-servos-using-arduino/
- https://www.youtube.com/watch?v=NqchLYWHCzA&t=452s
- https://www.instructables.com/A-Simple-MQTT-PubSub-Node-With-Arduino-UNO-and-W51/



