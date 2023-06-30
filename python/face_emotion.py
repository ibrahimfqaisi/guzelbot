import cv2
import numpy as np
from keras.models import load_model
from tkinter import messagebox

def emotion(cap):
    model = load_model('model_file_30epochs.h5')


    faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    labels_dict = {0: 'Angry', 1: 'Disgust', 2: 'Fear', 3: 'Happy', 4: 'Neutral', 5: 'Sad', 6: 'Surprise'}

    emotion_counts = {label: 0 for label in labels_dict.values()}  # Initialize counts for each emotion

    loop_count = 0

    while loop_count < 20:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceDetect.detectMultiScale(gray, 1.3, 3)
        
        for x, y, w, h in faces:
            sub_face_img = gray[y:y+h, x:x+w]
            resized = cv2.resize(sub_face_img, (48, 48))
            normalize = resized / 255.0
            reshaped = np.reshape(normalize, (1, 48, 48, 1))
            result = model.predict(reshaped)
            label = np.argmax(result, axis=1)[0]
            
            emotion = labels_dict[label]
            emotion_counts[emotion] += 1  # Increment the count for the detected emotion
            
            print(emotion)  # Print the detected emotion
            
            # cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 1)
            # cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 2)
            # cv2.rectangle(frame, (x, y-40), (x+w, y), (50, 50, 255), -1)
            # cv2.putText(frame, emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
            
        cv2.imshow("Frame", frame)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break
        
        loop_count += 1
    cv2.destroyAllWindows()
    global most_common_emotion
    most_common_emotion = max(emotion_counts, key=emotion_counts.get)
    print("Most Frequent Emotion:", most_common_emotion)
    file_path = 'most_emotion.txt'
    # Save the JSON data to a file
    with open(file_path, 'w+') as json_file:
        json_file.write(most_common_emotion)                                
