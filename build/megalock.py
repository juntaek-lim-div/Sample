import os
import ctypes
import hashlib
import json

class megalock:
    def __init__(self):
        #mega64.dll이 있으면 로드, 없으면 이 파일이 있는 경로에서 로드
        if os.path.isfile('./mega64.dll'):
            self.lock_dll = ctypes.WinDLL('./mega64.dll')
        else:
            this_file_path = os.path.abspath(__file__)
            now_directory = os.path.dirname(this_file_path)
            dll_path = os.path.join(now_directory, 'mega64.dll')
            self.lock_dll = ctypes.WinDLL(dll_path)
        
        self.lockinitusb = self.lock_dll['lockinitusb']
        self.lockcheck = self.lock_dll['lockcheck']
        self.lockversion = self.lock_dll['lockversion']
        self.lockbootcnt = self.lock_dll['lockbootcnt']
        self.locksn = self.lock_dll['locksn']
        self.lockwrite = self.lock_dll['lockwrite']
        self.lockread = self.lock_dll['lockread']
        self.lockwriteex = self.lock_dll['lockwriteex']
        self.lockreadex = self.lock_dll['lockreadex']
        
    def lock_init_usb(self,op1):
        en_val=9
        ad_val=1
        op1 = (op1 + ad_val) * en_val
        Result = self.lockinitusb(op1)
        return int(Result / en_val - ad_val)
    
    def lock_read_ex(self,op1):
        en_val = 21
        ad_val = 24
        op1 = (op1 + ad_val) * en_val
        Result = self.lockreadex(op1)
        return int(Result / en_val - ad_val)
    
    def lock_sn(self,op1):
        en_val = 19
        ad_val = 14
        op1 = (op1 + ad_val) * en_val
        Result = self.locksn(op1)
        return int(Result / en_val - ad_val)
    
    def MD5fromFile(file_path):
        md5 = hashlib.md5()
        with open(file_path, 'rb') as f:
            file = f.read()
            md5.update(file)
        return md5.hexdigest() 
    
    def MD5fromString(string):
        md5 = hashlib.md5()
        md5.update(string.encode('utf-8'))
        return md5.hexdigest()
    
    def CameraModel(self):
        build_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(build_dir)
        if(self.lock_init_usb(8) != 34606):
            raise Exception("동일비전의 USB가 연결되어 있지 않습니다.")
        result_hex = ""
        for i in range(0, 4):
            result_hex += hex(self.lock_sn(i))[2:]
            
            
        exe_path = os.path.join(os.path.dirname(build_dir), 'main.exe')
        #exe_md5 = megalock.MD5fromFile(exe_path)
        exe_md5 = "c59af77dbbcad4c7e9a56061f8805c8a"
        serial_path = os.path.join(build_dir, 'serial.txt')
        key_md5=""
        serial=""
        
        
        with open(serial_path, 'r') as f:
            for line in f.readlines():
                    if(line.startswith("key=")):
                        #맨뒤 공백이 있으면 제거
                        key_md5 = line.strip()[4:]
                    else:
                        #나머지는 serial_md5
                        serial = serial + line.strip()
                        
        program_md5 = megalock.MD5fromString(exe_md5 + serial)
        
        #program_md5 ^ usb_md5
        xor = hex(int(program_md5, 16) ^ int(key_md5, 16))[2:]
        
        usb_hex = ""
        for i in range(0, 4):
            usb_hex += hex(self.lock_sn(i))[2:]
              
        usb_md5 = megalock.MD5fromString(usb_hex)
        
        if(usb_md5 != xor):
            raise Exception("USB키가 올바르지 않습니다.")
        else:
            return 203490
                    
            
        
        
  