import sys
import numpy as np

class CRC_String():

    def __init__(self):
        print("Start")

    #input type Integer
    #return type numpy array String
    def changeToStr(inputCode):
        result = str(bin(inputCode))[2:]
        result = np.array(list(result))
        print(result)
        print(result.size)
        return result

    #input type String
    #return type Integer
    def countCodeSize(inputCode):
        result = inputCode.size
        print(result)
        return result

    #input type numpy array input
    #return type numpy array boolean
    def changeToBool(inputCode):
        result = inputCode.astype('bool')
        print(result)
        return result

    #this function is simple code for main
    def changeTotal(self, inputCode):
        result = str(bin(inputCode))[2:]
        result = np.array(list(result))
        resultsize = result.size
        result = result.astype('bool')

        return result, resultsize