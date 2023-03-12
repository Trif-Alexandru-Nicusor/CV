import cv2
import numpy as np

img=cv2.imread(input("Add file path:"))
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
mask=cv2.threshold(gray,250,255,cv2.THRESH_BINARY)[1]
mask=255-mask
kernel=np.ones((3,3),np.uint8)
mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
mask=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
mask=cv2.GaussianBlur(mask,(0,0),sigmaX=2,borderType=cv2.BORDER_DEFAULT)
mask=(2*(mask.astype(np.float32))-255.0).clip(0,255).astype(np.uint8)

result=img.copy()
result=cv2.cvtColor(result,cv2.COLOR_BGR2BGRA)
result[:, :, 3]=mask
cv2.imwrite("result.png",result)

cv2.imshow("INPUT",img)
cv2.imshow("GRAY",gray)
cv2.imshow("MASK",mask)
cv2.imshow("RESULT",result)
cv2.waitKey(0)
cv2.destroyAllWindows()