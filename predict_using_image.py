import cv2
import sys
import os
from gabor_filter import apply_gabor_filter
from face_train import Model

# from post_detection import show_image


def crop_face(image_path):

    for file_or_dir in os.listdir(image_path):
        abs_path = os.path.abspath(os.path.join(image_path, file_or_dir))
        print(file_or_dir)

        if file_or_dir == ".placeholder":
            continue

        image = cv2.imread(abs_path)
        frame_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # face recognition using the frontal face cascade
        cascade = cv2.CascadeClassifier(cascade_path)
        eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

        # use face detection using opencv
        # play around more with the scale factor
        facerect = cascade.detectMultiScale(frame_gray, scaleFactor=1.6, minNeighbors=3, minSize=(10, 10))
        eyes = eye_cascade.detectMultiScale(frame_gray)

        color = (255, 255, 255)
        for rect in facerect:
            #cv2.rectangle(image, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), color, thickness=2)

            #for (ex, ey, ew, eh) in eyes:
            #    cv2.rectangle(image, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            x, y = rect[0:2]
            width, height = rect[2:4]
            image = image[y - 10: y + height, x: x + width]
            cv2.imwrite(image_path + file_or_dir, image)


def gabor_filter_to_pics(image_path):

    for file_or_dir in os.listdir(image_path):
        abs_path = os.path.abspath(os.path.join(image_path, file_or_dir))
        print(file_or_dir)

        if file_or_dir == ".placeholder":
            continue

        image = cv2.imread(abs_path)
        frame_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        image = apply_gabor_filter(image)

        cv2.imwrite(image_path + "_00" + file_or_dir, image)


def verify_model_from_hdd_images(image_path):

    import os
    correct_detected_count = 0

    for file_or_dir in os.listdir(image_path):
        abs_path = os.path.abspath(os.path.join(image_path, file_or_dir))
        print(file_or_dir)

        if file_or_dir != ".placeholder":
            image = cv2.imread(abs_path)
        else:
            print("place holder detected")
            continue

        # cv2.imshow("Face Detection", image)
        # image = apply_gabor_filter(image)

        print(image.shape)
        result = model.predict(image)
        print(result)

        if result == 0:  # KK
            print('Image match! KK identified')
            correct_detected_count += 1
        else:
            print('No match yet')

    print("Total correctly detected images : ", correct_detected_count)

    #cv2.destroyAllWindows()

if __name__ == '__main__':

    # TODO add the paths to the config file
    cascade_path = "/home/kartikeya/TensorFlow/Packages/opencv/data/haarcascades/haarcascade_frontalface_default.xml"
    eye_cascade_path = '/home/kartikeya/TensorFlow/Packages/opencv/data/haarcascades/haarcascade_eye.xml'

    model = Model()
    model.load()

    image_path = "/home/kartikeya/TensorFlow/Projects/FBFaceDetection/data/user_pics/"

    # crop_face(image_path)
    # verify_model_from_hdd_images(image_path)
    gabor_filter_to_pics(image_path)
