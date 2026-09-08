import cv2
import numpy as np

# Initialize 2D Kalman Filter
def init_kalman_filter():
    # 4 state variables: [x, y, vx, vy] (Posisi x, y dan Kecepatan vx, vy)
    # 2 measurement variables: [x, y]
    kalman = cv2.KalmanFilter(4, 2)
    kalman.measurementMatrix = np.array([[1, 0, 0, 0],
                                         [0, 1, 0, 0]], np.float32)
    
    # State Transition Matrix (A)
    kalman.transitionMatrix = np.array([[1, 0, 1, 0],
                                        [0, 1, 0, 1],
                                        [0, 0, 1, 0],
                                        [0, 0, 0, 1]], np.float32)
    
    # Noise covariance matrices
    kalman.processNoiseCov = np.eye(4, dtype=np.float32) * 0.03
    kalman.measurementNoiseCov = np.eye(2, dtype=np.float32) * 0.5
    kalman.errorCovPost = np.eye(4, dtype=np.float32)
    return kalman

def detect_yellow_object(frame):
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    yellow_mask = cv2.inRange(hsv_frame, lower_yellow, upper_yellow)
    yellow_result = cv2.bitwise_and(frame, frame, mask=yellow_mask)
    return yellow_result

def calculate_distance(radius_in_pixels, actual_object_size, focal_length):
    if radius_in_pixels == 0:
        return 0
    # Formula perkiraan jarak berdasarkan diameter/radius
    distance = (actual_object_size * focal_length) / (2 * radius_in_pixels)
    return distance

def detect_ball_realtime():
    # Menggunakan kamera bawaan laptop (indeks 0)
    cap = cv2.VideoCapture(0)
    
    # Parameter fisik
    actual_ball_diameter_cm = 10.0  # Sesuaikan dengan diameter bola asli (cm)
    focal_length = 500.0             # Nilai focal length disesuaikan dengan kamera laptop

    # Inisialisasi Kalman Filter
    kalman = init_kalman_filter()
    kalman_initialized = False

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Gagal mengambil frame dari kamera laptop.")
            break

        frame_with_yellow_text = detect_yellow_object(frame)
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurFrame = cv2.GaussianBlur(grayFrame, (17, 17), 0)

        # Deteksi lingkaran menggunakan HoughCircles
        circles = cv2.HoughCircles(
            blurFrame, 
            cv2.HOUGH_GRADIENT, 
            dp=1.2, 
            minDist=500,
            param1=95, 
            param2=40, 
            minRadius=20, 
            maxRadius=100
        )

        # Step 1: Prediksi lokasi bola dengan Kalman Filter
        predicted = kalman.predict()
        pred_x, pred_y = int(predicted[0][0]), int(predicted[1][0])

        ball_detected = False

        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                center_x, center_y, radius_in_pixels = i[0], i[1], i[2]

                # Step 2: Koreksi/Update Kalman Filter dengan deteksi nyata
                measurement = np.array([[np.float32(center_x)], [np.float32(center_y)]])
                
                if not kalman_initialized:
                    kalman.statePost = np.array([[np.float32(center_x)], 
                                                 [np.float32(center_y)], 
                                                 [0], 
                                                 [0]], np.float32)
                    kalman_initialized = True
                
                kalman.correct(measurement)
                ball_detected = True

                # Visualisasi Deteksi Nyata (Lingkaran Hijau & Titik Merah)
                cv2.circle(frame, (center_x, center_y), radius_in_pixels, (0, 255, 0), 2)
                cv2.circle(frame, (center_x, center_y), 2, (0, 0, 255), 3)

                # Hitung Jarak
                distance = calculate_distance(radius_in_pixels, actual_ball_diameter_cm, focal_length)
                
                # Tampilkan Teks
                cv2.putText(frame, f"Distance: {distance:.2f} cm", (center_x - 50, center_y + 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
                cv2.putText(frame, f"Coords: ({center_x}, {center_y})", (center_x - 50, center_y + 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
                break

        # Step 3: Handling Occlusion (Jika Bola Terhalang / Tidak Terdeteksi)
        if not ball_detected and kalman_initialized:
            # Tampilkan posisi hasil prediksi Kalman (Lingkaran Cyan & Titik Kuning)
            cv2.circle(frame, (pred_x, pred_y), 25, (255, 255, 0), 2)
            cv2.circle(frame, (pred_x, pred_y), 3, (0, 255, 255), -1)
            cv2.putText(frame, "Predicting (Occluded)", (pred_x - 60, pred_y - 35),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

        # Tampilkan Window Hasil
        cv2.imshow("Deteksi Warna Kuning", frame_with_yellow_text)
        cv2.imshow("Tracking Bola + Kalman Filter", frame)

        # Tekan tombol 'q' untuk keluar
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_ball_realtime()