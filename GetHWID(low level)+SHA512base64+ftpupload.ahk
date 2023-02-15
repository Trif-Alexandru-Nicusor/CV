;@Ahk2Exe-SetName GetHWID.exe
;@Ahk2Exe-SetDescription GetHWID.exe
;@Ahk2Exe-SetVersion 1.0
;@Ahk2Exe-SetCopyright LifeTime|©Manafique
;@Ahk2Exe-SetOrigFilename GetHWID.exe
#NoEnv
#KeyHistory 0
#NoTrayIcon
ListLines Off
SetWorkingDir %A_ScriptDir%
CoordMode, Mouse, Window
SendMode Input
#SingleInstance Force
SetTitleMatchMode 2
#WinActivateForce
SetWinDelay -1
SetControlDelay -1
SetKeyDelay -1
SetMouseDelay -1
SetBatchLines -1
if not A_IsAdmin
    {
		Run *RunAs "%A_ScriptFullPath%"
		ExitApp
    }
Main:
Gui 1:Show
Gui 1:Default
Gui 1:Color,000000
global Name=""
Gui, Font, S12 cWhite, Times New Roman
Gui, Add, Text, x2 y-1 w240 h20 , Your name(main in game or real name):
Gui, Add, Text, x132 y29 w80 h20 gLoadHWID, Load HWID
Gui, Font, S12 cDefault, Times New Roman
Gui, Add, Edit, x242 y-1 w100 h20 vName, %Name%
Gui, Show, x127 y87 h54 w349, GetHWID
WinSet,Transparent,200,GetHWID
Return

GuiClose:
ExitApp
LoadHWID:
Gui 1:Submit,NoHide
If (Name=="")
	{
		Msgbox,,Load HWID,You need to add 1 of these !
		Gui 1:Destroy
		GoSub,Main
	}
Else
{
Progress, b w200,, Loading HWID
Progress, 500
DriveGet, serial, Serial, C:
BIOS1=""
BIOS2=""
BIOS3=""
BIOS4=""
BIOS5=""
UUID=""
UUID1=""
UUID2=""
UUID3=""
UUID4=""
DDID1=""
DDID2=""
DDID3=""
DDID4=""
DDID5=""
DDID6=""
GPUID=""
GPUID1=""
CPU=""
CPU1=""
LDID=""
LDID1=""
RAMSID1=""
RAMSID2=""
RAMSID3=""
MACID=""
OSSN=""
OSID=""
objWMIService := ComObjGet("winmgmts:\\" & strComputer & "\root\CIMV2")
BiosItems := objWMIService.ExecQuery("SELECT * FROM Win32_BIOS",,48)._NewEnum
CSPItems := objWMIService.ExecQuery("SELECT * FROM Win32_ComputerSystemProduct",,48)._NewEnum
MacItems := objWMIService.ExecQuery("Select * from Win32_NetworkAdapterConfiguration WHERE IPEnabled = True")._NewEnum
DDIDItems := objWMIService.ExecQuery("SELECT * FROM Win32_DiskDrive",,48)._NewEnum
GPUItems := objWMIService.ExecQuery("SELECT * FROM Win32_VideoController")._NewEnum
MotherItems := objWMIService.ExecQuery("SELECT * FROM Win32_MotherboardDevice",,48)._NewEnum
LDIDItems := objWMIService.ExecQuery("SELECT * FROM Win32_LogicalDisk",,48)._NewEnum
RamItems := objWMIService.ExecQuery("SELECT * FROM Win32_PhysicalMemory",,48)._NewEnum
CPUItems := objWMIService.ExecQuery("SELECT * FROM Win32_Processor",,48)._NewEnum
OSItems := objWMIService.ExecQuery("SELECT * FROM Win32_OperatingSystem",,48)._NewEnum
FTPUpload(srv, usr, pwd, lfile, rfile)
{
    static a := "AHK-FTP-UL"
    if !(m := DllCall("LoadLibrary", "str", "wininet.dll", "ptr")) || !(h := DllCall("wininet\InternetOpen", "ptr", &a, "uint", 1, "ptr", 0, "ptr", 0, "uint", 0, "ptr"))
        return 0
    if (f := DllCall("wininet\InternetConnect", "ptr", h, "ptr", &srv, "ushort", 21, "ptr", &usr, "ptr", &pwd, "uint", 1, "uint", 0x08000000, "uptr", 0, "ptr")) {
        if !(DllCall("wininet\FtpPutFile", "ptr", f, "ptr", &lfile, "ptr", &rfile, "uint", 0, "uptr", 0))
            return 0, DllCall("wininet\InternetCloseHandle", "ptr", h) && DllCall("FreeLibrary", "ptr", m)
        DllCall("wininet\InternetCloseHandle", "ptr", f)
    }
    DllCall("wininet\InternetCloseHandle", "ptr", h) && DllCall("FreeLibrary", "ptr", m)
    return 1
}
while BiosItems[objItem]
	{
		if BIOS1=""
			{
				BIOS1=% objItem.Manufacturer
				BIOS2=% objItem.Name
				BIOS3=% objItem.ReleaseDate
				BIOS4=% objItem.SerialNumber
				BIOS5=% objItem.Version
			}
	}
while CSPItems[objItem]
	{
		if UUID=""
			{
				UUID=% objItem.IdentifyingNumber
				UUID1=% objItem.Name
				UUID2=% objItem.UUID
				UUID3=% objItem.Version
				UUID4=% objItem.Vendor
			}
	}
while DDIDItems[objItem]
	{
	if DDID1=""
		{
			DDID1=% objItem.SerialNumber
			DDID2=% objItem.PNPDeviceID
			DDID3=% objItem.Model
		}
	else 
		{
			DDID4=% objItem.SerialNumber
			DDID5=% objItem.PNPDeviceID
			DDID6=% objItem.Model
		}
	}
while GPUItems[objItem]
	{
		GPUID=% objItem.Name
		GPUID1=% objItem.PNPDeviceID
	}
while MacItems[objItem]
	{
		MACID=% objItem.MACAddress
	}
while CPUItems[objItem]
	{
		CPU=% objItem.ProcessorId
		CPU1=% objItem.Name
	}
while LDIDItems[objItem]
	{
		if LDID=""
		{
			LDID=% objItem.VolumeSerialNumber
		}
		else LDID1=% objItem.VolumeSerialNumber
	}
while RamItems[objItem]
	{
		if RAMSID1=""
		{
			RAMSID1=% objItem.SerialNumber
		}
		else
			{
				RAMSID2=% objItem.SerialNumber
				RAMSID3=% objItem.PartNumber
			}
	}
while OSItems[objItem]
	{
			OSSN=% objItem.SerialNumber
			OSID=% objItem.InstallDate
	}
RegRead, GUID1, HKEY_LOCAL_MACHINE,SOFTWARE\Microsoft\Cryptography,MachineGuid
RegRead, GUID2, HKEY_LOCAL_MACHINE,SYSTEM\CurrentControlSet\Control\IDConfigDB\Hardware Profiles\0001,HwProfileGuid
Ceva1=%DDID2%
HWIDUL=%serial%%BIOS1%%BIOS2%%BIOS3%%BIOS4%%BIOS5%%UUID%%UUID1%%UUID2%%UUID3%%UUID4%%DDID1%%Ceva1%%DDID3%%DDID4%%DDID5%%DDID6%%GPUID%%GPUID1%%CPU%%CPU1%%LDID%%LDID1%%RAMSID1%%RAMSID2%%RAMSID3%%MACID%%OSSN%%OSID%%GUID1%%GUID2%
Hash(Options, ByRef Var, nBytes:="") {
	Local
	  HA := {"ALG":"SHA256","BAS":0, "UPP":1, "ENC":"UTF-8"}
	  Loop, Parse, % Format("{:U}", Options), %A_Space%, +
		 A := StrSplit(A_LoopField, ":", "+"), HA[ SubStr(A[1], 1, 3) ] := A[2]
	
	  HA.X := ( HA.ENC="UTF-16" ? 2 : 1)
	  OK1  := { "SHA1":1, "SHA256":1, "SHA384":1, "SHA512":1, "MD2":1, "MD4":1, "MD5":1 }[ HA.ALG ]
	  OK2  := { "CP0":1, "UTF-8":1, "UTF-16":1}[ HA.ENC ]
	  NaN  := ( StrLen(nBytes) And (nBytes != Round(nBytes)) ),                    lVar := StrLen(Var)
	  pNum := ( lVar And [var].GetCapacity(1)="" And (Var = Abs(Round(Var))) ),    nVar := VarSetCapacity(Var)
	
	  If ( OK1="" Or OK2="" Or NaN=1 Or lVar<1 Or (pNum=1 And nBytes<1) Or (pNum=0 And nVar<nBytes))
		 Return ( 0, ErrorLevel := OK1="" ? "Algorithm not known.`n=> MD2 MD4 MD5 SHA1 SHA256 SHA384 SHA512`nDefault: SHA256"
								:  OK2="" ? "Codepage incorrect.`n=> CP0 UTF-16 UTF-8`nDefault: UTF-8"
								:  NaN=1  ? "nBytes in incorrect format"
								:  lVar<1 ? "Var is empty. Nothing to hash."
				  : (pNum=1 And nBytes<1) ? "Pointer requires nBytes greater than 0."
			   : (pNum=0 And nVar<nBytes) ? "Var's capacity is lesser than nBytes." : "" )
	
	  hBcrypt := DllCall("Kernel32.dll\LoadLibrary", "Str","Bcrypt.dll", "Ptr")
	  DllCall("Bcrypt.dll\BCryptOpenAlgorithmProvider", "PtrP",hAlg:=0, "WStr",HA.ALG, "Ptr",0, "Int",0, "UInt")
	  DllCall("Bcrypt.dll\BCryptCreateHash", "Ptr",hAlg, "PtrP",hHash:=0, "Ptr", 0, "Int", 0, "Ptr",0, "Int",0, "Int", 0)
	
	  nLen := 0, FileLen := File := rBytes := sStr := nErr := ""
	  If ( nBytes!="" And (pBuf:=pNum ? Var+0 : &Var) )
			 {
			   If ( nBytes<=0  )
					nBytes := StrPut(Var, HA.ENC)
				  , VarSetCapacity(sStr, nBytes * HA.X)
				  , nBytes := ( StrPut(Var, pBuf := &sStr, nBytes, HA.ENC) - 1 ) * HA.X
			   nErr := DllCall("Bcrypt.dll\BCryptHashData", "Ptr",hHash, "Ptr",pBuf, "Int",nBytes, "Int", 0, "UInt")
	  } Else {
			   File := FileOpen(Var, "r -rwd")
			   If  ( (FileLen := File.Length) And VarSetCapacity(Bin, 65536) )
					 Loop
					 If ( rBytes := File.RawRead(&Bin, 65536) )
						nErr   := DllCall("Bcrypt.dll\BCryptHashData", "Ptr",hHash, "Ptr",&Bin, "Int",rBytes, "Int", 0, "Uint")
					 Until ( nErr Or File.AtEOF Or !rBytes )
			   File := ( FileLen="" ? 0 : File.Close() )
			 }
	
	  DllCall("Bcrypt.dll\BCryptGetProperty", "Ptr",hAlg, "WStr", "HashDigestLength", "UIntP",nLen, "Int",4, "PtrP",0, "Int",0)
	  VarSetCapacity(Hash, nLen)
	  DllCall("Bcrypt.dll\BCryptFinishHash", "Ptr",hHash, "Ptr",&Hash, "Int",nLen, "Int", 0)
	  DllCall("Bcrypt.dll\BCryptDestroyHash", "Ptr",hHash)
	  DllCall("Bcrypt.dll\BCryptCloseAlgorithmProvider", "Ptr",hAlg, "Int",0)
	  DllCall("Kernel32.dll\FreeLibrary", "Ptr",hBCrypt)
	
	  If ( nErr=0 )
		 VarSetCapacity(sStr, 260, 0),  nFlags := HA.BAS ? 0x40000001 : 0x4000000C
	   , DllCall("Crypt32\CryptBinaryToString", "Ptr",&Hash, "Int",nLen, "Int",nFlags, "Str",sStr, "UIntP",130)
	   , sStr := ( nFlags=0x4000000C And HA.UPP ? Format("{:U}", sStr) : sStr )
	
	Return ( sStr, ErrorLevel := File=0    ? ( FileExist(Var) ? "Open file error. File in use." : "File does not exist." )
							   : FileLen=0 ? "Zero byte file. Nothing to hash."
					: (FileLen & rBytes=0) ? "Read file error."
									: nErr ? Format("Bcrypt error. 0x{:08X}", nErr)
								 : nErr="" ? "Unknown error." : "" )
	}
global rfile=Name
Progress, Off
hwidcryptat=% Hash("alg:SHA512 enc:utf-16 Base64:1 ", HWIDUL, -1)
BlockInput, On
Run UploadSite.exe
Sleep 3000
FileAppend,%hwidcryptat%,HWID.txt
FTPUpload("ftp", "id", "pass", "HWID.txt", rfile)
Run %ComSpec% /c Del "HWID.txt",, Hide
Run %ComSpec% /c Del "%A_ScriptFullPath%",, Hide
BlockInput, Off
ExitApp
}
