import cv2

img=cv2.imread("solar-system.jpg")


cv2.putText(img,"Sol",(100,80),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))
cv2.putText(img,"Mercurio",(120,180),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(img,"Venus",(195,260),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(img,"Terra",(300,260),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(img,"Marte",(400,260),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(img,"Jupter",(500,70),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(img,"Saturno",(700,80),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(img,"Urano",(900,150),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(img,"Netuno",(1100,100),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))


cv2.imshow("resultado",img)

cv2.waitKey(0)

#cv2.imwrite(“Solar_systemwithname.jpg”,img)