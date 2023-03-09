<h1 align="center">Intelligent-Door-Access-System-with-Facial-Recognition-and-Voice-Control</h1>

## TABLE OF CONTENTS:

**1. INTRODUCTION**

**2. HARDWARES USED**

**3. SOFTWARES USED**

**4. PROGRAMMING LANGUAGES**

**5. WORKFLOW**

**6. MAIN COMPONENTS:**
      
     **1: SMART DOOR WITH FACE RECOGNITION**
     **2: AlEXA WITH CUSTOM SKILLS FOR RECOGNITION AND DOOR CONTROL**
     **3: SERVO MOTOR FOR DOOR MOVEMENT**

**7. OUTPUT**

**8. CONCLUSION**

#

## **1. INTRODUCTION:**

The "Intelligent Door Access System with Facial Recognition and Voice Control" is a project that aims to create a smart door system that can automatically recognize the face of a person and allow them access to a building or a room. The system is equipped with a camera that captures the face of a person when they ring the doorbell, and a facial recognition algorithm that identifies the person based on their unique facial features.In addition, the system is integrated with Alexa, a voice-controlled virtual assistant, which enables the user to interact with the system using voice commands. Through Alexa, the user can identify the person at the door and command the door to open or close, providing an added layer of security and convenience.

The first component is a camera, which is mounted near the doorbell or the entrance. The camera captures the face of the person standing at the door when they press the doorbell.The second component is a facial recognition algorithm, which is responsible for identifying the person based on their facial features. The algorithm uses a database of faces to match the face of the person at the door with the faces in the database. If the face matches, the door can be unlocked or opened automatically, granting the person access.The third component is Alexa, the voice-controlled virtual assistant. Alexa can be integrated with the system to enable the user to interact with the system using voice commands. For example, the user can ask Alexa to identify the person at the door and receive a response based on the facial recognition algorithm's analysis.

Additionally, the user can also use Alexa to open or close the door. This feature provides an added layer of convenience and security, as the user can control the door without having to physically interact with it.Overall, the Intelligent Door Access System with Facial Recognition and Voice Control offers several benefits over traditional access control systems. It eliminates the need for keys or access cards, which can be lost or stolen, and provides a more secure means of entry. Additionally, the system is convenient and easy to use, as the user can control the door using their voice, and it can be integrated with other smart home devices for added functionality.

#

## **2. HARDWARES USED:**

- [RASPBERRY PI 4 MODEL B](https://www.hackster.io/raspberry-pi/products/raspberry-pi-4-model-b)
- [W5100S-EVB-PICO](https://www.hackster.io/wiznet/products/w5100s-evb-pico1)
- [JUMPER WIRES](https://www.hackster.io/diyables/products/jumper-wires)
- [AMAZON ECHO-DOT](https://www.hackster.io/amazon-alexa/products/echo-dot)
- [LED DOT-MATRIX](https://www.hackster.io/diyables/products/led-matrix-4-in-1-32x8)
- [ARDUCAM MINI 2MP PLUS](https://www.arducam.com/product/arducam-2mp-spi-camera-b0067-arduino/)
- [TRIPOD STAND](https://www.amazon.in/AmazonBasics-WT0352G-Lightweight-Mini-Tripod/dp/B00M78G2VO/ref=asc_df_B00M78G2VO/?tag=googleshopdes-21&linkCode=df0&hvadid=396988520763&hvpos=&hvnetw=g&hvrand=2538694165889750999&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007788&hvtargid=pla-309497986922&psc=1&ext_vrnc=hi)
- [PUSH BUTTON](https://www.hackster.io/diyables/products/button)
- [SERVO MOTOR](https://www.hackster.io/diyables/products/servo-motor-sg90-180-degree)
- [DOOR LOCK](https://www.the-diy-life.com/arduino-based-rfid-door-lock-make-your-own/)

#

## **3. SOFTWARE AND SERVICES USED:**

- [openCV](https://opencv.org/)
- [AURDINO IDE](https://www.arduino.cc/)
- [AMAZON ALEXA SKILLS KIT](https://developer.amazon.com/en-US/alexa)
- [FLASK-ASK](https://github.com/johnwheeler/flask-ask)
- [MQTT SERVICE](https://mqtt.org/)
- [NGROK](https://ngrok.com/)

#

## **4. PROGRAMMING LANGUAGES**
- [C++](https://isocpp.org/)
- [PYTHON](https://www.python.org/)

#

## **4. WORK FLOW:**

The workflow of this project starts with a person pushing a button that is similar to a calling bell. An ARDUCAM MINI 2MP PLUS is attached to the button, which is running on the Flask server. When the button is pushed, it will click a snap of the person at the front and goes for face recognition using OpenCV. The face_recognition() function loads pre-encoded images of known faces from a specified directory using the SimpleFacerec library. Then it reads the specified image file and performs face recognition on the image using the loaded encoding images. The result from the face recognition is being published into an HTML post as a JSON file.

The next phase is the Alexa phase. When the user is inside the house, he can ask Alexa who is at the door/who is there. Then, Alexa would reply with the name and time of the person visited to the user. If the face is not identified, it will say face not found to the user. If the user wants the person to be let in, he would command Alexa to open the door. This skill set is linked with Chat GPT, which would convert the statement from the user, and based on the sentence and polarity, the message is either mapped to open the door or close the door.The entire Alexa skill is supported by the Flask server running on a Raspberry Pi, and the ngrok functionalities are being used to ensure the visibility of the local host to the Alexa skill endpoint. The ngrok service is used to expose a local web server to the internet, which enables Alexa to communicate with the Flask server running on the Raspberry Pi.

The last part of this project is the servo motor Micro Servo Motor SG90 attached to the door lock. The return message from the Chat GPT is sent via MQTT, and a Wiznet board attached to the motor and the door lock is there to capture the message from the MQTT topic and act according to the message. When the Chat GPT receives a command to open the door, it sends a message to the Wiznet board, which then activates the servo motor to unlock the door. When the Chat GPT receives a command to close the door, it sends a message to the Wiznet board, which then activates the servo motor to lock the door.In conclusion, this project provides a complete solution for secure access control to homes or buildings. The project's workflow is well thought out and detailed, ensuring that all components work together seamlessly to provide a reliable and efficient access control system.

## **MAIN COMPONENTS:**




