import socket, sys
import ipaddress


top_20_port = [21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1723,3306,3389,5900,8080]
top_100_port = [1, 3, 7, 9, 13, 17, 19, 21, 22, 23, 25, 26, 37, 53, 79, 80, 81, 82, 88, 100, 106, 110, 111, 113, 119, 135, 139, 143, 144, 179, 199, 254, 255, 280, 311, 389, 427, 443, 444, 445, 464, 465, 497, 513, 514, 515, 543, 544, 548, 554, 587, 593, 625, 631, 636, 646, 787, 808, 873, 902, 990, 993, 995, 1000, 1022, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1044, 1048, 1049, 1050, 1053, 1054, 1056, 1058, 1059, 1064, 1065, 1066, 1069, 1071, 1074, 1080, 1110, 1234]
top_200_port = [1, 3, 7, 9, 13, 17, 19, 21, 22, 23, 25, 26, 37, 53, 79, 80, 81, 82, 88, 100, 106, 110, 111, 113, 119, 135, 139, 143, 144, 179, 199, 254, 255, 280, 311, 389, 427, 443, 444, 445, 464, 465, 497, 513, 514, 515, 543, 544, 548, 554, 587, 593, 625, 631, 636, 646, 787, 808, 873, 902, 990, 993, 995, 1000, 1022, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1044, 1048, 1049, 1050, 1053, 1054, 1056, 1058, 1059, 1064, 1065, 1066, 1069, 1071, 1074, 1080, 1110, 1234, 1433, 1494, 1521, 1720, 1723, 1755, 1761, 1801, 1900, 1935, 1998, 2000, 2001, 2002, 2003, 2005, 2049, 2103, 2105, 2107, 2121, 2161, 2301, 2383, 2401, 2601, 2717, 2869, 2967, 3000, 3001, 3128, 3268, 3306, 3389, 3689, 3690, 3703, 3986, 4000, 4001, 4045, 4899, 5000, 5001, 5003, 5009, 5050, 5051, 5060, 5101, 5120, 5190, 5357, 5432, 5555, 5631, 5666, 5800, 5900, 5901, 6000, 6001, 6002, 6004, 6112, 6646, 6666, 7000, 7070, 7937, 7938, 8000, 8002, 8008, 8009, 8010, 8031, 8080, 8081, 8443, 8888, 9000, 9001, 9090, 9100, 9102, 9999, 10000, 10001, 10010, 32768, 32771, 49152, 49153, 49154, 49155, 49156, 49157, 50000]


help_text = """
this program is (SPS) ==> simpel port scaner

  for use this porgram:
	SPS.py (1_element) (2_element)

    1_element is host ip and domain this mandatory

	2_element is port defolt is top_20_port 
	    and can use top_100_port and top_200_port
	    and allp ans use desired port: 22,33,44
	    and singrl port 22

		"""

ips = []
ports = []

class styl:
	END      = '\33[0m'
	BOLD     = '\33[1m'
	ITALIC   = '\33[3m'
	URL      = '\33[4m'
	LINK    = '\33[5m'
	SELCT = '\33[7m'
	BLACK  = '\33[30m'
	RED    = '\33[31m'
	GREEN  = '\33[32m'
	YELLOW = '\33[33m'
	BLUE   = '\33[34m'
	VIOLET = '\33[35m'
	BEIGE  = '\33[36m'
	WHITE  = '\33[37m'


def port_scan(host, port):
	try:
		socket.setdefaulttimeout(0.5)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host, port))
		print(styl.BOLD + styl.GREEN + "Port %d is opend" % (port) + styl.END)
	except Exception as e:
		print(styl.BOLD + styl.RED + "Port %d is closed" % (port) + styl.END)
	finally:
		s.close()

def cidr_checker():
	if len(arg1.split('.')) == 4:
		for ip in ipaddress.IPv4Network(arg1):
			ips.append(str(ip))


if len(sys.argv) > 1:
	arg1 = sys.argv[1]
	if arg1.find("/"):
		cidr_checker()
	else:
		ips.append(arg1)


else:
	print(styl.BOLD + styl.GREEN + help_text + styl.END )
	sys.exit()

if len(sys.argv) > 2:
	arg1 = sys.argv[2]
	if arg2 == 'allp':
		for ip in ips:
			for p in range(66000):
				port_scan(ip, p)
		sys.exit()

	elif arg2 == top_100_port:
		ports = top_100_port
	elif arg2 == top_200_port:
		ports = top_200_port

	elif arg2.find(','):
		port = arg2.split(',')
		ports = [int(p) for p in port]
	else:
		print(styl.BOLD + styl.RED + "port is not cracted \n" + styl.GREEN + help_text + styl.END)

else:
	ports = top_20_port




for ip in ips:
	print(f"{styl.YELLOW}scaning for this ip {ip}:{styl.END}")
	for port in ports:
		port_scan(ip, port)








