import csv
import math
import numpy as np
def calculate(in_type,in_price,in_gender,in_distance):
    list = []
    type = ["พัดลม", "แอร์", "สูท"]
    gender = ["ชาย", "หญิง", "รวม"]
    # ["","type", "price", "gender", "", "distance", "",""]
    # in_type = input("Enter room type(" + ",".join(type) + "): ")
    # in_price = input("Enter price(0-12000): ")
    # in_gender = input("Enter gender(" + ",".join(gender) + "): ")
    # in_distance = input("Enter distance(0-2500m): ")
    user = ["", in_type, in_price, in_gender, "", in_distance]
    col_price = []
    col_dis = []
    col_size = []

    with open('1234.csv', 'r', encoding="utf8") as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            if row != []:
                e = row[0].split(",")
                col_dis.append(float(int(e[5]) / 100))
                col_price.append(float(int(e[2]) / 100))
                col_size.append(float(int(e[7])))
                if e[1] == user[1] or user[1] == "":
                    if e[3] == user[3] or user[3] == "":
                        if e[4] == user[4] or user[4] == "":
                            list.append(e)
    if (list == []): print("No data")
    data = []
    typeIndex = type.index(user[1]) if user[1] in type else 1
    price = float(int(user[2]) / 1000) if user[2].isdigit else 3000
    genderIndex = gender.index(user[3]) if user[3] in gender else 2
    distance = float(int(user[5]) / 1000) if user[5].isdigit else 0

    col_dis.append(distance*10)
    col_price.append(price*10)
    col_size.append(50 if user[1] == "สูท" else 30)
    x = np.array([typeIndex, price, genderIndex, distance])
    max = -1

    for item in list:
        y = np.array([type.index(item[1]), float(int(item[2]) / 1000), gender.index(item[3]), float(int(item[5]) / 1000)])
        r = np.corrcoef(x, y)[0][1]

        if r > max:
            max = r
            data = [[item, r]]
        elif r == max:
            data.append([item, r])

    # col = np.array([col_dis,col_price,col_size])
    return data
    # print(np.cov([col_dis, col_price, col_size]))