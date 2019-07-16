import cv2
import numpy as np
from styx_msgs.msg import TrafficLight

class TLClassifier(object):
    def __init__(self):
        pass

    def get_classification(self, image):
        """Determines the color of the traffic light in the image
        Args:
            image (cv::Mat): image containing the traffic light
        Returns:
            int: ID of traffic light color (specified in styx_msgs/TrafficLight)
        """

        # Convert image to HSV  color space  
        hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV) 
        
        #Define color ranges to look for traffic light colors
        min_color = np.array([330/360*255, 100, 100])
        max_color = np.array([30/360*255, 255, 255])

        color_count = cv2.countNonZero(cv2.inRange(hsv, min_color, max_color))
     
        #Leaving out yellow because unnecessary for our implementation 
        if color_count > 100:
            return TrafficLight.RED
        else:
           min_color[0] += 120
           max_color[1] += 120
           color_count = cv2.countNonZero(cv2.inRange(hsv, min_color, max_color))
           if cv2.countNonZero(color_count) > 100:
               return TrafficLight.GREEN

        return TrafficLight.UNKNOWN
