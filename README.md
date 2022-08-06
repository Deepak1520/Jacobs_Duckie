# Jacobs_Duckie
Members:
- Deepak Budha
- Santosh Luitel
- Uriel

This project is based on the duckietown project where we detect a straight line i.e. either a black line placed on a contrasting colored surface or a white line as long as the Jacobs_Duckie can see it..

# Problem we are solving and a solution
We are considering the object detecting and vision part of the duckietown.
We take a  as a target object which we want to detect and make the duckieking follow the ball.
We are using **Hough Transforms** algorithm to detect the straight line. we are using
the implementation from *cv2* to detect the number of straight lines in the
camera setting. So we have the function parameters as mathematical formula to detect the stright line. Any black straight line placed on a contrasting colored surface or a white line can be used as a demo. We have used a black taped straight line.


# RUN 
The code is written in python script which can be run directly in a ROS
environment. cd into the source folder. run `chmod +x main.py` to be able to
run the py script as executable. Then directly run `./main.py`.

`utils.py` script contains the algorithm(cht) that we are using for the detection.

P.S. you might also need to have duckietowns_msgs package for ROS message and services definitions in the directory with main.py.


