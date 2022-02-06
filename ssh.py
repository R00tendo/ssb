import paramiko
host = "127.0.0.1"
username = "kali"
password = "192.168"
sh = paramiko.SSHClient()
sh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sh.connect(host, 22, username, password)
sh.close()
print("Done")
