from pymem import Pymem
import pymem.process as process
from os import _exit as exitfunc
import warnings
def DisDeprecation():
    warnings.simplefilter("ignore", DeprecationWarning)
def GetRDR2Process():
    try:
        return Pymem("RDR2.exe")
    except:
        print("Not Founded RDR2.exe")
        exitfunc(3321)

def GetRDR2_ProcessHandle():
    process_handle_rdr2 = GetRDR2Process().process_handle
    return process_handle_rdr2

def Inject(nameofdll : str):
    rdr2_exe = GetRDR2Process()
    if(rdr2_exe.base_address == 0):
        print("Not Founded Base Address of RDR2.exe")
    DisDeprecation()
    process.inject_dll(GetRDR2_ProcessHandle(), bytes(nameofdll, "utf-8"))

def Main():
    dllpath = input("Please Write You're DLL Path: ")
    Inject(dllpath)

if __name__ == "__main__":
    Main()
