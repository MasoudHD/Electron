
def a2d(resolution = 8, Vref = 5, Offset = 0, Gain = 1, voltage = 0):
    voltage = (voltage-Offset)/Gain
    return (2**resolution)*voltage/Vref

def d2a(resolution = 8, Vref = 5, Offset = 0, Gain = 1, ADC = 0):
    return (((ADC*Vref)/(2**resolution))+Offset)*Gain

def resolution(resolution = 8, Vref = 5):
    return Vref/(2**resolution)

def timCalculator(frq, time, error, frqUnit, timeUnit):
    error /= 100
    
    if frqUnit == "KHz":
        frq *= 1E+3  
    elif frqUnit == "MHz":
        frq *= 1E+6 

    if timeUnit == "ms":
        time *= 1E-3  
    elif timeUnit == "us":
        time *= 1E-6
    elif timeUnit == "ns":
        time *= 1E-9    
    
    values = []
    for ps in range(1, 65536):
        f = frq/ps
        if len(values) > 0 and int(values[-1][1]) == ps:
            break
        for c in range(0, 65536):
            if (time*(1-error)) < c/f < (time*(1+error)):
                value = []
                value.append(str(ps))
                value.append(str(c))
                values.append(value)
    return values