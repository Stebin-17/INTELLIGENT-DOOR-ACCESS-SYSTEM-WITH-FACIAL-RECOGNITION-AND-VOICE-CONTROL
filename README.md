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

**SMART DOOR WITH FACE RECOGNITION**

The section aims to kickoff the workflow of the project by using the ARDUCAM MINI 2MP PLUS camera to capture the image of a person when the doorbell button is pressed. A dedicated Flask server runs continuously and receives the image from the camera, which is then processed using the OpenCV deep face library to identify the person's face. The identified face is cross-checked with a database, and if found, the server writes a JSON file with the time, picture, and identified name to an HTML file. If the face is not in the database, the server sends a "stranger" message to the HTML file. This project can be a useful tool for enhancing home security by identifying the people at the door and alerting homeowners of any unauthorized visitors.

**WORKFLOW OF THIS PART:**

<p align="center">
  <img src="https://user-images.githubusercontent.com/114398468/223940861-8fda8665-0d02-4add-89cf-510272e7998d.png" />
</p>

- The ARDUCAM MINI 2MP PLUS camera is connected to the Raspberry Pi, and the Flask server is started on the Pi.
- When the doorbell button is pressed, the camera captures an image of the person at the door.
- The captured image is sent to the Flask server.
- The Flask server receives the image and uses the OpenCV deep face library to identify the person's face.
- The identified face is cross-checked with a database of known faces to determine if the person is a known visitor or a stranger.
- If the identified face is a known visitor, the server writes a JSON file with the time, picture, and identified name to an HTML file.
- If the identified face is not in the database, the server sends a "stranger" message to the HTML file.

**ArduCam Mini 2MP Plus - SPI Camera Module - Pin Definition**

<img style="width:50rem" src="https://github.com/Stebin-17/Intelligent-Door-Access-System-with-Facial-Recognition-and-Voice-Control/blob/main/Door-Facial-System/Files/AruduCam-Mini-2MP-Plus-SPI-Camera-Module-Pin.jpg" alt="AruduCam-Mini-2MP-Plus-SPI-Camera-Module">


ArduCam OV2640 Module requires CS, MOSI, MISO, SCLK pins for SPI connection, and SDA, SCL pins for I2C connection. This project modified the source code of ArduCam to use SPI1.

**Pico pin configuration for ArduCam OV2640**

1. CS --> GPIO 13
2. MOSI --> GPIO 11
3. MISO --> GPIO 12
4. SCLK --> GPIO 10
5. SDA --> GPIO 8
6. SCL --> GPIO 9

<h2>Getting Started</h2>

<ol>
	<li>Clone this repository.</li>
	<li>Modify the names list in ```app.py``` with the names of the people you want to recognize.</li>
	<li>Start the Flask server using python ```main.py```</li>
	<li>Open your web browser and navigate to http://localhost:1066.</li>
	<li>Upload an image of a person in front of the door to trigger face recognition.</li>
</ol>

<h2>Code Explaination</h2>

> main.py

This code is a Python script for a Flask server that implements a facial recognition system for enhancing home security. It receives an image captured by an ARDUCAM MINI 2MP PLUS camera module and processes it using the OpenCV deep face library to identify the person's face. The identified face is then cross-checked with a database, and if found, the server writes a JSON file with the time, picture, and identified name to an HTML file. If the face is not in the database, the server sends a "stranger" message to the HTML file.

Here's a brief explanation of the code:

- Importing the required modules: The code starts by importing the necessary modules such as os, time, Flask, request, redirect, flash, url_for, render_template, FlaskForm, FileField, UploadSet, json, and datetime.

- Initializing the Flask app: The app object is created and initialized.

- Defining the route for uploading an image: The upload route is defined using the @app.route decorator. The route accepts POST requests containing an image file and saves it in the 'static/img' directory.

- Configuring the image upload settings: The Flask-Uploads module is used to configure the image upload settings. The 'photos' UploadSet is defined to store the image files.

- Initializing global variables: 'count' and 'flag' are initialized as global variables. 'count' is used to generate the filename for the captured image, and 'flag' is used to indicate if a new image has been captured.

- Defining the 'get_files' function: This function yields all the files in a given directory.

- Initializing variables for face recognition: 'image_path' is initialized with the path to the directory containing the captured image. 'data' is a dictionary that stores the JSON data to be written to the HTML file.

- Defining the 'face_recognition' function: This function takes a path to an image and performs face recognition using the DeepFace library. It returns the name of the recognized face.

- Defining the 'func' function: This function runs in a separate thread and checks if a new image has been captured. If a new image has been captured, it performs face recognition and writes the JSON data to the HTML file.

- Starting the 'func' thread: The 'func' thread is started using the threading module.

- Starting the Flask app: The app is run on the host '0.0.0.0' and port '1066'.








