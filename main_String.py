import CRC_String

#----------------------------Initialize Field
divisorCode = 0x04C11DB7
packetData = 0x705dcce4a1c800e04c362a9f08004500002cb26200004001ebb8c0a81a0c0101010108007e7264b7000012cfb5deee1d4d72821135d058700046
initialCode = 0xFFFFFFF
#--------------------------------------------


# Binary Code of Divisor, Packet, Initial
modulesCRC = CRC_String.CRC_String(divisorCode, packetData, initialCode)


#modulesCRC.GetCRC()
#select = input("if you want crack packet input crack")
#if(select == 'crack'):
#    modulesCRC.crackCRC()
#modulesCRC.compareCRC()