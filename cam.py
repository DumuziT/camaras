import cv2

def main():
    cap = cv2.VideoCapture("rtsp://admin1:asdqwe123@192.168.9.14:554/videoMain")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: break
        cv2.imshow('RTSP Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
