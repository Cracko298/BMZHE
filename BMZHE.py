from time import sleep
from os import system
from os import path
# 47 Inkwood Ct. Unit A

error_cd = "Error Code: Dat_Not_Valid - 0x01"
err = "Error Code: Dat_Not_Opened - 0x0F"
ch0 = path.exists('Data0')  # OS.SYSTEM CHECKS FOR FILES.
ch1 = path.exists('Data1')
ch2 = path.exists('Data2')
ch3 = path.exists('Data6')
ch4 = path.exists('Data7')
ch5 = path.exists('Data8')

check_win = path.exists("C:\Windows\SysWOW64")
if check_win == True:
  clear = 'cls'
else:
  clear = 'clear'

def bmzCheck0():

  if ch0 == True:
    file0 = open("Data0", 'rb+')
    file0.seek(89)
    datacheck = file0.read(1)
    if datacheck >= b'\x00':
      file0.close()
    else:
      print("Data0 Is Not Valid or Has Not Been Opened.")
      print("Error Code: Dat_Not_Valid 0x0F")
      with open('Log.txt', 'a') as error_file:
        error_file.write(f'Data0 {err}\n')
      sleep(2)
      exit()


  if ch1 == True:
    file0 = open("Data1", 'rb+')
    file0.seek(89)
    datacheck = file0.read(1)
    if datacheck >= b'\x00':
      file0.close()
    else:
      print("Data1 Is Not Valid or Has Not Been Opened.")
      print("Error Code: Dat_Not_Valid 0x0F")
      with open('Log.txt', 'a') as error_file:
        error_file.write(f'Data1 {err}\n')
      sleep(2)
      exit()
    


  if ch2 == True:
    file0 = open("Data2", 'rb+')
    file0.seek(89)
    datacheck = file0.read(1)
    if datacheck >= b'\x00':
      file0.close()
    else:
      print("Data2 Is Not Valid or Has Not Been Opened.")
      print("Error Code: Dat_Not_Valid 0x0F")
      with open('Log.txt', 'a') as error_file:
        error_file.write(f'Data2 {err}\n')
      sleep(2)
      exit()
  


  if ch3 == True:
    file0 = open("Data6", 'rb+')
    file0.seek(89)
    datacheck = file0.read(1)
    if datacheck >= b'\x00':
      file0.close()
    else:
      print("Data6 Is Not Valid or Has Not Been Opened.")
      print("Error Code: Dat_Not_Valid 0x0F")
      with open('Log.txt', 'a') as error_file:
        error_file.write(f'Data6 {err}\n')
      sleep(2)
      exit()


  if ch4 == True:
    file0 = open("Data7", 'rb+')
    file0.seek(89)
    datacheck = file0.read(1)
    if datacheck >= b'\x00':
      file0.close()
    else:
      print("Data7 Is Not Valid or Has Not Been Opened.")
      print("Error Code: Dat_Not_Valid 0x0F")
      with open('Log.txt', 'a') as error_file:
        error_file.write(f'Data7 {err}\n')
      sleep(2)
      exit()


  if ch5 == True:
    file0 = open("Data8", 'rb+')
    file0.seek(89)
    datacheck = file0.read(1)
    if datacheck >= b'\x00':
      file0.close()
    else:
      print("Data8 Is Not Valid or Has Not Been Opened.")
      print("Error Code: Dat_Not_Opened 0x0F")
      with open('Log.txt', 'a') as error_file:
        error_file.write(f'Data8 {err}\n')
      sleep(2)
      exit()
  Health()


def HmrHealth():
  system(clear)
  print("WARNING: You Selected A Save-Data Editing Option!")
  print("This Function Will Edit All Save-Data Files Found In The Currect Directory.")
  input("Press 'Enter' To Continue. ")
  system(clear)
  print("This Program Only Accepts 4-Byte Answers (Or less).")
  print(" ")
  number = int(input("Enter An Integer for Health: "))
  byte_array = bytearray(number.to_bytes(4, byteorder='big'))
  reversed_array = byte_array[::-1]

  if ch0 == True:
    with open("Data0", 'rb+') as bin:
      print(f'Wrote {number} Into Health Sector of Data0.')
      sleep(1)
      bin.seek(100)
      bin.write(reversed_array)
      bin.seek(108)
      bin.write(reversed_array)

  if ch1 == True:
    with open("Data1", 'rb+') as bin:
      print(f'Wrote {number} Into Health Sector of Data1.')
      sleep(1)
      bin.seek(100)
      bin.write(reversed_array)
      bin.seek(108)
      bin.write(reversed_array)

  if ch2 == True:
    with open("Data2", 'rb+') as bin:
      print(f'Wrote {number} Into Health Sector of Data2.')
      sleep(1)
      bin.seek(100)
      bin.write(reversed_array)
      bin.seek(108)
      bin.write(reversed_array)
  sleep(2)
  Menu1()


def HmrEnergy():
  system(clear)
  print("WARNING: You Selected A Save-Data Editing Option!")
  print("This Function Will Edit All Save-Data Files Found In The Currect Directory.")
  input("Press 'Enter' To Continue. ")
  system(clear)
  print("This Program Only Accepts 4-Byte Answers (Or less).")
  print(" ")
  number = int(input("Enter An Integer for Energy: "))
  byte_array = bytearray(number.to_bytes(4, byteorder='big'))
  reversed_array = byte_array[::-1]

  if ch0 == True:
    with open("Data0", 'rb+') as bin:
      print(f'Wrote {number} Into Energy Sector of Data0.')
      sleep(1)
      bin.seek(104)
      bin.write(reversed_array)
      bin.seek(112)
      bin.write(reversed_array)

  if ch1 == True:
    with open("Data1", 'rb+') as bin:
      print(f'Wrote {number} Into Energy Sector of Data1.')
      sleep(1)
      bin.seek(104)
      bin.write(reversed_array)
      bin.seek(112)
      bin.write(reversed_array)

  if ch2 == True:
    with open("Data2", 'rb+') as bin:
      print(f'Wrote {number} Into Energy Sector of Data2.')
      sleep(1)
      bin.seek(104)
      bin.write(reversed_array)
      bin.seek(112)
      bin.write(reversed_array)
      
  sleep(2)
  Menu1()


















def Health():  # Not Finished Yet...
  system(clear)
  print("WARNING: You Selected A Save-Data Editing Option!")
  print("This Function Will Edit All Save-Data Files Found In The Currect Directory.")
  input("Press 'Enter' To Continue. ")
  system(clear)
  print("This Program Only Accepts 4-Byte Answers (Or less).")
  print(" ")
  number = int(input("Enter An Integer for Health: "))
  byte_array = bytearray(number.to_bytes(4, byteorder='big'))
  reversed_array = byte_array[::-1]

  if ch0 == True:
    with open("Data0", 'rb+') as bin:
      print(f'Wrote {number} Into Health Sector of Data0.')
      sleep(1)
      bin.seek(88)
      bin.write(reversed_array)

  if ch1 == True:
    with open("Data1", 'rb+') as bin:
      print(f'Wrote {number} Into Health Sector of Data1.')
      sleep(1)
      bin.seek(88)
      bin.write(reversed_array)

  if ch2 == True:
    with open("Data2", 'rb+') as bin:
      print(f'Wrote {number} Into Health Sector of Data2.')
      sleep(1)
      bin.seek(88)
      bin.write(reversed_array)

  if ch3 == True:
    with open("Data6", 'rb+') as bin:
      print(f'Wrote {number} Into Health Sector of Data6.')
      sleep(1)
      bin.seek(88)
      bin.write(reversed_array)

  if ch4 == True:
    with open("Data7", 'rb+') as bin:
      print(f'Wrote {number} Into Health Sector of Data7.')
      sleep(1)
      bin.seek(88)
      bin.write(reversed_array)

  if ch5 == True:
    with open("Data8", 'rb+') as bin:
      print(f'Wrote {number} Into Health Sector of Data8.')
      bin.seek(88)
      bin.write(reversed_array)

  sleep(3)
  Menu0()

def MaxLevel():
  system(clear)
  print("WARNING: You Selected A Save-Data Editing Option!")
  print("This Function Will Edit All Save-Data Files Found In The Currect Directory.")
  input("Press 'Enter' To Continue. ")
  system(clear)
  print("This Program Only Accepts 4-Byte Answers (Or less).")
  print(" ")
  number = int(input("Enter An Integer for Level: "))
  byte_array = bytearray(number.to_bytes(4, byteorder='big'))
  reversed_array = byte_array[::-1]

  if ch0 == True:
    with open("Data0", 'rb+') as bin:
      print(f'Wrote {number} Into Level Sector of Data0.')
      sleep(1)
      bin.seek(16)
      bin.write(reversed_array)

  if ch1 == True:
    with open("Data1", 'rb+') as bin:
      print(f'Wrote {number} Into Level Sector of Data1.')
      sleep(1)
      bin.seek(16)
      bin.write(reversed_array)

  if ch2 == True:
    with open("Data2", 'rb+') as bin:
      print(f'Wrote {number} Into Level Sector of Data2.')
      sleep(1)
      bin.seek(16)
      bin.write(reversed_array)
  sleep(2)
  Menu1()


























def Menu1():
  system(clear)
  simplist = [0, 1, 2, 3]
  print("The Magic Hammer Stats Editor (BMZHE)")
  print(" ")
  print("1 = Edit Max Health")
  print("2 = Edit Max Energy")
  print("3 = Edit Max Level")
  print(" ")
  print("0 = Return To Menu")
  print(" ")
  useri = int(input("Enter Choice: "))
  if useri not in simplist:
    Menu1()

  if useri == 1:
    HmrHealth()

  if useri == 0:
    Menu0()
  
  if useri == 2:
    HmrEnergy()

  if useri == 3:
    MaxLevel()


























def Menu0():
  system(clear)
  simplist = [0, 1, 2, 3]
  print("(BMZHE) BattleMinerZ Health Editor (v1.3)")
  print(" ")
  print("1 = Edit 'BattleMinerZ' Health")
  print(" ")
  print("2 = Edit 'BattleMiner' Health")
  print("3 = Edit 'The Magic Hammer' Health/Stats")
  print("0 = Exit Application")
  print(" ")
  useri = int(input("Enter Choice: "))
  if useri not in simplist:
    Menu0()

  if useri == 1:
    bmzCheck0()

  if useri == 0:
    exit()

  if useri == 3:
    Menu1()
  
  if useri == 2:
    system(clear)
    print("This Hasn't Been Developed as of Yet.")
    print("BattleMiner has a Confusing Save-Data Layout. So it might take a little while.")
    print(" ")
    sleep(4)
    Menu0()


def Load():
  sleep(1)
  print("Created By:  r       ")
  sleep(0.125)
  system(clear)
  print("Created By:  r c     ")
  sleep(0.125)
  system(clear)
  print("Created By: Cr c     ")
  sleep(0.125)
  system(clear)
  print("Created By: Cr c    8")
  sleep(0.125)
  system(clear)
  print("Created By: Cr c  2 8")
  sleep(0.125)
  system(clear)
  print("Created By: Crac  2 8")
  sleep(0.125)
  system(clear)
  print("Created By: Crac o2 8")
  sleep(0.125)
  system(clear)
  print("Created By: Crac o298")
  sleep(0.125)
  system(clear)
  print("Created By: Cracko298 ")
  sleep(2)
  system(clear)
  Menu0()





if ch0 == False or ch1 == False or ch2 == False or ch3 == False or ch4 == False or ch5 == False:
  if ch1 == True:
    system(clear)
    Load()
  if ch2 == True:
    system(clear)
    Load()
  if ch3 == True:
    system(clear)
    Load()
  if ch4 == True:
    system(clear)
    Load()
  if ch5 == True:
    system(clear)
    Load()

if ch0 == False:
  print("Data0 Not Found - Slot #1 - Singleplayer Adventure.")
  sleep(0.5)
  if ch1 == False:
    print("Data1 Not Found - Slot #2 - Singleplayer Adventure.")
    sleep(0.5)
    if ch2 == False:
      print("Data2 Not Found - Slot #3 - Singleplayer Adventure.")
      sleep(0.5)
      print(" ")
      if ch3 == False:
        print("Data6 Not Found - Slot #1 - Multiplayer Adventure.")
        sleep(0.5)
        if ch4 == False:
          print("Data7 Not Found - Slot #2 - Multiplayer Adventure.")
          sleep(0.5)
          if ch5 == False:
            print("Data8 Not Found - Slot #3 - Multiplayer Adventure.")
            sleep(0.5)
            print(" ")
            print("NOTICE: No Save-Data Was Found In Current Directory!")
            sleep(0.5)
            print("The Application Is Useless Unless Provided With Save-Data.")
            sleep(5)
            print(" ")
            print("Error Code: Dat_Not_Found 0x01")
            with open('Log.txt', 'a') as error_file:
              error_file.write(f'Save-Data {error_cd}\n')
            print("The Application Will Now Close...")
            sleep(2)
            exit()
            
print("Starting Application...")
sleep(3)
system(clear)
Load()
