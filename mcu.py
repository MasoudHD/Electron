
def a2d(resolution = 8, Vref = 5, Offset = 0, Gain = 1, voltage = 0):
    voltage = (voltage-Offset)/Gain
    return (2**resolution)*voltage/Vref

def d2a(resolution = 8, Vref = 5, Offset = 0, Gain = 1, ADC = 0):
    return (((ADC*Vref)/(2**resolution))+Offset)*Gain

def resolution(resolution = 8, Vref = 5):
    return Vref/(2**resolution)

def timCalculator(frq, time, error):
    frq *= 1000000
    time /= 1000
    error /= 100
    values = []
    listCounter = []
    listPreScaler = []
    index = 0
    for ps in range(1, 65536):
        f = frq/ps
        if index > 0 and listCounter[index-1] == ps:
            break
        for c in range(0, 65536):
            if (time*(1-error)) < c/f < (time*(1+error)):
                value = []
                value.append(str(ps))
                value.append(str(c))
                values.append(value)
                listPreScaler.append(ps)
                listCounter.append(c)
                index += 1
    return values