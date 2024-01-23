
import ctypes
import hashlib
import os
import json
import argparse

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
    
    def lock_check(self):
        en_val = 26
        ad_val = 12
        Result = self.lockcheck()
        return int(Result / en_val - ad_val)
    
    def lock_version(self):
        en_val = 15
        ad_val = 15
        Result = self.lockversion()
        return int(Result / en_val - ad_val);
    
    def lock_boot_cnt(self):
        en_val = 25
        ad_val = 1
        Result = self.lockbootcnt()
        return int(Result / en_val - ad_val)
    
    def lock_sn(self,op1):
        en_val = 19
        ad_val = 14
        op1 = (op1 + ad_val) * en_val
        Result = self.locksn(op1)
        return int(Result / en_val - ad_val)
    
    def lock_write(self,op1,op2):
        en_val = 31
        ad_val = 19
        op1 = (op1 + ad_val) * en_val
        op2 = (op2 + ad_val) * en_val
        Result = self.lockwrite(op1, op2)
        return int(Result / en_val - ad_val)
    
    def lock_read(self,op1):
        en_val = 21
        ad_val = 24
        op1 = (op1 + ad_val) * en_val
        Result = self.lockread(op1)
        return int(Result / en_val - ad_val)
    
    def lock_write_ex(self,op1,op2):
        en_val = 12
        ad_val = 19
        op1 = (op1 + ad_val) * en_val
        op2 = (op2 + ad_val) * en_val
        Result = self.lockwriteex(op1, op2)
        return int(Result / en_val - ad_val)
    
    def lock_read_ex(self,op1):
        en_val = 21
        ad_val = 24
        op1 = (op1 + ad_val) * en_val
        Result = self.lockreadex(op1)
        return int(Result / en_val - ad_val)
    
    def lock_check(self):
        en_val = 5
        ad_val = 10
        Result = self.lockcheck()
        return int(Result / en_val - ad_val)
    

if(__name__=="__main__"):
    usb = megalock()
    usb.lock_init_usb(8)
    for i in range (0,8):
        #write 1111
        usb.lock_write_ex(i, 1111)
        
    #read 1111
    for i in range (0,8):
        print(usb.lock_read_ex(i))