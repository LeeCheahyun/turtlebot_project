import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from std_msgs.msg import String


to_TB_data=rospy.Publisher('TB_data',String,queue_size=10)
tb1="/tb3_0"
tb2="/tb3_1"
tb3="/tb3_2"
tb4="/tb3_3"
tb5="/tb3_4"

def callback0(data):
    # print(data.)
    x = data.pose.pose.position.x
    y = data.pose.pose.position.y
    z = data.pose.pose.orientation.z


    print(data.pose.pose.position.x)
    print(data.pose.pose.position.y)
    print(data.pose.pose.orientation.z)
    print()
    pos_data={data.pose.pose.position.x,data.pose.pose.position.y,data.pose.pose.orientation.z}
    txt = f"{tb1}_{x}_{y}_{z}"
    to_TB_data.publish(txt)

def callback1(data):
    # print(data.)
    x = data.pose.pose.position.x
    y = data.pose.pose.position.y
    z = data.pose.pose.orientation.z


    print(data.pose.pose.position.x)
    print(data.pose.pose.position.y)
    print(data.pose.pose.orientation.z)
    print()
    pos_data={data.pose.pose.position.x,data.pose.pose.position.y,data.pose.pose.orientation.z}
    txt = f"{tb2}_{x}_{y}_{z}"
    to_TB_data.publish(txt)

def callback2(data):
    # print(data.)
    x = data.pose.pose.position.x
    y = data.pose.pose.position.y
    z = data.pose.pose.orientation.z


    print(data.pose.pose.position.x)
    print(data.pose.pose.position.y)
    print(data.pose.pose.orientation.z)
    print()
    pos_data={data.pose.pose.position.x,data.pose.pose.position.y,data.pose.pose.orientation.z}
    txt = f"{tb2}_{x}_{y}_{z}"
    to_TB_data.publish(txt)

def callback3(data):
    # print(data.)
    x = data.pose.pose.position.x
    y = data.pose.pose.position.y
    z = data.pose.pose.orientation.z


    print(data.pose.pose.position.x)
    print(data.pose.pose.position.y)
    print(data.pose.pose.orientation.z)
    print()
    pos_data={data.pose.pose.position.x,data.pose.pose.position.y,data.pose.pose.orientation.z}
    txt = f"{tb3}_{x}_{y}_{z}"
    to_TB_data.publish(txt)

def callback4(data):
    # print(data.)
    x = data.pose.pose.position.x
    y = data.pose.pose.position.y
    z = data.pose.pose.orientation.z

    print(data.pose.pose.position.x)
    print(data.pose.pose.position.y)
    print(data.pose.pose.orientation.z)
    print()
    pos_data={data.pose.pose.position.x,data.pose.pose.position.y,data.pose.pose.orientation.z}
    txt = f"{tb4}_{x}_{y}_{z}"
    to_TB_data.publish(txt)

if __name__=='__main__':

    rospy.init_node('pose_pub')
    # tb0 is master
    # 보내야하는 publisher name =시나리오 쓰고있네(TB_data) 형식은 string[tb.name_x_y_z]

    tb0_pos=rospy.Subscriber('/amcl_pose',PoseWithCovarianceStamped,callback=callback0)
    # tb1_pos=rospy.Subscriber('/amcl_pose',PoseWithCovarianceStamped,callback=callback1)
    # tb2_pos=rospy.Subscriber('/amcl_pose',PoseWithCovarianceStamped,callback=callback2)
    # tb3_pos=rospy.Subscriber('/amcl_pose',PoseWithCovarianceStamped,callback=callback3)
    # tb4_pos=rospy.Subscriber('/amcl_pose',PoseWithCovarianceStamped,callback=callback4)

    rospy.spin()
    pass