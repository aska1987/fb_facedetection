# FBFaceDetection
Idea: Fetch photos from facebook and use it to train neural network to identify people

What works
----------

* The current implementation uses only a binary classifier.
* Thus, at the moment, it can recognise only one person.
* The pictures of the user (person to be identified) are stored in the data/user_pics
* The fetch_pictures_from_facebook.py script fetches the user pictures from his/her FB account. The pictures are downloaded in the path data/user_pics.
* AFLW dataset is used to differentiate between the user and other people ( Due to hardware limitation only few pictures from the AFLW dataset were used at the moment) https://lrs.icg.tugraz.at/research/aflw/
* The training uses simple network to learn the features
* Prediction simply marks the test image as of the user or other random people.
* The current recognition results are around 93% accuracy. Low availability of user pictures (i.e. myself :) ) and lack of hardware ( AFLW dataset is massive and need lot of disk and GPU access), thus couldn't train the network well.

On-going / Future work:
------------------------

* The project is NOT completed and the whole idea to integrate FB to the face recognition part is in basic stage.
* I need to test the network with massive dataset and check on the accuracy.
* I want to explore FACENET network and probably use it to increase the efficiency.
* I want to extent this to google or epson glasses.


Model accuracy and loss graphs
-------------------------------

![Alt text](https://github.com/kkarnatak/fb_facedetection/blob/master/store/graphs/model_acc.png?raw=true "Model Accuracy")
![Alt text](https://github.com/kkarnatak/fb_facedetection/blob/master/store/graphs/model_loss.png?raw=true "Model Loss")


The model accuracy increased to 94% when the face was cropped from the given images. I ran facedetection on the images, cropped them and enabled usual data augmentation provided within keras framework. The graphs are as below:

![Alt text](https://github.com/kkarnatak/fb_facedetection/blob/master/store/graphs/model_acc_crop.png?raw=true "Model Accuracy")
![Alt text](https://github.com/kkarnatak/fb_facedetection/blob/master/store/graphs/model_loss_crop.png?raw=true "Model Loss")
