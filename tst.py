import cv
capture = cv.CaptureFromCAM(-1)
cv.NamedWindow("capture", cv.CV_WINDOW_AUTOSIZE)
while True:
	frame = cv.QueryFrame(capture)
	cv.ShowImage("capture", frame)
	cv.WaitKey(10)
	path = "capture.jpg"
	cv.SaveImage(path, frame)