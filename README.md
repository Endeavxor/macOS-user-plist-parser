# macOS user plist parser
Small tool allowing to extract some user data *(password hash, etc ...)* from the user's binary Plist file

# Requirements 
- Python 3

# I. How it works
## Retrieve the file containing the information of the desired user

```bash
# Where uSeRnAmE is one of the mac accounts
cp /private/var/db/dslocal/nodes/Default/users/uSeRnAmE.plist .
```
## Download and execute the script 
```bash
git clone https://github.com/Endeavxor/macOS-user-plist-parser.git
cd macOS-user-plist-parser
python3 macOS_user_plist_parser.py ../uSeRnAmE.plist --hash
```
## List of options :
- --hash : Extracts user's session password information
- --user-info : Extracts the basic user information *(name, home dir,...)*
- --all : Extracts everything above

*Note : There are others information contained in the uSeRnAmE.plist file, if I perceive the need to extract it in the future it will be added, or don't hesitate to ask me*

# II. Hashcat :
In case the account password information has been extracted, you can try to break it with Hashcat *(however, don't waste too much time, it can be very slow because of the algorithm used)*

```bash
hashcat --username -m 7100 hashThatYouHaveFound.txt bruteforcelist.txt
```
