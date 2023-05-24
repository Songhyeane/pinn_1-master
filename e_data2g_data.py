import math
import numpy as np
import pandas
import pandas as pd


def convert_data(data_path):
    f = open(data_path)
    convert_data,resurt_data=[],[]
    while True:
        line = f.readline()
        if not line : break
        convert_datas = line

    convert_datas = convert_datas.split(' ')

    for data in convert_datas:
        convert_data = 0.0
        data1 = '0.'
        data2 = '0.'

        if data == '':
            continue
        if float(data) == 0.0 :
            resurt_data.append(0.0)
            continue

        if data[0] == '-':
            time = data[1]
            flag = True
            for chr in data[3:]:
                if chr == 'e' :
                    flag = False

                if flag :
                    data1 += chr
                    data2 += '0'
                else:
                    data1 += chr
                    data2 += chr

            data2 = list(data2)
            data2[0] = '1'
            data2 = ''.join(data2)

            data1 = '-' + data1
            data2 = '-' + data2

        else :
            time = data[0]
            flag = True
            for chr in data[2:]:
                if chr == 'e' :
                    flag = False
                if flag:
                    data1 += chr
                    data2 += '0'
                else:
                    data1 += chr
                    data2 += chr

            data2 = list(data2)
            data2[0] = '1'
            data2 = ''.join(data2)

        #print(f'data:{data} ,data1:{data1} ,data2:{data2} ,time:{time}')

        #print()

        #print(f'data:{data} ,f_data1:{float(data1)} ,f_data2:{float(data2)} ,time:{time}')

        #print()

        convert_data = float(data1) + float(time)*float(data2)
        convert_data = '{:.10f}'.format(convert_data)

        resurt_data.append(convert_data)

    return resurt_data

def radian_to_defgree(data_list):
    result = []
    for data in data_list:
        print(data)
        angle_deg = math.degrees(float(data))
        result.append(angle_deg)

    return result

def save_data(data_path,result_list):
    f = open(data_path,'w')
    for data in result_list :
        f.write(str(data)+'\n')
    f.close()

def make_list(data_path):
    f = open(data_path,'r')
    list = []
    while True :
        line = f.readline()
        if not line:
            break
        list.append(line[:-1])

    f.close()

    return list

result_list=convert_data('C:/research/workspace/pinn_1-master/data/input/test')
save_data('C:/research/workspace/pinn_1-master/data/input/a.txt',result_list)

