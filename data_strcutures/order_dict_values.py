from collections import Counter

ip = [
	"192.168.0.100",
	"192.168.0.110",
	"192.168.0.120",
	"192.168.0.130",
	"192.168.0.100",
	"192.168.0.110",
	"192.168.0.120",
	"192.168.0.100",
	"192.168.0.110",
	"192.168.0.100",
]

print(f"The top ip is {Counter(ip).most_common(1)[0][0]}"
	f" which accessed {Counter(ip).most_common(1)[0][1]} times.")
