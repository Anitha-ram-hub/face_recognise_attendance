import RPi.GPIO as GPIO
import cv2
import time

# ---------- CONFIG ----------
BUTTON_PIN = 26  # button between GPIO26 and GND

TRAINER_PATH = 'trainer/trainer.yml'          # path to your trained file
CASCADE_PATH = 'haarcascade_frontalface_default.xml'

# index 0 = "None" placeholder, then your IDs in order (1,2,3...)
names = ['None', 'Person1', 'Person2', 'Person3']  # <-- edit to match your dataset IDs
# ------------------------------

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(TRAINER_PATH)
faceCascade = cv2.CascadeClassifier(CASCADE_PATH)
font = cv2.FONT_HERSHEY_SIMPLEX


def run_face_recognition():
    """Opens camera, runs recognition, closes when user presses 'q'/ESC."""
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)
    cam.set(4, 480)
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    print("Camera started. Press 'q' in the video window to stop this session.")

    while True:
        ret, img = cam.read()
        if not ret:
            print("Camera read failed.")
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH))
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id_, confidence = recognizer.predict(gray[y:y + h, x:x + w])

            if confidence < 100:
                label = names[id_] if id_ < len(names) else "Unknown"
            else:
                label = "unknown"

            conf_text = "  {0}%".format(round(100 - confidence))
            cv2.putText(img, str(label), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, conf_text, (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

        cv2.imshow('Face Recognition', img)
        k = cv2.waitKey(10) & 0xff
        if k == 27 or k == ord('q'):  # ESC or 'q' to exit this session
            break

    cam.release()
    cv2.destroyAllWindows()
    print("Session ended. Waiting for next button press...")


def main():
    print("System ready. Press the button (GPIO26) to start face recognition.")
    print("Press Ctrl+C in Thonny/terminal to exit the whole program.")
    try:
        while True:
            if GPIO.input(BUTTON_PIN) == GPIO.LOW:
                time.sleep(0.05)  # simple debounce
                if GPIO.input(BUTTON_PIN) == GPIO.LOW:
                    run_face_recognition()
                    time.sleep(0.5)  # avoid instant re-trigger after closing window
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        GPIO.cleanup()


if __name__ == "__main__":
    main()
