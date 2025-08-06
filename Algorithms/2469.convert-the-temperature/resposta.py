class Solution(object):
    def convertTemperature(self, celsius):
        resposta = []
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        resposta.append(kelvin)
        resposta.append(fahrenheit)
        return resposta