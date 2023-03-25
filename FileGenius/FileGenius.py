import os
import shutil
import datetime
import pyAesCrypt



class FileGenius():
    
    
    def CreateFile(way, expansion, text): 
        try:
            expansion = expansion.split('.')

            file = open(str(way) + '.' + str(expansion[1]), 'w', encoding='utf-8')
            file.write(str(text)) 
            file.close()
        except IndexError:

            file = open(str(way) + '.' + str(expansion[0]), 'w', encoding='utf-8')
            file.write(str(text)) 
            file.close()
        
    def ReadFile(way, expansion, type):
        try:
            if type == '0' or type == 0:
                expansion = expansion.split('.')
            
                file = open(str(way) + '.' + str(expansion[1]), 'r', encoding='utf-8')
                print(file.read())
                file.close()
            else:
                expansion = expansion.split('.')
            
                file = open(str(way) + '.' + str(expansion[0]), 'r', encoding='utf-8')
                stat = os.stat(str(way) + '.' + str(expansion[0]))
                print("Bytes: " + str(stat.st_size))
                print("MegaBytes: " + str(stat.st_size /(1024 * 1024)))
                print(file.read())    
                file.close()
        except IndexError:
            if type == '0' or type == 0:
            
                file = open(str(way) + '.' + str(expansion), 'r', encoding='utf-8')
                print(file.read())
                file.close()
            else:
                expansion = expansion.split('.')
            
                file = open(str(way) + '.' + str(expansion[0]), 'r', encoding='utf-8')
                stat = os.stat(str(way) + '.' + str(expansion[0]))
                print("Bytes: " + str(stat.st_size))
                print("MegaBytes: " + str(stat.st_size /(1024 * 1024)))
                print(file.read())    
                file.close()
                
    def EncryptFile(way, expansion, password):
        try:
            expansion = expansion.split('.')
            
            buffer = 512 * 1024

            pyAesCrypt.encryptFile(str(way) + '.' + str(expansion[1]), str(way) + '.fg', password, buffer)
        except IndexError:
            buffer = 512 * 1024

            pyAesCrypt.encryptFile(str(way) + '.' + str(expansion[0]), str(way) + '.fg', password, buffer)
            
    def DecryptFile(way, expansion, password):
        try:
            expansion = expansion.split('.')
        
            buffer = 512 * 1024

            pyAesCrypt.decryptFile(str(way) + '.' + str(expansion[1]), str(way) + '.txt', password, buffer)
        except IndexError:
            buffer = 512 * 1024

            pyAesCrypt.decryptFile(str(way) + '.' + str(expansion[0]), str(way) + '.txt', password, buffer)

    def DeleteFile(way, expansion):
        try:
            expansion = expansion.split('.')
            
            os.remove(str(way) + "." + str(expansion[1]))
        except IndexError:     
            os.remove(str(way) + "." + str(expansion[0]))
            
    def InformationFile(way, expansion):
        try:
            expansion = expansion.split('.')
            
            stat = os.stat(str(way) + '.' + str(expansion[0]))

            information = {
                'Bytes': str(stat.st_size),
                'MegaBytes': str(stat.st_size /(1024 * 1024)),
                'Time': str(datetime.datetime.fromtimestamp(stat.st_ctime))
            }
            
            return information
        except IndexError:
            expansion = expansion.split('.')
            
            stat = os.stat(str(way) + '.' + str(expansion[0]))

            information = {
                'Bytes': str(stat.st_size),
                'MegaBytes': str(stat.st_size /(1024 * 1024)),
                'Time': str(datetime.datetime.fromtimestamp(stat.st_ctime))
            }
            
            return information
    
    def CopyFile(wat, expansion, name):
        try:
            expansion = expansion.split('.')
        
            shutil.copy(str(wat) + '.' + str(expansion[1]), str(name) + '.' + str(expansion[1]))
        except IndexError: 
            shutil.copy(str(wat) + '.' + str(expansion[0]), str(name) + '.' + str(expansion[0]))
    
