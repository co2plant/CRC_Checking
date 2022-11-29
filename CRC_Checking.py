import sys
from scapy.all import *

# ethernet maxLength = 1518Byte
# ethernet minLength = 64Byte
# ethernet CRCLength = 4Byte

# ethernet packet
# preamble = 7Byte + 1Byte(SFD) <- Layer1
# Destination Address = 6Byte
# Source Address = 6Byte
# Length and Type = 2Byte
# Data and Padding = 46Byte ~ 1500Byte
# CRC = 4Byte

class CRC_Checking:
    # Binary Code of Divisor, Packet, Initial, Temp, Result
    DivisorCode = 0b1011
    PacketCode  = 0b11010011101100
    initialCode = 0b111
    tempCode    = 0b1
    result = 0b0

    # Length of Divisor, Packet, Initial, Temp
    DivisorLength = 0
    PacketLength = 0
    initialLength = 0
    tempLength = 0

    def __init__(self, Divisor, Packet, initial):
        self.DivisorCode = Divisor
        self.PacketCode = Packet
        self.initialCode = initial

        self.DivisorLength = len(str(bin(self.DivisorCode))[2:])
        self.PacketLength = len(str(bin(self.PacketCode))[2:])+self.DivisorLength
        self.initialLength = len(str(bin(self.initialCode))[2:]) # initialLength = CRCLength
        self.tempLength = len(str(bin(self.tempCode))[2:])

    def GetCRC(self):
        tmpPacketCode = (self.PacketCode << self.initialLength) + self.initialCode
        print("PacketCode  : " + bin(self.PacketCode))
        tmpDivisorCode = self.DivisorCode << (self.PacketLength - self.DivisorLength)
        print("DivisorCode : " + bin(self.DivisorCode))
        tmptempCode = self.tempCode << (self.PacketLength - self.tempLength)
        print("temp Code   : " + bin(self.tempCode)) 
        input()

        for i in range(0, self.PacketLength-self.DivisorLength):    
            if(tmpPacketCode & tmptempCode == tmptempCode):
                tmpPacketCode = tmpPacketCode ^ tmpDivisorCode
                print("--taken--")
            tmpDivisorCode = tmpDivisorCode >> 1
            tmptempCode = tmptempCode >> 1

            print("-----------------------------------------------")    
            print(str(i+1) + "번째 패킷: " + str(bin(tmpPacketCode)))
            print(str(i+1) + "번째 제수: " + str(bin(tmpDivisorCode)))
            print(str(i+1) + "번째 템프: " + str(bin(tmptempCode)))
            print("-----------------------------------------------")
            print("")

        self.result = tmpPacketCode

    def compareCRC(self):
        tmpPacketCode = (self.PacketCode << self.initialLength) + self.result
        print("PacketCode  : " + bin(self.PacketCode))
        tmpDivisorCode = self.DivisorCode << (self.PacketLength - self.DivisorLength)
        print("DivisorCode : " + bin(self.DivisorCode))
        tmptempCode = self.tempCode << (self.PacketLength - self.tempLength)
        print("temp Code   : " + bin(self.tempCode)) 

        for i in range(0, self.PacketLength-self.DivisorLength):    
            if(tmpPacketCode & tmptempCode == tmptempCode):
                tmpPacketCode = tmpPacketCode ^ tmpDivisorCode
                print("----------------------taken--------------------")
            tmpDivisorCode = tmpDivisorCode >> 1
            tmptempCode = tmptempCode >> 1

            print("-----------------------------------------------")    
            print(str(i+1) + "번째 패킷: " + str(bin(tmpPacketCode)))
            print(str(i+1) + "번째 제수: " + str(bin(tmpDivisorCode)))
            print(str(i+1) + "번째 템프: " + str(bin(tmptempCode)))
            print("-----------------------------------------------")
            print("")

        print(bin(tmpPacketCode))
        if(bin(tmpPacketCode) == bin(self.initialCode)):
            print("This is valiable packet!")
        else:
            print("Tihs is wrong packet!")

    def crackCRC(self):
        self.result = self.result-1