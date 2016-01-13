import openpyxl

# Scenario

# Stage 1
# Open file $HOME/dhcpd.conf for reading
# Read temp file line by line till the end in a loop
# Find all lines containing of subnet but not subnet-mask, no comment mark "#" before "subnet"
# Write them into a temp file /tmp/dhcpd.tmp

DHCP_CFG='/home/georgiev/dhcpd.conf'
TMP_FILE='/tmp/dhcpd.tmp'

def stage_1():
    f1 = open(DHCP_CFG,'r')
    f2 = open(TMP_FILE,'w')

    # Reading line by line with a loop
    try:
        for line in f1:
            # print line - prints empty character '\0' at the end of the line
            # print line.strip() - is OK in Linux without empty character '\0' at the end
            # the line should contain "subnet", but not "subnet-mask", no comment mark "#" before "subnet"
            if line.count('subnet')>0:
                if line.count('subnet-mask')==0:
                    if line.find('#') == -1: # Comment mark not found
                        f2.write(line)
                    else: # Comment mark is found
                        if line.find('#')>line.find('subnet'): # Comment mark is after "subnet"
                            f2.write(line)
    finally:
        f1.close()
        f2.close()
    
# Stage 2
# Create an Excel workbook with sheet "Network IDs"
# Select "Sheet1", cell A1
# Open temp file for reading
# a) omit word "subnet"
# b) write the next word (network ID) to the first column A2
# c) omit the work "netmask"
# d) write the next word (subnet mask) to the second column B2
# Increase the row counter
# Repeat the loop


exit()