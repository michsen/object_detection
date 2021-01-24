# Start Appp

## App lokal

- app_local/dashboard
- streamlit run main.py

## App Web

- https://discuss.streamlit.io/t/new-component-streamlit-webrtc-a-new-way-to-deal-with-real-time-media-streams/8669


# Train Classifier

Quelle: https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/

1. get cropped images and store it in folder data/{object_name}_cropped

2. Create positive files for training
    - Resize to 50x50: image_preparation/Image_Preparation_for_Training.ipynb
        - Abschnitt Grayscale & Resize of already cropped images
    - Create Descritpion file: training_classifier/Image_Preparation_for_Training.ipynb
        - Abschnitt Descriptor Files

3. Upload Data to Server
    - Upload positives und negatives
    - Upload negatives.txt, Upload pos_info.lst (in den Ordner wo auch die positiv-Images liegen)
    - data - Ordner erstellen

4. Create Vector File
    - opencv_createsamples -info Bindung_normal_pos_hw/Bindung_normal_pos_hw_info.lst -num 1638 -w 20 -h 20 -vec positives_bindung_normal_hw.vec

5. Resize Server falls nötig auf mindestens 4 GB Arbeitsspeicher (Anleitung auf DigitalOccean)

6. Training Classifier
    - opencv_traincascade -data data_bindung_normal_hw -vec positives_bindung_normal_hw.vec -bg negatives_bindung_normal_hw.txt -numPos 1500 -numNeg 1500 -numStages 10 -w 20 -h 20