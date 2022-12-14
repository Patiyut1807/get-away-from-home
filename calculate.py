import csv
import pandas as pd
import numpy as np


def calculate(in_type, in_price, in_gender, in_distance):
    list = []
    type = ["พัดลม", "แอร์", "สูท"]
    gender = ["ชาย", "หญิง", "รวม"]
    user = ["", in_type, in_price, in_gender, "", in_distance]

    with open('1234.csv', 'r', encoding="utf8") as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            if row != []:
                e = row[0].split(",")
                if e[1] == user[1] or user[1] == "":
                    if e[3] == user[3] or user[3] == "":
                        if e[4] == user[4] or user[4] == "":
                            list.append(e)
    if (list == []):
        print("No data")
    data = []
    typeIndex = type.index(user[1]) if user[1] in type else 1
    price = float(int(user[2]) / 1000) if user[2].isdigit else 3000
    genderIndex = gender.index(user[3]) if user[3] in gender else 2
    distance = float(int(user[5]) / 1000) if user[5].isdigit else 0
    x = np.array([typeIndex, price, genderIndex, distance])
    max = -1

    # วน loop ในข้อมูลหอ(list คือ list ของข้อมูลหอ)
    for item in list:
        y = np.array([type.index(item[1]), float(int(item[2]) / 1000), gender.index(item[3]), float(int(item[5]) / 1000)])

        # คำนวณค่า Pearson โดยเปรียบเทียบข้อมูลผู้ใช้(x) กับข้อมูลของหอ(y)
        r = np.corrcoef(x, y)[0][1]

        # เปรียบเทียบหาหอที่มีค่า Pearson มากที่สุด
        if r > max:
            max = r
            data = [[item, r]]
        elif r == max:
            data.append([item, r])

    # รับค่า Vector ผู้ใช้ลง MatrixData
    matrixData = [[typeIndex, price, genderIndex, distance]]

    # รับค่า Vector ข้อมูลของหอทุกหอพักลงใน MatrixData
    for i in range(len(list)):
        matrixData.append([type.index(list[i][1]), float(int(list[i][2])/1000), gender.index(list[i][3]), float(int(list[i][5])/1000)])

    # สร้าง Correlation Matrix
    arrayData = np.array(matrixData)
    corrMatrix = np.corrcoef(arrayData)

    # ใส่ string "ผู้ใช้" เข้าไปที่ index 0 ของ list เพื่อนำไปตั้งชื่อ column ใน dataframe
    list.insert(0, ["ผู้ใช้"])

    # ใส่เลขกำกับ column หน้าชื่อหอทุกหอ เพื่อไม่ให้เกิด ValueError เพราะชื่อหอซ้ำ
    for i in range(len(list)):
        list[i][0] = "{} ".format(i) + list[i][0]
    corrDF = pd.DataFrame(corrMatrix, columns=['%s' % list[i][0] for i in range(len(list))])

    return data, corrDF


