import cv2
import time
from datetime import datetime

vcap = cv2.VideoCapture("rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov")

fourcc = cv2.VideoWriter_fourcc(*'XVID')

fps = vcap.get(cv2.CAP_PROP_FPS)
width = vcap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = vcap.get(cv2.CAP_PROP_FRAME_HEIGHT) 

curr_time = datetime.now()
formatted_time = curr_time.strftime('%Y%m%d_%H%M%S')

vout = cv2.VideoWriter()
vout.open(formatted_time+'.avi', fourcc, int(fps), (int(width), int(height)), True)

cnt = 0
while (cnt < (int(fps) * 60)):
    ret, frame = vcap.read()
    vout.write(frame)
    cnt += 1
    cv2.imshow('VIDEO', frame)
    cv2.waitKey(1)
vout.release()
vcap.release()
