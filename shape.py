import cv2
import numpy as np

def detect_traffic_light(image_path):
    # 이미지 로드
    image = cv2.imread(image_path)

    # 이미지를 HSV 형식으로 변환
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 검은색과 회색 범위
    lower_dark = np.array([0, 0, 0])
    upper_dark = np.array([180, 255, 48])

    # 마스크 생성
    mask_dark = cv2.inRange(hsv_image, lower_dark, upper_dark)

    # 이미지에서 Contour(윤곽선) 검출
    contours, _ = cv2.findContours(mask_dark, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 감지된 모든 Contour에 대해 반복
    all_rectangles = []
    for contour in contours:
        # 현재 Contour에 대한 사각형 좌표 가져오기
        x, y, w, h = cv2.boundingRect(contour)
        all_rectangles.append((x, y, w, h, cv2.contourArea(contour)))

    # 가장 큰 상위 2개의 사각형 선택
    top_rectangles = sorted(all_rectangles, key=lambda rect: rect[4], reverse=True)[:2]
    return top_rectangles, image, hsv_image