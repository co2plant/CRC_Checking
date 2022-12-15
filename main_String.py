import numpy as np
import csv
from CRC_String import CRC_String

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
 
# Binary Code of Divisor, Packet, Initial, Temp, Result

#----------------------------Initialize Field
DivisorCode=0x1DB7
PacketCode=0x474a18ac412905b4a18ce2718915fdf7
initialCode=0x0000
#--------------------------------------------

modules = CRC_String()
DivisorCode=input("제수를 입력해 주세요:")
PacketCode=input("페이로드를 입력해 주세요:")
initialCode=input("이니셜코드를 입력해 주세요:")

tmpPacket, packetSize = modules.changeTotal(PacketCode)
tmpDivisor, divisorSize = modules.changeTotal(DivisorCode)
tmpInitial, initialSize = modules.changeTotal(initialCode)

#패킷 뒤에 이니셜라이즈 코드를 붙여줌
inputPacket = np.append(tmpPacket, tmpInitial, axis=0)

for i in range(0, packetSize):
    if(inputPacket[i]==True):
        result = np.logical_xor(inputPacket[i:(i+divisorSize)], tmpDivisor)
        inputPacket[i:(i+divisorSize)] = result
        print(inputPacket)

result = inputPacket[packetSize:]
print("-----")
print(inputPacket[packetSize:])
print("-----")

tmpresult = ''.join(result.astype('int').astype('str'))
with open('./CRC_Checking/log.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['PACKET', 'DIVISOR', 'INITIAL', 'CRC'])
    csvwriter.writerow([''.join(tmpPacket.astype('int').astype('str')), ''.join(tmpDivisor.astype('int').astype('str')), ''.join(tmpInitial.astype('int').astype('str')), ''.join(result.astype('int').astype('str'))])
    csvwriter.writerow([])

option = input("페이로드를 재입력 하려면 0, 아니라면 1을 입력하세요.")
if(option=='0'):
    PacketCode=input("페이로드를 입력해 주세요:")
    tmpPacket, packetSize = modules.changeTotal(PacketCode)

#만들어진 CRC코드를 패킷 뒤에 붙여줌
inputPacket = np.append(tmpPacket, result, axis=0)

for i in range(0, packetSize):
    if(inputPacket[i]==True):
        result = np.logical_xor(inputPacket[i:(i+divisorSize)], tmpDivisor)
        inputPacket[i:(i+divisorSize)] = result
        print(inputPacket)

print(inputPacket[packetSize:])
result = inputPacket[packetSize:]
print(tmpInitial)

with open('./CRC_Checking/log.csv', 'a', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow([''.join(tmpPacket.astype('int').astype('str')), ''.join(tmpDivisor.astype('int').astype('str')), ''.join(tmpInitial.astype('int').astype('str')), ''.join(result.astype('int').astype('str'))])

if(np.array_equal(result, tmpInitial)):
    print("Is it correct!")
else:
    print("retry")