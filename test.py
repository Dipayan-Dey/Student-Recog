    #===== Face Recognition ====== 
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int(100 * (1 - predict / 300))

                # DB Connection
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Ayan@123",
                    database="face_recognizer"
                )
                my_cursor = conn.cursor()

                # Fetch details from DB
                my_cursor.execute("SELECT name FROM students WHERE reg=%s", (id,))
                i = my_cursor.fetchone()
                i = "+".join(i) if i else "Unknown"

                my_cursor.execute("SELECT roll FROM students WHERE reg=%s", (id,))
                r = my_cursor.fetchone()
                r = "+".join(r) if r else "Unknown"

                my_cursor.execute("SELECT dep FROM students WHERE reg=%s", (id,))
                d = my_cursor.fetchone()
                d = "+".join(d) if d else "Unknown"

                conn.close()

                # Show details if confidence good
                if confidence > 77:
                    cv2.putText(img, f"Reg.no: {r}", (x, y - 65), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Name: {i}", (x, y - 40), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Department: {d}", (x, y - 15), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        # Load cascade and recognizer
        faceCascade = cv2.CascadeClassifier(r"D:\Student Face Recog system\haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("clissifire.xml")

        # Start video capture
        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press Enter to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()
