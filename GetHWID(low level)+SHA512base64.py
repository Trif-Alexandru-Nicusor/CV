import ftplib
import win32com.client
import hashlib
import base64
objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
objWBEMService = objWMIService.ConnectServer(".", "root\cimv2")
BiosItems = objWBEMService.ExecQuery("SELECT * FROM Win32_BIOS")
CSPItems = objWBEMService.ExecQuery("SELECT * FROM Win32_ComputerSystemProduct")
MacItems = objWBEMService.ExecQuery("Select * from Win32_NetworkAdapterConfiguration WHERE IPEnabled = True")
DDIDItems = objWBEMService.ExecQuery("SELECT * FROM Win32_DiskDrive")
GPUItems = objWBEMService.ExecQuery("SELECT * FROM Win32_VideoController")
LDIDItems = objWBEMService.ExecQuery("SELECT * FROM Win32_LogicalDisk")
RamItems = objWBEMService.ExecQuery("SELECT * FROM Win32_PhysicalMemory")
CPUItems = objWBEMService.ExecQuery("SELECT * FROM Win32_Processor")
OSItems = objWBEMService.ExecQuery("SELECT * FROM Win32_OperatingSystem")
for obj_item in BiosItems:
	bios1=obj_item.Manufacturer
	bios2=obj_item.Name
	bios3=obj_item.ReleaseDate
	bios4=obj_item.SerialNumber
	bios5=obj_item.Version
biosid=f"{bios1}{bios2}{bios3}{bios4}{bios5}"

for obj_item in CSPItems:
    uuid=obj_item.IdentifyingNumber
    uuid1=obj_item.Name
    uuid2=obj_item.UUID
    uuid3=obj_item.Version
    uuid4=obj_item.Vendor
cspid=f"{uuid}{uuid1}{uuid2}{uuid3}{uuid4}"

for obj_item in MacItems:
    mac=obj_item.MACAddress
macid=f"{mac}"

for obj_item in DDIDItems:
	ddid1=obj_item.SerialNumber
	ddid2=obj_item.PNPDeviceID
	ddid3=obj_item.Model
ddidid=f"{ddid1}{ddid2}{ddid3}"

for obj_item in GPUItems:
	gpuid1=obj_item.Name
	gpuid2=obj_item.PNPDeviceID
gpuid=f"{gpuid1}{gpuid2}"

ldid1=""
for obj_item in LDIDItems:
	if ldid1=="":
		ldid1=obj_item.VolumeSerialNumber
	else:
		ldid2=obj_item.VolumeSerialNumber
ldid=f"{ldid1}{ldid2}"

ramsid1=""
for obj_item in RamItems:
	if ramsid1=="":
		ramsid1=obj_item .SerialNumber
	else:
		ramsid2=obj_item .SerialNumber
		ramsid3=obj_item .PartNumber
ramid=f"{ramsid1}{ramsid2}{ramsid3}"

for obj_item in CPUItems:
	cpu1=obj_item.ProcessorId
	cpu2=obj_item.Name
cpuid=f"{cpu1}{cpu2}"

for obj_item in OSItems:
	ossn=obj_item.SerialNumber
	ossid=obj_item.InstallDate
osid=f"{ossn}{ossid}"

hwid=f"{biosid,cspid,macid,gpuid,ldid,ramid,cpuid,osid}"

def sha512_base64(hwid):
    hash = hashlib.sha512(hwid.encode('utf-8'))
    hash_digest = hash.digest()
    encoded_hash = base64.b64encode(hash_digest)
    return encoded_hash.decode('utf-8')

result = sha512_base64(hwid)
with open("HWID.txt", "w") as f:
    f.write(f"{result}(python)\n")

