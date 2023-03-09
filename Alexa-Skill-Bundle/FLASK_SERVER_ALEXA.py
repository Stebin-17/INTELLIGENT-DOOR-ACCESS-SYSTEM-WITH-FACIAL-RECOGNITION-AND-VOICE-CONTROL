import telegram
from telegram.ext import Updater,MessageHandler
import logging
import os
import paho.mqtt.client as mqtt
from flask import Flask
from flask_ask import Ask, request, session, question, statement
import RPi.GPIO as GPIO
import os
import openai
import json
import urllib.request
import requests
import urllib
from urllib.request import urlopen
from datetime import datetime


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

STATUSON = ['on','high']

STATUSOFF = ['off','low']


@ask.intent("facerecognition")
def facerecognition():
    url = 'http://192.168.0.107:1066/static/img/file.json'
    response = urllib.request.urlopen(url)
    text = response.read().decode('utf-8')
    res=json.loads(text)
    print(res.keys())
    text1=res['face_name']
    text2=res['time']
    timestamp = res['time']

    # Convert the timestamp to datetime object
    dt_object = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')

    # Combine year-month-day and time in hours and minute with am/pm into a single variable
    text3 = dt_object.strftime('%Y-%m-%d %I:%M %p')
    return statement("{} is at the door,time is {}".format(text1,text3))



@ask.intent("dooropen",mapping={'user_question1':'permission'})
def dooropen(user_question1,room):
    first_client = mqtt.Client()
    first_client.connect('54.87.92.106',1883)
    openai.api_key = "sk-*****************************************As0A"
    chat = user_question1
    print(chat)
    if "let him in" in chat.lower() or "he is a good guy" in chat.lower() or "he is my friend" in chat.lower() or "i know him" in chat.lower():
        first_client.publish("home/door","OPEN THE DOOR")
        return statement("Opening the doors")
       
    elif "he is harmfull" in chat.lower() or "he is bad" in chat.lower() or "he is my enemy" in chat.lower():
        first_client.publish("home/door","CLOSE THE DOOR")
        return statement("closing the door")
        
    
    else:
        response = openai.Completion.create(
          model="text-davinci-003",
          prompt="Convert \"" + chat + "\" to any one among below commands :\n- Unlock the door\n- Lock the door \n",
          temperature=0,
          max_tokens=100,
          top_p=1,
          frequency_penalty=0.2,
          presence_penalty=0)
        chat2="Convert \"" + chat + "\" to any one among below commands :\n- Unlock the door\n- Lock the door \n"
        print(chat2)
        print(response)
        text=response['choices'][0]['text']
        print("the response from chatgpt is {}".format(text))
        
        if "Unlock the door" in text or "Open" in text:
            first_client.publish("home/door","OPEN THE DOOR")
            return statement("Opening the doors")
            
        elif "Lock the door" in text or "Close" in text or "Shut" in text or "don't know" in text:
            first_client.publish("home/door","CLOSE THE DOOR")
            return statement("closing the door")
        else:
            return statement("chatGpt returned {}".format(text))


@ask.intent("AMAZON.NoIntent")
def stop_chatgpt():
    return statement("Exiting the ChatGPT Skill")

@ask.launch
def launch():
    speech_text = 'Welcome'
    return question(speech_text).reprompt(speech_text).simple_card(speech_text)

@ask.intent('GpioIntent', mapping = {'status':'status'})
def Gpio_Intent(status,room):
    first_client = mqtt.Client()
    first_client.connect('54.87.92.106',1883)
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)    
    GPIO.setup(17,GPIO.OUT)
    if status in STATUSON:
        GPIO.output(17,GPIO.HIGH)
        first_client.publish("home/alexa","TURN ON LIGHTS")
        return statement('turning {} lights'.format(status))
    elif status in STATUSOFF:
        GPIO.output(17,GPIO.LOW)
        first_client.publish("home/alexa","TURN OFF LIGHTS")
        return statement('turning {} lights'.format(status))
    else:
        return statement('Sorry not possible.')
 
@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = 'You can say hello to me!'
    return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)


@ask.intent('AMAZON.StopIntent')
def stop():
    return statement ("Exiting the skill")

@ask.session_ended
def session_ended():
    return "{}", 200



if __name__ == '__main__':
    
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
    
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)










