import cv
cv.NamedWindow("capture", cv.CV_WINDOW_AUTOSIZE)
capture = cv.CaptureFromCAM(-1)
fourcc = cv.CV_FOURCC('X','V','I','D')
fps = 14
w, h = 640, 480
stream = cv.CreateVideoWriter("test3.avi", fourcc, fps, (w, h))
while True:
	frame = cv.QueryFrame(capture)
	cv.ShowImage("capture", frame)
	cv.WaitKey(10)
	cv.WriteFrame(stream, frame)