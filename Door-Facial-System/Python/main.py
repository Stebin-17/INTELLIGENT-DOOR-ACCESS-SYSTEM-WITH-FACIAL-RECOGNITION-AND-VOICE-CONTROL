import os
import time
from flask import Flask, request, redirect, flash, url_for, render_template
from flask_wtf import FlaskForm
from wtforms import FileField
from flask_uploads import configure_uploads, IMAGES, UploadSet
import json
# using datetime module
import datetime;
# libraries for face recognition
import threading
from deepface import DeepFace
import time
import re

app = Flask(__name__)

photos = UploadSet("photos", IMAGES)
app.config["UPLOADED_PHOTOS_DEST"] = "static/img"
app.config["SECRET_KEY"] = os.urandom(24)
configure_uploads(app, photos)
count = 1


def get_files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file


image_path = "/home/christ-infotech-007/Rohan/smart_door_alexa/FlaskServer/images/"
data = {"image_id": "capture01", "message": "", "face_name": "", "time": "", "image_link": ""}

flag = False


def face_recognition(path):
    for file in get_files(path):
        result = DeepFace.verify(
            img1_path=path + file,
            img2_path="/home/christ-infotech-007/Rohan/smart_door_alexa/FlaskServer/static/img/capture01.jpeg",
            model_name="SFace")
        if result['verified'] == True:
            return file


def func():
    global flag
    # initializing substrings
    sub = ".jpeg"
    extract = str(re.escape(sub))
    while True:
        time.sleep(0.1)
        if flag == True:
            message = "Someone is at the door"
            link = "http://192.168.0.107:1077/static/img/capture01.jpeg"
            try:
                face_name = face_recognition(image_path)
                face_name = re.findall("(.*)" + extract, face_name)[0]
                print(face_name)
                print(str(datetime.datetime.now()))
                data["time"] = str(datetime.datetime.now())
                data["face_name"] = face_name
                data["message"] = message
                data["image_link"] = link
                with open(
                        '/home/christ-infotech-007/Rohan/smart_door_alexa/FlaskServer/static/img/file.json',
                        'w') as outfile:
                    json.dump(data, outfile)
                print("Face has been successfully recognized")
            except Exception as e:
                print("Error occured",e)
                data["face_name"] = "Familiar face not found"
                data["message"] = message
                data["image_link"] = link
                with open('/home/christ-infotech-007/Rohan/smart_door_alexa/FlaskServer/static/img/file.json',
                          'w') as outfile:
                    json.dump(data, outfile)
                flag = False
            flag = False


@app.route("/", methods=['GET', 'POST'])
def upload():
    global count
    global flag
    if request.method == 'POST' and 'image/jpeg' == request.content_type:
        filepath = "/home/christ-infotech-007/Rohan/smart_door_alexa/FlaskServer/static/img/capture%02d.jpeg" % count
        f = open(filepath, "wb")
        # count = count + 1
        f.write(bytes(request.data))
        f.close()
        flag = True
        return f'{filepath}'

    return render_template('upload.html')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    process = threading.Thread(target=func, args=())
    process.start()
    # main()
    app.run(host='0.0.0.0', port=1066)
