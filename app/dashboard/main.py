import os
import cv2
import streamlit as st

c_cascade = cv2.CascadeClassifier('../cascade_c_hw.xml')
h_cascade = cv2.CascadeClassifier('../cascade_h_hw.xml')

st.title("Reza's Object Detection")

scale = st.slider('Scale', min_value=1.01, max_value=20.0, value=1.2)
no_neighbors = st.slider('No Neighbors', min_value=1, max_value=200, value=10)
min_size = st.slider('Min Size', min_value=1, max_value=500, value=10)
max_size = st.slider('Max Size', min_value=1, max_value=500, value=150)

run = st.sidebar.checkbox('Live', value=False)
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)
take_picture = st.sidebar.button('Take a picture')
classify = st.sidebar.checkbox('Classify')

upper_left = (300, 200)
bottom_right = (800, 500)

if take_picture:
    run = False
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #Rectangle marker
    r = cv2.rectangle(frame, upper_left, bottom_right, (100, 50, 200), 5)
    rect_img = frame[upper_left[1] : bottom_right[1], upper_left[0] : bottom_right[0]]

    image = rect_img
    cv2.imwrite('Images/image_atoms.jpg', image)

if classify:
    img = cv2.imread('app/dashboard/Images/image_atoms.jpg')
    st.write(os.listdir())
    os.chdir('app/dashboard')
    st.write(os.getcwd())
    st.write(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    c_atoms = c_cascade.detectMultiScale(gray, scale, no_neighbors, minSize=(min_size,min_size), maxSize=(max_size,max_size)) 
    h_atoms = h_cascade.detectMultiScale(gray, scale, no_neighbors, minSize=(min_size,min_size), maxSize=(max_size,max_size)) 
    for (x,y,w,h) in c_atoms:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),10)
    for (x,y,w,h) in h_atoms:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),10)
    st.write('Recognized {} C atoms and {} H atoms'.format(len(c_atoms), len(h_atoms)))
    st.image(img)



while run:
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #Rectangle marker
    r = cv2.rectangle(frame, upper_left, bottom_right, (100, 50, 200), 5)
    rect_img = frame[upper_left[1] : bottom_right[1], upper_left[0] : bottom_right[0]]

    


    img = rect_img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    c_atoms = c_cascade.detectMultiScale(gray, scale, no_neighbors, minSize=(min_size,min_size), maxSize=(max_size,max_size)) 
    h_atoms = h_cascade.detectMultiScale(gray, scale, no_neighbors, minSize=(min_size,min_size), maxSize=(max_size,max_size)) 
    for (x,y,w,h) in c_atoms:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),10)
    for (x,y,w,h) in h_atoms:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),10)
    #st.write('Recognized {} C atoms and {} H atoms'.format(len(c_atoms), len(h_atoms)))
    #st.image(img)


    #frame[upper_left[1] : bottom_right[1], upper_left[0] : bottom_right[0]] = rect_img
    frame[upper_left[1] : bottom_right[1], upper_left[0] : bottom_right[0]] = img

    FRAME_WINDOW.image(frame)