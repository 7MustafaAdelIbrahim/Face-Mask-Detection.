## ABSTRACTION.

COVID-19 pandemic has rapidly affected our life disrupting the world trade and movements. Wearing a protective face mask has become a new normal. As we know it's a dangerous 
virus which can be spreading from humans to humans through droplets and airborne and as for the prevention, wearing a face mask is essentials while going outside or meeting to others. 
However, some irresponsible people refuse to wear face mask with so many excuses. Therefore, face mask detection has become a crucial task to help global society. This 
documentation presents a simple approach to achieve this purpose using some basic Machine Learning packages like TensorFlow, Keras, OpenCV, and Scikit-Learn. With the help 
of OpenCV we were able to capture the video feed from different sources like webcam, video file or an IP camera. The proposed method detects the face from the image correctly 
and then identifies if it has a mask on or not. As a surveillance task performer, it can also detect a face along with a mask in motion. The method attains average accuracy up to 
99.6% and 99.8% respectively on two different datasets.

## DATASET.
our dataset is avialable on kaggle [here](https://www.kaggle.com/datasets/ashishjangra27/face-mask-12k-images-dataset)
    12K Images divided in training, testing and validation directories.

<p float="left">
<img src= "https://user-images.githubusercontent.com/84151016/179366324-836daaca-7dee-450a-b319-47f5fcf22d2f.png", width= 280, height= 500 />
<img src= "https://user-images.githubusercontent.com/84151016/179366346-5205c64f-97c8-4e15-aa78-f7518fc17e17.png", width= 280, height= 500 />
<img src= "https://user-images.githubusercontent.com/84151016/179366377-4441b3fd-6bf2-4343-9634-fd09c5a8afe2.png", width= 280, height= 500 />
</p>

## A brief look over the models
I have trayies to build our model depending on different deep learning architectures, such as AlexNet, DenseNet and MobileNet.

## METHODOLOGY.

<img src= "https://user-images.githubusercontent.com/84151016/179366925-e9d4c34e-babe-46e0-a4fc-473dbad6dbde.png" width= 500, height= 300>


## CONCLUSIONS.

During this work, we have trained so many models and finally we’ve come up with 3 models that represent the different stages we’ve come across until we reached these 
results. The final model has been developed to come up with an efficient way for detecting and notifying officials when a person does not follow the COVID 19 safety 
protocols in a workplace, business establishments …etc
