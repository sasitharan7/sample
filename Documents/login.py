from pexpect import pxssh
import getpass
try:
	s = pxssh.pxssh()
	hostname = '172.31.6.68' 
	username = 'sasi'
	password = 'Sfish123'
	s.login(hostname,username,password)
	s.sendline('uptime;df -h;free -m')
	s.prompt()
	print (s.before)
	s.sendline('ls -alrt')
	s.prompt()
	print(s.before)
	s.logout()
except :
	print("LOGIN FAILED")
