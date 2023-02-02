import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "Mercury",
            (50,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))
cv2.putText(img,
            "Venus",
            (80,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))
cv2.putText(img,
            "Earth",
            (110,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))
cv2.putText(img,
            "Mars",
            (140,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))
cv2.putText(img,
            "Jupiter",
            (170,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))
            