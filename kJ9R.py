#Tech-Gym-13-25-A
#���A���^�C���摜�F��

import cv2
import numpy as np

# Web�J����������͂��J�n
cap = cv2.VideoCapture(0)

while True:
    # �J�����̉摜��ǂݍ���
    _, frame = cap.read()
    
    # �摜���k���\������
    frame = cv2.resize(frame, (500,300))
    
    # �E�B���h�E�ɉ摜���o��
    cv2.imshow('OpenCV Web Camera', frame)
    
    # ESC��Enter�L�[�������ꂽ�烋�[�v�𔲂���
    k = cv2.waitKey(1) # 1msec�m�F
    if k == 27 or k == 13: break

cap.release() # �J���������
cv2.destroyAllWindows() # �E�B���h�E��j��