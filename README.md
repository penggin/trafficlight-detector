# Trafficlight-detector
![image](https://github.com/penggin/trafficlight-detector/assets/108963864/4878ada9-e576-4577-95e0-4ca77563dcde)
### team member:  
* Lee donghun 
* Lee seungjae
* Ahn Hyochan 
* You seongmin
  
### introduce : 
A program that detects the color of a traffic light and informs it

### purpose :
Traffic Light Color Classification Service for the Blind

### features
Distinguish between green and red traffic lights
separate the unique differences in color into numbers

### functions
* cv2.cvtColor() : changes the color to a number
* lower_color = np.array() : Arrangement limits each color to a numeric range ex) lower_red1 = np.array([0, 100, 100])
* cv2.inRange() : Create a mask by color
* imshow() : print the image

### languages used
* python
* python OpneCV (cv2)
* 

### Images used
![red](https://github.com/penggin/trafficlight-detector/assets/108963864/66d19815-9024-4e3a-8376-d671954bd0a5)
![green](https://github.com/penggin/trafficlight-detector/assets/108963864/5ce060e4-69a6-41d3-8e0e-19cb8a3789a1)
