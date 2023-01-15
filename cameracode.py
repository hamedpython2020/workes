import requests, cv2, imutils
import numpy as np

url = "http://192.168.0.103:8000/shot.jpg"

while True:
    img_re = requests.get(url)
    img_a = np.array(bytearray(img_re.content), dtype=np.uint8)

    img = cv2.imdecode(img_a, -1)
    img = imutils.resize(img, width=1000, height=1800)
    cv2.imshow("Android_cam", img)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
