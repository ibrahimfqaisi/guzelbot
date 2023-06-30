import cv2
import numpy as np

def add_face_to_dataset(dataset_file, names_dict):
    try:
        dataset = np.load(dataset_file, allow_pickle=True).item()
    except FileNotFoundError:
        dataset = {}
    
    for name, face_images in names_dict.items():
        if name not in dataset:
            dataset[name] = []
        dataset[name].extend(face_images)
    
    np.save(dataset_file, dataset)

def preprocess_faces(face_images):
    processed_faces = []
    for face_image in face_images:
        processed_face = cv2.equalizeHist(face_image)
        processed_face = processed_face / 255.0
        processed_faces.append(processed_face)
    return processed_faces

def capture_faces(dataset_file):
    faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    video = cv2.VideoCapture(0)
    num_faces_to_capture = 5
    captured_faces = []
    name = input("Enter the name for the faces: ")

    while len(captured_faces) < num_faces_to_capture:
        ret, frame = video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceDetect.detectMultiScale(gray, 1.3, 3)

        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

            face_image = gray[y:y+h, x:x+w]
            resized_face = cv2.resize(face_image, (100, 100))
            processed_face = preprocess_faces([resized_face])

            cv2.imshow("Captured Face", processed_face[0])

            captured_faces.append(processed_face[0])

            if len(captured_faces) >= num_faces_to_capture:
                break

        cv2.imshow("Video", frame)
        cv2.waitKey(1)

    video.release()
    cv2.destroyAllWindows()

    captured_dict = {name: captured_faces}
    add_face_to_dataset(dataset_file, captured_dict)

dataset_file = 'dataset.npy'
capture_faces(dataset_file)
