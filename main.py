from color import detect_color
from shape import detect_traffic_light

# 이미지 파일 경로
image_path = "./green.jpg"

# 인식 및 표시
rect, img, hsv_img = detect_traffic_light(image_path)
detect_color(rect, img, hsv_img)