import numpy as np
import cv2

file_path = "Sample.mp4"

#Load Video
cap = cv2.VideoCapture(file_path)

#Get Width & Height & FPS
Vwidth = cap.get(3)
Vheight = cap.get(4)
fps = round(cap.get(5),0)

print(str(Vwidth) + 'x' + str(Vheight) + ' , ' + str(fps) + 'fps')

#Get total number of frames
TotalFrames =  int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print("Total Frames: " ,TotalFrames )

result = None

#Start
while True:

#Load the video into capture reader
    ret, frame = cap.read()
    
#Get position of the current frame and calculate the current % done
    Current_Frame_POS = int( cap.get(1) )
    Learnstr = "Learning: " + str(Current_Frame_POS) + "/" + str(TotalFrames) + " " + str(round(Current_Frame_POS/ TotalFrames*100,1)) +'%' 
    # print(Learnstr)

#To avoid errors in frames
    if frame is None:
        break

#Initialize the average 
    if Current_Frame_POS == 1:
        avg = np.float32(frame)

#Calculate the accumulated weight of the input image and the learned images
    cv2.accumulateWeighted(frame, avg, 0.005) 
    result = cv2.convertScaleAbs(avg)

#Type on frame
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    fontScale              = 0.5 #Font Scale
    fontColor              = (255,255,255) #White
    lineType               = 2 #Font Thickness
    cv2.putText(frame,Learnstr, (10,30), font, fontScale,fontColor, lineType)

#Show Video
    cv2.imshow('Orgiginal',frame)
    
#Press ESC to quit
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        exit()

cv2.imshow('result', result)
cv2.imwrite('BG.jpg', result)
cv2.waitKey(0)

# Release Capture when Done
cap.release()
cv2.destroyAllWindows()