import cv2
import mediapipe as mp

# 初始化Mediapipe的手部模型
mp_hands = mp.solutions.hands

def main():
    # 打开摄像头
    cap = cv2.VideoCapture(0)

    # 初始化手部识别器
    with mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5) as hands:

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # 将图像从BGR转换为RGB
            image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # 手部识别
            results = hands.process(image_rgb)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # 获取手部关键点的位置
                    for idx, landmark in enumerate(hand_landmarks.landmark):
                        h, w, c = frame.shape
                        cx, cy = int(landmark.x * w), int(landmark.y * h)

                        # 在图像上绘制关键点
                        cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)

            # 显示图像
            cv2.imshow('Hand Gesture Recognition', frame)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
