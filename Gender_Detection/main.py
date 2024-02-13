import face_recognition

# Load an image with faces
image_path = "Gender_Detection/image.jpg"
image = face_recognition.load_image_file(image_path)

# Find face locations
face_locations = face_recognition.face_locations(image)

# Load the gender model
face_gender_model = face_recognition.load_gender_predictor()

# Predict gender for each face
for face_location in face_locations:
    top, right, bottom, left = face_location
    face_image = image[top:bottom, left:right]

    # Predict gender
    gender_predictions = face_gender_model.predict([face_image])
    gender = gender_predictions[0]
    
    print(f"Gender: {gender} for face at location {face_location}")
