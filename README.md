## ABSTRACTION.

COVID-19 pandemic has rapidly affected our life disrupting the world trade and movements. Wearing a protective face mask has become a new normal. As we know it's a dangerous 
virus which can be spreading from humans to humans through droplets and airborne and as for the prevention, wearing a face mask is essentials while going outside or meeting to others. 
However, some irresponsible people refuse to wear face mask with so many excuses. Therefore, face mask detection has become a crucial task to help global society. This 
documentation presents a simple approach to achieve this purpose using some basic Machine Learning packages like TensorFlow, Keras, OpenCV, and Scikit-Learn. With the help 
of OpenCV we were able to capture the video feed from different sources like webcam, video file or an IP camera. The proposed method detects the face from the image correctly 
and then identifies if it has a mask on or not. As a surveillance task performer, it can also detect a face along with a mask in motion. The method attains average accuracy up to 
99.6% and 99.8% respectively on two different datasets.

## INTRODUCTION.

Coronavirus disease 2019 (COVID-19) has globally infected over 216 million people causing  over 4.5 million deaths. Individuals with COVID-19 have had a wide scope of symptoms 
reported – going from mellow manifestations to serious illness. Respiratory problems like shortness of breath or difficulty in breathing is one of them. Elder people having lung disease 
can possess serious complications from COVID-19 illness as they appear to be at higher risk. To curb certain respiratory viral ailments, including COVID-19, wearing a clinical mask is very 
necessary. The public should be aware of whether to put on the mask for source control or aversion of COVID-19. Potential points of interest of the utilization of masks lie in reducing 
vulnerability of risk from a noxious individual during the "pre-symptomatic" period and stigmatization of discrete persons putting on masks to restraint the spread of virus. Therefore, 
face mask detection has become a crucial task in present global society.Face mask detection involves in detecting the location of the face and then determining 
whether it has a mask on it or not. The issue is proximately cognate to general object detection to detect the classes of objects. Face identification categorically deals with 
distinguishing a specific group of entities i.e., Face. It has numerous applications, such as autonomous driving, education, surveillance, and so on. To overcome this situation, a 
robust face mask detection needs to be developed. In order to detect a face mask, the object detection algorithm can be implemented. The state of art of object detection 
algorithm which has a robust performance is the You Only Look Once (YOLO). A few years later, YOLO method was improved to YOLO V2 which was able to detect over 9000 object 
categories. In this version, a novel, multi-scale training method was developed [6]. Thereafter, Kim, et al., implemented the YOLO-V2 for image recognition and other 
testbenches for a CNN accelerator. In this work, the YOLO V2 method has been applied through the simulation and FPGA experiment. Harisankar, et al. on the other hand, modified 
the YOLO V2 to detect and localize the pedestrian by adding the Model H architecture. In order to detect the pedestrian precisely, they used ZED camera and created the depth 
map. Within two years Redmon, et al., introduced the YOLO V3 although the architecture is a little bigger than the last time, this version is accurately as SSD algorithm but three times 
faster. Therefore, Hu, et al. implemented this version to detect the workers with or without helmets in videos. The first, YOLO V3 model was to identify and intercept the worker video 
then made the sample model of wearing and not wearing helmet. The theorical analysis and experimental results verify that the proposed algorithm is able to detect the helmet 
with high detection accuracy. Because of the YOLO method is open source, then it allows everyone to improve the algorithm of the YOLO method. As presented in, Alexey, et al. 
introduced the YOLOv4 with optimal speed and accuracy. In this work, they assumed that such universal features such as Weighted-Residual-Connections (WRC), Cross-Stage-Partial 
connections (CSP), Cross mini-Batch Normalization (CmBN), Self-adversarial-training (SAT) and Mish activation are able to give high detection accuracy. According to the state of 
arts and the results which have already been tested by some researcher, in this work we developed a face mask detection for COVID-19 prevention by using the YOLO V4 
algorithm. the YOLO v4 algorithm will be used to detect the face mask. The face mask detection will be applied in real-time application to detect all types of commercial face 
mask. By adding the YOLO V4, it is hoped that this device able to detect whether the users are wearing a face mask or not...

## DATASET.
our dataset is avialable on kaggle [here](https://www.kaggle.com/datasets/ashishjangra27/face-mask-12k-images-dataset)
    12K Images divided in training, testing and validation directories.

<p float="left">
<img src= "https://user-images.githubusercontent.com/84151016/179366324-836daaca-7dee-450a-b319-47f5fcf22d2f.png", width=300, height=400 />
<img src= "https://user-images.githubusercontent.com/84151016/179366346-5205c64f-97c8-4e15-aa78-f7518fc17e17.png", width=300, height=400 />
<img src= "https://user-images.githubusercontent.com/84151016/179366377-4441b3fd-6bf2-4343-9634-fd09c5a8afe2.png", width=300, height=400 />
</p>

## A brief look over the models
I have trayies to build our model depending on different deep learning architectures, such as AlexNet, DenseNet and MobileNet.


## Conclusions

During this work, we have trained so many models and finally we’ve come up with 3 models that represent the different stages we’ve come across until we reached these 
results. The final model has been developed to come up with an efficient way for detecting and notifying officials when a person does not follow the COVID 19 safety 
protocols in a workplace, business establishments …etc
