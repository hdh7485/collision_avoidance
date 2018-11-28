import rospy
from sensor_msgs.msg import LaserScan
from visualization_msgs.msg import Marker

class CollisionAvoidance():
	def __init__(self):
		rospy.Subscriber('scan', LaserScan, self.laser_cb)
		rospy.spin()
		
	def small_area_remove_filter(self, input_list, min_length):
		counter = 0
		i = 0
		first_index = 0
		while True:
			if i >= len(input_list):
				break
			if input_list[i] == 1:
				i += 1
			else:
				counter = 0
				first_index = i
				while input_list[i] == 0:
					i += 1	
					counter += 1
					if i >= len(input_list):
						break
				last_index = i
				if counter < min_length:
					while first_index < last_index:
						input_list[first_index] = 1
						first_index += 1	
		output_list = input_list
		return output_list
	
	def find_nearest_empty(self, input_list):
		left_first_empty = -1
		right_first_empty = -1
		for i in reversed(range(len(input_list)//2)):
			if output_list[i] == 0:
				left_first_empty = i
				break
		for i in range(len(input_list)//2, len(input_list)):
			if output_list[i] == 0:
				right_first_empty = i
				break
		return left_first_empty, right_first_empty

	def laser_cb(self, laser_data):
		empty_space = []
		for distance in laser_data.ranges:
			if distance < 0.4:
				empty_space.append(1)		
			else:
				empty_space.append(0)
		filtered_space = self.small_area_remove_filter(empty_space, 300)

		rospy.loginfo(laser_data.ranges)
		rospy.loginfo(filtered_space)

def main():
	rospy.init_node('collision_avoidance', anonymous=True)
	collision_avoidance = CollisionAvoidance()

if __name__ == '__main__':
	main()

