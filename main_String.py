import numpy as np
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
DivisorCode=0x04C11DB7
PacketCode=0x705dcce4a1c800e04c362a9f08004500002cb26200004001ebb8c0a81a0c0101010108007e7264b7000012cfb5deee1d4d72821135d058700046
initialCode=0xFFFFFFFF
#--------------------------------------------

modules = CRC_String()

tmpPacket, packetSize = modules.changeTotal(PacketCode)
tmpDivisor, divisorSize = modules.changeTotal(DivisorCode)
tmpInitial, initialSize = modules.changeTotal(initialCode)

inputPacket = np.append(tmpPacket, tmpInitial, axis=0)

for i in range(0, packetSize):
    if(inputPacket[i]==True):
        result = np.logical_xor(inputPacket[i:(i+divisorSize)], tmpDivisor)
        inputPacket[i:(i+divisorSize)] = result
        print(inputPacket)
    #print(str(i+1) + "---while---")

result = inputPacket[packetSize:]
print("-----")
print(inputPacket[packetSize:])
print("-----")

inputPacket = np.append(tmpPacket, result, axis=0)

for i in range(0, packetSize):
    if(inputPacket[i]==True):
        result = np.logical_xor(inputPacket[i:(i+divisorSize)], tmpDivisor)
        inputPacket[i:(i+divisorSize)] = result
        print(inputPacket)
    #print(str(i+1) + "---while---")

print(inputPacket[packetSize:])
result = inputPacket[packetSize:]
print(tmpInitial)

if(np.array_equal(result, tmpInitial)):
    print("Is it correct!")
else:
    print("retry")