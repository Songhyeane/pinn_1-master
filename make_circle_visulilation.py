import numpy as np
import math
import scipy as sp
import matplotlib.pyplot as plt
import os
from PIL import Image
from IPython.display import Image as Img
from IPython.display import display
import e_data2g_data as e2d
import pandas as pd

def find_a_x(thetar,thetal,d,hr,hl):
    if thetal > np.pi*0.5 :
        tan_l = np.tan(np.pi-thetal)
        if thetar  > np.pi*0.5:
            tan_r = - np.tan(np.pi - thetar)
        else :
            tan_r =   np.tan(thetar)
    else:
        tan_l = - np.tan(thetal)
        if thetar  > np.pi*0.5:
            tan_r = - np.tan(np.pi - thetar)
        else :
            tan_r =   np.tan(thetar)

    return (hr-tan_r*d-hl)/(tan_l-tan_r)

def find_a_y(thetar,thetal,d,hr,hl):
    x = find_a_x(thetar,thetal,d,hr,hl)
    if thetal > np.pi*0.5 :
        tan_l = np.tan(np.pi-thetal)
    else:
        tan_l = - np.tan(thetal)

    y = tan_l*x+hr
    return y

def cal_area_1(center_a,center_b,d,thetar,thetal,hr,hl):

    a = center_a
    b = center_b
    r = np.sqrt(pow((0.0 - a),2) + pow((hl - b),2))
    # theta_1 = np.arctan((hl - b) / (0 - a))
    # theta_2 = np.arctan((hr - b) / (d - a))

    # if theta_1 < 0.0 :
    #     theta_1 =np.pi + theta_1
    # if theta_2 < 0.0 :
    #     theta_2 =np.pi + theta_2
    theta_1 = np.pi-thetal

    theta_2 = thetar

    theta = abs(theta_1 - theta_2)

    point_1 = center_a +(center_b*center_a)/(r*np.sin(theta_1))

    point_2 = center_a +(center_b*(center_a-d))/(r*np.sin(theta_2))

    fan_shape = 0.5 * theta * (pow(r,2))

    triangle_1 = 0.5 * (0-point_1) * hl

    triangle_2 = 0.5 * (d - point_2) * hr

    triangle_3 = 0.5 * (point_2 - point_1) * (0-b)

    area = fan_shape - triangle_1 + triangle_2 - triangle_3

    # print(f'theta_1: {math.degrees(theta_1)} theta_2: {math.degrees(theta_2)} theta: {math.degrees(theta)}')

    return area

def cal_area_3(center_a,center_b,d,hr,hl):

    a = center_a
    b = center_b
    r = np.sqrt(pow((0.0 - a),2) + pow((hl - b),2))
    theta_1 = abs(np.arctan((hl - b) / (0 - a)))
    theta_2 = abs(np.arctan((hr - b) / (d - a)))

    # if theta_1 < 0.0 :
    #     theta_1 = - theta_1
    # if theta_2 < 0.0 :
    #     theta_2 = - theta_2

    theta = abs(theta_1 - theta_2)

    hl = r*np.sin(theta_1)+center_b
    hr = r*np.sin(theta_2)+center_b

    point_1 = (hl * a) / (hl - b)

    point_2 = d + (a - d) * hr / (hr - b)

    fan_shape = 0.5 * theta * (pow(r,2))

    triangle_1 = 0.5 * (0-point_1) * hl

    triangle_2 = 0.5 * (d - point_2) * hr

    triangle_3 = 0.5 * (point_2 - point_1) * (0-b)

    area = fan_shape - triangle_1 + triangle_2 - triangle_3

    # print(f'theta_1: {math.degrees(theta_1)} theta_2: {math.degrees(theta_2)} theta: {math.degrees(theta)}')

    return area


def cal_area_2(center_a,center_b,d,hr,hl):
    a,b = center_a,center_b
    r = np.sqrt(pow((0.0 - a),2) + pow((hl - b),2))

    def f(x):
        return np.sqrt(pow(r,2)-pow(x-a,2))+b

    area = sp.integrate.quad(f, 0, d)

    # (x-a)^2 + (y-b)^2 = r^2

    return area


import matplotlib.pyplot as plt
import numpy as np

def plot_circle_within_range(a, b, r, d):
    theta = np.linspace(0, np.pi, 100)
    x = a + r * np.cos(theta)
    y = b + r * np.sin(theta)

    plt.figure()
    plt.plot(x, y)
    plt.xlim(0, d)
    plt.ylim(0, 0.0004)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Circle within Range')
    plt.grid(True)
    #plt.show()

    return plt

def cal_r(center_a,center_b,d,hr,hl):
    a = center_a
    xl = 0.0
    xr = d
    hl = hl
    hr = hr
    b = center_b
    r = np.sqrt(pow((0.0 - a), 2) + pow((hl - b), 2))

    return r

def generate_gif(input_path,output_path):
    print(1)
    img_list = os.listdir(input_path)
    print(2)
    img_list = [input_path + '/' + x for x in img_list]
    images = [Image.open(x) for x in img_list]
    print(3)

    img = images[0]
    img.save(output_path, save_all=True, append_images=images[1:], loop=0xff, duration=100)
    # loop 반복 횟수
    # duration 프레임 전환 속도 (500 = 0.5초)
    return Img(url=output_path)

#generate_gif('./data/output/circle_by_original','./data/output/gifes1.gif')


cal_result_table = pd.DataFrame({'hl':e2d.make_list('./data/output/hl_table.txt'),
                             'hr':e2d.make_list('./data/output/hr_table.txt'),
                             'thetal_radian':e2d.make_list('./data/output/thetal_radian_table.txt'),
                             'thetar_radian':e2d.make_list('./data/output/thetar_radian_table.txt'),
                             'thetal_degree':e2d.make_list('./data/output/thetal_degree_table.txt'),
                             'thetar_degree':e2d.make_list('./data/output/thetar_degree_table.txt'),
                             'center_a':e2d.make_list('./data/output/the_center_of_a_circle.txt'),
                             'center_b':e2d.make_list('./data/output/the_center_of_b_circle.txt'),
                             'time':e2d.make_list('./data/output/time_table.txt'),
                              })

# for idx in range(cal_result_table.shape[0]):
#      serial = cal_result_table.loc[idx]
#      t = float(serial.time)
#      area=cal_area_1(float(serial.center_a),float(serial.center_b),0.000321,float(serial.thetar_radian),float(serial.thetal_radian),float(serial.hr)+0.0002,float(serial.hl)+0.0002)
#      print(area)
#

print(cal_area_2(find_a_x(np.deg2rad(59),np.deg2rad(94),0.000321,0.0001089,0.0002),find_a_y(np.deg2rad(59),np.deg2rad(94),0.000321,0.0001089,0.0002),0.000321,0.0001089,0.0002))