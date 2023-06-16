import torch
import sys
import datetime
from PIL import Image as Image1
import clip
import numpy as np
import tensorflow as tf
import cv2
print("This might take a couple of minutes since packages are being loaded")
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db

subject = sys.argv[1]
subject = str(subject)
# Initialize the app wnit    h a service account
# cred = credentials.Certificate("E:\work\erofinal-firebase-adminsdk-3m21h-b0709184ff.json")
# firebase_admin.initialize_app(cred, {
#     'databaseURL' : 'https://erofinal-default-rtdb.asia-southeast1.firebasedatabase.app/'
# })

# Function to record attendance
# def record_attendance(name, status,subject):
#     # Current date and time
#     now = datetime.datetime.now()
#     date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

#     # Data to save
#     data = {
#         'name': name,
#         'status': status,
#         'date_time': date_time,
#         'subject': subject
#     }

#     # Push data to Firebase
#     ref = db.reference('/attendance')
#     ref.push(data)

face_model = tf.keras.models.load_model('E:/vscode/face.h5', compile=False)
cap = cv2.VideoCapture(0)
face_counts = []  # Counter for each face
continuous_counter = 0
model, preprocess = clip.load('ViT-B/16')
model.eval()
input_resolution = model.visual.input_resolution
context_length = model.context_length
vocab_size = model.vocab_size

print("Model parameters:",
      f"{np.sum([int(np.prod(p.shape)) for p in model.parameters()]):,}")
print("Input resolution:", input_resolution)
print("Context length:", context_length)
print("Vocab size:", vocab_size)
CLASS_VOCAB = ['Abhishek SJ', 'Aditya VSM', 'Akash', 'Aniruddh Bhardwaj', 'Ashish',
               'Chirag', 'Hemanth', 'Khushi', 'Lekhana', 'Nihith', 'Paar', 'Rohan', 'Lekhana']


def get_clip_features_per_video(img):
    image = preprocess(img).unsqueeze(0)
    with torch.no_grad():
        # encoding image into feature vectors using the CLIP model
        image_features = model.encode_image(image)
        # print(image_features)
    return image_features


def count_repeated_from_last(arr, target_string):
    count = 0
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == target_string:
            count += 1
        else:
            break
    return count


while True:
    # Read each frame from the video stream
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(
        "E:/work/haarcascade/haarcascade_frontalface_alt.xml")
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    print('Number of detected faces:', len(faces))
    if len(faces) > 0:
        # Counter for continuous predictions
        for i, (x, y, w, h) in enumerate(faces):
            face = frame[y-40:y+h+40, x-40:x+w+40]
            color_converted = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
            pil_image = Image1.fromarray(color_converted)
            video_features = get_clip_features_per_video(
                pil_image).cpu().numpy()
            probabilities = face_model.predict([video_features])[0]
            highest_probability = np.argsort(probabilities)[::-1]
            #cv2.imwrite(f'{CLASS_VOCAB[highest_probability[0]]}.jpg', face)
            # Increment the counter for the highest probability face
            print(f"{CLASS_VOCAB[highest_probability[0]]}.jpg")
            face_name = CLASS_VOCAB[highest_probability[0]]
            # Increment the counter for the highest probability face
            face_name = CLASS_VOCAB[highest_probability[0]]
            face_counts.append(face_name)
            print(f"{face_counts}---------------")

            # Check if the name appears 10 times
            continuous_counter = count_repeated_from_last(
                face_counts, face_name)

            if continuous_counter > 2 and continuous_counter < 4:
                if probabilities[highest_probability[0]] * 100 > 60:
                    print(
                        f"{i} {face_name}: {probabilities[highest_probability[0]] * 100:5.2f}%")
                    # print(f"uploading attendance{face_name}")
                    # record_attendance(face_name, 'present',subject)
            elif continuous_counter > 4:
                face_counts = []  # Counter for each face
                continuous_counter = 0
