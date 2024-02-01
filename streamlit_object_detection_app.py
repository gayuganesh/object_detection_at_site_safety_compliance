%%writefile app.py
import streamlit as st
from PIL import Image
import numpy as np
from io import BytesIO
from roboflow import Roboflow

rf = Roboflow(api_key="Ps51nXOB4N8owuxwYi4n")
project = rf.workspace().project("workers-safety-equipment-z1mra")
model = project.version(3).model

def predict_objects(uploaded_file):
    pil_image = Image.open(uploaded_file)
    np_image = np.array(pil_image)
    predicted = model.predict(np_image, confidence=40, overlap=30).json()
    objects = []
    score = 0
    for i in predicted.get('predictions'):
        objects.append(i.get('class'))
    for j in objects:
        if j in ("Helmet", "Vest", "Gloves"):
            score += 1
        else:
            continue
    if score !=3:
      out = "you can't enter"
    else:
      out = "you can enter"
    return objects, out

def main():
    st.title("Image Uploader and Object Detection")
    st.write("Upload an image and see the predicted objects below!")

    # File uploader widget
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        # Call the prediction function
        objects, score = predict_objects(uploaded_file)

        # Display the predicted objects and score
        st.subheader("Predicted Objects:")
        st.write(", ".join(objects))

        st.subheader("Score:")
        st.write(score)

if __name__ == "__main__":
    main()
