import sys
import os.path
import cv2

def solve(filename):
    im = cv2.imread(filename)
    im_flip_both = cv2.flip(im, -1)     # -1 means flip in both axis
#     cv2.imshow("im_flip_both", im_flip_both)
#     cv2.waitKey(0)
    cv2.imwrite("ans2.png", im_flip_both)

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except:
        print "invalid input argv: {a}".format(a=sys.argv)
        raise
    assert os.path.isfile(filename)
    solve(filename)
