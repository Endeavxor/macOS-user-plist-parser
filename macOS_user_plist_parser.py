import plistlib
import sys

"""
@author : Endeavxor
"""
def getHint(plistInfos):
	return plistInfos["hint"][0]
	
def getUsername(plistInfos):
	return plistInfos["name"][0]
	
def parUserAccountInfos(plistInfos):
	username = getUsername(plistInfos)
	passwordHint = getHint(plistInfos)
	shell = plistInfos["shell"][0]
	home = plistInfos["home"][0]
	uid = plistInfos["uid"][0]
	gid = plistInfos["gid"][0]
	print(f"\tUsername : {username}\n\tHome Directory : {home}\n\tPassword Hint : {passwordHint}\n\tUID : {uid}\n\tGID : {gid}\n\tShell : {shell}")

def parseUserAccountHash(plistInfos):
	plistShadowHashData = plistlib.loads(plistInfos["ShadowHashData"][0])
	sha512HashInfos = plistShadowHashData["SALTED-SHA512-PBKDF2"]
	
	iterations = sha512HashInfos["iterations"]
	salt = sha512HashInfos["salt"].hex()
	entropy = sha512HashInfos["entropy"][:64].hex()
	username = getUsername(plistInfos)
	
	print(f"\tIterations : {iterations}\n\tSalt : {salt}\n\tEntropy : {entropy}\n\tHashcat : {username}:$ml${iterations}${salt}${entropy}")

def getHandleToPlist(pathToPlist):
	with open(pathToPlist,"rb") as plist:
		plistInfos = plistlib.load(plist)
	return plistInfos
	
if len(sys.argv) < 3:
	print(f"Usage : python3 {sys.argv[0]} username.plist [--hash | --user-info | --all]")
else:
	plistInfos = getHandleToPlist(sys.argv[1])
	for arg in sys.argv[2:]:
		if arg in ("--hash","--all"):
			print("\n[+] Hash Infos :")
			parseUserAccountHash(plistInfos)
			print("_"*30)
		if arg in ("--user-info","--all"):
			print("\n[+] User Infos :")
			parUserAccountInfos(plistInfos)
			print("_"*30)
