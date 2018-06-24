m_values = ['mm', 'cm', 'm', 'km']
i_values = ["ml", "yd", "ft", "in"]
i_conver = [1760, 3, 12]

mass_m_values = ["mg", "g", "kg", "t"]
mass_i_values = ["t", "lb", "oz"]
mass_i_conver = [2204.62, 16]

def m_to_i(measure, symbol, conversion):
    index = m_values.index(symbol)
    measure *= (100**(index)) #convert to milimiters
    measure /= 25.4 #convert to inches

    #convert to requested imperial
    index = i_values.index(conversion)
    for value in i_conver[index:]:
        measure /= value

    return measure

def i_to_m(measure, symbol, conversion):
    index = i_values.index(symbol)
    for value in i_conver[index:]:
        measure *= value

    measure *= 25.4 # converter to milimiters
    index = m_values.index(conversion)
    measure /= (100**(index))#convert to requested metric

    return measure

def temp(f=None, c=None):
    if c:
        return c * 9/5 + 32

    if f:
        return (f - 32) * 5/9

def mass_i_to_m(measure, symbol, conversion):
    #convert to oz
    index = mass_i_values.index(symbol)
    for value in mass_i_conver[index:]:
        measure = measure * value

    measure = measure * 28349.5 #convert to miligrams
    index = mass_m_values.index(conversion)
    measure /= (100**(index+1)) #convert to requested imperial

    return measure

def mass_m_to_i(measure, symbol, conversion):
    index = mass_m_values.index(symbol)
    measure *= (100**(index+1)) # convert to miligrams
    measure = measure / 28349.5 #convert to oz

    #convert to requested imperial
    index = mass_i_values.index(conversion)
    for value in mass_i_conver[index:]:
        measure = measure / value

    return measure

def convert(value, symbol, conversion):
    value = int(value)
    if symbol in m_values and conversion in i_values:
        measure = m_to_i(value, symbol, conversion)
    elif symbol in i_values and conversion in m_values:
        measure = i_to_m(value, symbol, conversion)
    elif symbol in mass_m_values and conversion in mass_i_values:
        measure = mass_m_to_i(value, symbol, conversion)
    elif symbol in mass_i_values and conversion in mass_m_values:
        measure = mass_i_to_m(value, symbol, conversion)
    elif symbol == 'c':
        measure = temp(c=value)
    elif symbol == 'f':
        measure = temp(f=value)
    else:
        msg = "Not a convertible symbol. \nImperial length unit symbols: {}\nImperial weight/mass unit symbols: {}\nMetric length unit symbols: {}\nMetric weight/mass unit symbols: {}\nTemperature unit symbols: c - f"
        return msg.format(" - ".join(i_values), " - ".join(mass_i_values), " - ".join(m_values), " - ".join(mass_m_values))

    return measure
