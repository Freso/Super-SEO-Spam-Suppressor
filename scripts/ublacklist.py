# Generates a list in the match pattern format for the the uBlacklist browser extension from the content of the `sources` folder.
# Usage:
# python ublacklist.py > ublacklist.txt

# Open header
with open("sources/headers/default.txt", "r") as header:
	linesheader = header.readlines()

# Open blocked formats
with open("sources/domains.txt", "r") as domains:
	linesdomains = domains.readlines()
with open("sources/tlds.txt", "r") as tlds:
	linestlds = tlds.readlines()
with open("sources/urls.txt", "r") as urls:
	linesurls = urls.readlines()
blocklist = linesdomains + linestlds + linesurls

# Print blocklist
for line in linesheader:
	print(line.strip())
print()
for line in blocklist:
	print('*://*.' + line.strip() + '/*')
