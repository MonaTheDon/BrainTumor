import streamlit as st
import tensorflow as tf
import streamlit as st
import cv2
from PIL import Image, ImageOps
import numpy as np


st.set_page_config(page_title="Brain Tumor Classification", page_icon="🧠")
@st.cache_resource(experimental_allow_widgets=True)
def load_model():
  model=tf.keras.models.load_model('keras_model.h5')
  return model
with st.spinner('Model is being loaded..'):
  model=load_model()
class_names={0: "Glioma",
1 :"Pituitary",
2 :"meningioma"}


st.title("Brain Tumor Classification 🧠")

st.subheader("Detects whether an MRI image has Pituitary, Glioma or Meningiona Tumor")

file = st.file_uploader("Please upload a brain MRI Picture", type=["jpg", "png"])

st.set_option('deprecation.showfileUploaderEncoding', False)
def import_and_predict(image_data, model):
    
        size = (224,224)    
        image = ImageOps.fit(image_data, size)
        image = np.asarray(image)
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        #img_resize = (cv2.resize(img, dsize=(75, 75),    interpolation=cv2.INTER_CUBIC))/255.
        
        img_reshape = img[np.newaxis,...]
    
        prediction = model.predict(img_reshape)
        
        return prediction
if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    predictions = import_and_predict(image, model)
    score = tf.nn.softmax(predictions[0])
    st.write(predictions)
    st.write(score)
    st.write(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score))
)
