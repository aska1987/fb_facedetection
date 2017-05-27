import numpy as np
import cv2
import sys

def build_filters():
    filters = []
    ksize = 31
    for theta in np.arange(0, np.pi, np.pi / 16):
        kern = cv2.getGaborKernel((ksize, ksize), 4.0, theta, 10.0, 0.5, 0, ktype=cv2.CV_32F)
    kern /= 1.5 * kern.sum()
    filters.append(kern)
    return filters


def process(img, filters):
    accum = np.zeros_like(img)
    for kern in filters:
        fimg = cv2.filter2D(img, cv2.CV_8UC3, kern)
    np.maximum(accum, fimg, accum)
    return accum


def apply_gabor_filter(image):
    print
    __doc__

    # image = cv2.imread(image)
    height, width, channel = image.shape

    if height > 800 or width > 800:
        image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

    # image = cv2.GaussianBlur(image, (5.5), 0)
    image = cv2.medianBlur(image, 5)
    image = cv2.bilateralFilter(image,9,75,75)
    # image = cv2.AddWeighted(image, 1.5, image, -0.5, 0)
    # if img is None:
    #    print( 'Failed to load image file:', img_path)
    #    sys.exit(1)

    filters = build_filters()

    res1 = process(image, filters)

    # cv2.imshow('result', res1)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return res1


if __name__ == "__main__":
    import os

    user_path = '/home/kartikeya/TensorFlow/Projects/FBFaceDetection/data/user_pics'
    other_path = '/home/kartikeya/TensorFlow/Projects/FBFaceDetection/data/others'

    for file_or_dir in os.listdir(user_path):
        abs_path = os.path.abspath(os.path.join(user_path, file_or_dir))
        print(abs_path)
        apply_gabor_filter(abs_path)
