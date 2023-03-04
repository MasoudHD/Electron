
E12 = (1, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2)
E24 = (1, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2, 2.2, 2.4, 2.7, 3, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1)


def calculate(data, resStandard):
    Voh = data[0]
    Vol = data[1]
    Vs = 0.0
    Vr = data[2]
    R2 = 10.0

    Vh = data[3]
    Vl = data[4]

    er = data[5]

    a = R2*(Voh-Vh)
    b = R2*(Vr-Vh)
    c = Vh+Vs
    d = R2*(Vol-Vl)
    e = R2*(Vr-Vl)
    f = Vl+Vs
    g = (b*f-c*e)
    h = (c*d-a*f) 
    R1dR3 = g/h
    R3 = (a*g+b*h)/(c*g)
    R1 = (g*R3)/h

    if resStandard == "E12":
        selList = list(E12)
    elif resStandard == "E24":
        selList = list(E24) 
    tempVlList = []
    tempVhList = []
    tempR123List = []
    tempR1 = []
    tempR2 = []
    tempR3 = []
    tempVh = []
    tempVl = []

    for i in range(0, 1000):
        tempR1.append(min(selList, key=lambda x:abs(x-(R1*(i+1)/100))))
        tempR2.append(min(selList, key=lambda x:abs(x-(R2*(i+1)/100))))
        tempR3.append(min(selList, key=lambda x:abs(x-(R3*(i+1)/100))))
        tempVh.append((Vr*tempR2[i]*tempR3[i]+Voh*tempR1[i]*tempR2[i]-Vs*tempR1[i]*tempR3[i])/(tempR1[i]*tempR2[i]+tempR1[i]*tempR3[i]+tempR2[i]*tempR3[i]))
        tempVl.append((Vr*tempR2[i]*tempR3[i]+Vol*tempR1[i]*tempR2[i]-Vs*tempR1[i]*tempR3[i])/(tempR1[i]*tempR2[i]+tempR1[i]*tempR3[i]+tempR2[i]*tempR3[i]))
        if [tempR1[i], tempR2[i], tempR3[i]] not in tempR123List:
            tempR123List.append([tempR1[i], tempR2[i], tempR3[i]])
            tempVhList.append(tempVh[i])
            tempVlList.append(tempVl[i])

    result = []
    for i in range(0, len(tempVhList)):
        if tempVhList[i]*(1-er)<=Vh<=tempVhList[i]*(1+er) and tempVlList[i]*(1-er)<=Vl<=tempVlList[i]*(1+er):
            rowData = []
            rowData.append("{:.2f}".format(tempVhList[i]))
            rowData.append("{:.2f}".format(tempVlList[i]))
            rowData.append("{:.2f}".format(tempR123List[i][0]))
            rowData.append("{:.2f}".format(tempR123List[i][1]))
            rowData.append("{:.2f}".format(tempR123List[i][2]))
            if rowData not in result:
                result.append(rowData)
    return result
