import cv2
import time
import datetime as dt

class SecurityCamera(object):
    def __init__(self, camera_num:int=0):
        """
        Camera object initialization.

        Args:
            camera_num (int): Webcam number
        
        Properties:
            video (cv2.VideoCapture): Video capture object
            is_running (bool): True if the camera is running
            color (tuple): RGB color of the rectangle
        """
        self.video = cv2.VideoCapture(camera_num, cv2.CAP_DSHOW)
        self.is_running = False
        self.color = (0, 255, 0)
        
        print("Camera setup complete.")
        
    def record(self):
        self.is_running = True
        detection = False
        timer_started = False
        detection_stopped_time = None
        SECONDS_TO_RECORD_AFTER_DETECTION = 5
        
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

        frame_size = (int(self.video.get(3)), int(self.video.get(4)))
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")

        while self.is_running:
            _, frame = self.video.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.2, 5)
            bodies = body_cascade.detectMultiScale(gray, 1.2, 5)

            if len(faces) + len(bodies) > 0:
                if detection:
                    timer_started = False
                else:
                    detection = True
                    current_time = dt.datetime.now().strftime("%d %B %Y, %I:%M:%S %p")
                    out = cv2.VideoWriter(f"Recording-[{current_time}].mp4", fourcc, 30, frame_size)
                    print("Started Recording!")
                    
            elif detection:
                if timer_started:
                    if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
                        detection = False
                        timer_started = False
                        out.release()
                        print('Stop Recording!')
                else:
                    timer_started = True
                    detection_stopped_time = time.time()

            if detection:
                out.write(frame)

            # Display colored rectangles around faces
            for (x, y, width, height) in faces:
                time_stamp = dt.datetime.now().strftime("%I:%M:%S %p")
                image = cv2.rectangle(frame, (x, y), (x + width, y + height), self.color, 3)
                cv2.putText(image, f'{time_stamp}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

            cv2.imshow("Camera", frame)

            # Press "Esc" key to close
            key = cv2.waitKey(30)
            if key == 27:
                print("Ending recording session.")
                self.is_running = False
                break

        out.release()
        self.video.release()
        cv2.destroyAllWindows()
    

if __name__ == "__main__":
    CAM_NUM = 0
    cam = SecurityCamera(CAM_NUM)
    cam.record()
