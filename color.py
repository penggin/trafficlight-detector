import cv2
import numpy as np

def detect_color(top_rectangles, image, hsv_image):
    colors = {'red': 0, 'green': 0}
    # 선택된 사각형들 표시 및 초록색과 빨간색 비율 식별
    for rect in top_rectangles:
        x, y, w, h, area = rect
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # 사각형 영역 추출
        roi = hsv_image[y:y+h, x:x+w]

        # 초록색과 빨간색 범위
        lower_green = np.array([40, 40, 40])
        upper_green = np.array([80, 255, 255])

        lower_red = np.array([0, 40, 40])
        upper_red = np.array([10, 255, 255])

        # 초록색과 빨간색 마스크 생성
        mask_green = cv2.inRange(roi, lower_green, upper_green)
        mask_red = cv2.inRange(roi, lower_red, upper_red)

        # 초록색과 빨간색 픽셀 수 계산
        green_pixels = cv2.countNonZero(mask_green)
        red_pixels = cv2.countNonZero(mask_red)

        # 초록색과 빨간색 픽셀 수 비율 계산
        green_ratio = green_pixels / (green_pixels + red_pixels)
        red_ratio = red_pixels / (green_pixels + red_pixels)

        # 초록색 또는 빨간색 판단
        if green_ratio > red_ratio:
            color = "Green = {:.2f}".format(green_pixels)
            colors['green'] += green_pixels
        else:
            color = "Red = {:.2f}".format(red_pixels)
            colors['red'] += red_pixels

        # 결과에 색상 정보 추가
        cv2.putText(image, f"Color: {color}", (x, y + h + 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # 결과 표시
    cv2.imshow("Detected Pedestrian Traffic Light", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    if colors['red'] > colors['green']:
        print("Red")
    else:
        print("Green")