
def a2d(resolution = 8, Vref = 5, Offset = 0, Gain = 1, voltage = 0):
    voltage = (voltage-Offset)/Gain
    return (2**resolution)*voltage/Vref

def d2a(resolution = 8, Vref = 5, Offset = 0, Gain = 1, ADC = 0):
    return (((ADC*Vref)/(2**resolution))+Offset)*Gain

def resolution(resolution = 8, Vref = 5):
    return Vref/(2**resolution)