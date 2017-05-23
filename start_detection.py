import cv2
import sys

from face_train import Model
#from post_detection import show_image


if __name__ == '__main__':

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cant connect to the camera")
        sys.exit(0)

    # TODO add the paths to the config file
    cascade_path = "/home/kartikeya/TensorFlow/Packages/opencv/data/haarcascades/haarcascade_frontalface_default.xml"
    eye_cascade_path = '/home/kartikeya/TensorFlow/Packages/opencv/data/haarcascades/haarcascade_eye.xml'

    model = Model()
    model.load()

    # Continue the loop until the escapce key
    while True:

        is_read, frame = cap.read()
        
        if not is_read:
            print("Unable to read the frame from the camera");
            sys.exit(0);

      	# convert to gray scale - reduce complexity and S2N
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # face recognition using the frontal face cascade
        cascade = cv2.CascadeClassifier(cascade_path)
        eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

        # use face detection using opencv
        # play around more with the scale factor
        facerect = cascade.detectMultiScale(frame_gray, scaleFactor=1.5, minNeighbors=3, minSize=(10, 10))
        eyes = eye_cascade.detectMultiScale(frame_gray)

        if len(facerect) > 0:
            print('face detected')
            # white color bounding box
            color = (255, 255, 255)
            for rect in facerect:
                # draw a rectanagle around the detected face
                cv2.rectangle(frame, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), color, thickness=2)

                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(frame, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
                x, y = rect[0:2]
                width, height = rect[2:4]
                image = frame[y - 10: y + height, x: x + width]
                cv2.imshow( "Face Detection", image )
                result = model.predict(image)
                print(result)
                if result == 0:  # KK
                    print('Image match! KK identified')
                    import time
                    time.sleep(5)
                else:
                    print('No match yet')

        k = cv2.waitKey(100)

    # clear up the windows
    cap.release()
    cv2.destroyAllWindows()
