"""An example library for converting temperatures."""


def convert_f_to_c(temperature_f):
    temperature_c = (temperature_f - 32) * (5/9)
    return temperature_c

def convert_c_to_f(temperature_c):
    temperature_f = (temperature_c * (9/5))+32
    return temperature_f

def convert_f_to_k(temperature_f):
    (temperature_f - 32)*(5/9)+273.15 = temperature_k
    return temperature_k

def convert_k_to_f(temperature_k):
    (temperature_k - 273.15)*(9/5)+32 = temperature_f
    return temperature_f
    
def convert_c_to_k(temperature_c):
    temperature_c + 273.15 = temperature_k
    return temperature_k

def convert_k_to_c(temperature_k):
    temperature_k - 273.15 = temperature_c
    return temperature_c
