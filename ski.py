# ---------------------------------------------- BASIC CALCULATOR PORTION ----------------------------------------------
# Calls a function that stores every octade of the user's IP address
def address_maker(x):
    while True:
        if x>=0 and x<256:
            return x
        else:
            j= -1
            print("A legitimate octade must be between 0-255")
            return j


# Calls a function that calculates the mask of an IP address through given class and saves each mask octade
def mask_calculator_class(x):
    if x=="A":
        return 255,0,0,0
    elif x=="B":
        return 255,255,0,0
    elif x=="C":
        return 255,255,255,0
    elif x=="D":
        return None, None, None, "N/A (Multicast Address)"
    else:
        return None, None, None, "N/A (Expirimental/Reserved)"


# Calls a function that calculates the class through the first octade of the IPv4
def class_calculator(first_octade):
    if first_octade>=0 and first_octade<128:
        return "A"
    elif first_octade>=128 and first_octade<192:
        return "B"
    elif first_octade>=192 and first_octade<224:
        return "C"
    elif first_octade>=224 and first_octade<240:
        return "D"
    else:
        return "E"


# calls a function that calculates the CIDR of an IP address through given mask. Will return None if class is D/E
def cidr_calculator(a,b,c,d):
    if b==c==d==0:
        counter=0
        for i in range(7,16):
            if a==counter:
                return i-7
            else:
                counter=counter+2**(14-i)
    elif a==255 and c==d==0:
        counter=0
        for i in range(14,23):
            if b==counter:
                return i-6
            else:
                counter=counter+2**(21-i)
    elif a==b==255 and d==0:
        counter=0
        for i in range(21,30):
            if c==counter:
                return i-5
            else:
                counter=counter+2**(28-i)
    elif a==b==c==255:
        counter=0
        for i in range(28,37):
            if d==counter:
                return i-4
            else:
                counter=counter+2**(35-i)
    else:
        return None


# calls a function that calculates the mask of an IP address through given CIDR and saves each octade
def mask_calculator_cidr(cidr):
    if cidr>=0 and cidr<=32:
        if cidr<=8:
            a=0
            for i in range(7,-2,-1):
                if cidr==7-i:
                    return a,0,0,0
                else:
                    a=a+2**i
        elif cidr>8 and cidr<=16:
            b=128
            for i in range(6,-2,-1):
                if cidr==15-i:
                    return 255,b,0,0
                else:
                    b=b+2**i
        elif cidr>16 and cidr<=24:
            c=128
            for i in range(6,-2,-1):
                if cidr==23-i:
                    return 255,255,c,0
                else:
                    c=c+2**i
        else:
            d=128
            for i in range(6,-2 ,-1):
                if cidr==31-i:
                    return 255,255,255,d
                else:
                    d=d+2**i


# calls a function that converts a decimal number to a binary number in a stored list
def dec_to_bin(x):
    L=[]
    if x!=0:
        while x!=0:
            a = x%2
            L.append(a)
            x = x//2
    else:
        for i in range(8):
            L.append(0)
    Ln = L[::-1]
    while len(Ln)<8:
        Ln.insert(0,0) # makes sure list is always at least 8 digits to use for comparison
    return Ln


# calls a function that converts a binary number in a sequence from a list, to a decimal number
def bin_to_dec(L):
    number = 0
    revL = L[::-1]
    for i in range(len(revL)):
        if revL[i]==1:
            number = number + 2**i
    return number


# calls a function that returns the mask in binary so it can be compared with the IPv4 later on for the broadcast address
def mask_binary(a1,b1,c1,d1):
    first_mask_octade = dec_to_bin(a1)
    second_mask_octade = dec_to_bin(b1)
    third_mask_octade = dec_to_bin(c1)
    fourth_mask_octade = dec_to_bin(d1)
    return first_mask_octade,second_mask_octade,third_mask_octade,fourth_mask_octade


# calls a function that returns the IPv4 octades in binary to save some clutter
def octade_binary(a1,b1,c1,d1):
    first_octade = dec_to_bin(a1)
    second_octade = dec_to_bin(b1)
    third_octade = dec_to_bin(c1)
    fourth_octade = dec_to_bin(d1)
    return first_octade,second_octade,third_octade,fourth_octade


# calls a function that takes in 8 arguments (4 octades for mask, 4 for ip), converts them to binary, compares them, and returns the network address octades
def network_address(a1,b1,c1,d1,a,b,c,d):
    N1 = []
    N2 = []
    N3 = []
    N4 = []
    for i in range(8):
        if a1[i]==1 and a[i]==1:
            N1.append(1)
        else:
            N1.append(0)
    for i in range(8):
        if b1[i]==1 and b[i]==1:
            N2.append(1)
        else:
            N2.append(0)
    for i in range(8):
        if c1[i]==1 and c[i]==1:
            N3.append(1)
        else:
            N3.append(0)
    for i in range(8):
        if d1[i]==1 and d[i]==1:
            N4.append(1)
        else:
            N4.append(0)
    return N1,N2,N3,N4


# calls a function that takes in the mask and the network address of the IPv4 address to compare them and return the broadcast address octades
def broadcast_address(a1,b1,c1,d1,ak,bk,ck,dk):
    a,b,c,d = ak[:],bk[:],ck[:],dk[:] # creates a fresh copy of the given lists
    for i in range(len(a1)):
        if a1[i]==0:
            a[i]=1
        if b1[i]==0:
            b[i]=1
        if c1[i]==0:
            c[i]=1
        if d1[i]==0:
            d[i]=1
    return a,b,c,d


# calls a function that finds the usable hosts (addresses excluding network/broadcast)
def find_usable_hosts(cidr):
    if cidr==None:
        return "N/A"
    elif cidr>=31:
        return 0
    usable_hosts = (2**(32-cidr))-2
    return usable_hosts


# calls a function that determines the usable network range
def host_range(n1,n2,n3,n4,b1,b2,b3,b4,hosts): # takes in network octades and broadcast octades in decimals
    nn1,nn2,nn3,nn4 = n1,n2,n3,n4
    bn1,bn2,bn3,bn4 = b1,b2,b3,b4
    if hosts==0:
        return 0,0,0,0,0,0,0,None
    if nn4<255:
        nn4=nn4+1
    elif nn3<255:
        nn3=nn3+1
        nn4 = 0
    elif nn2<255:
        nn2=nn2+1
        nn3,nn4 = 0,0
    elif nn1<255:
        nn1=nn1+1
        nn2,nn3,nn4 = 0,0,0
    if bn4>0:
        bn4=bn4-1
    elif bn3>0:
        bn3=bn3-1
        bn4 = 255
    elif bn2>0:
        bn2=bn2-1
        bn3,bn4 = 255,255
    elif bn1>0:
        bn1=bn1-1
        bn2,bn3,bn4 = 255,255,255
    return nn1,nn2,nn3,nn4,bn1,bn2,bn3,bn4



# ---------------------------------------------- SUBNET PORTION ----------------------------------------------
# calls a function that determines the bits that should be given to the Network ID of the IPv4 depending on user choice
def network_bits_calculator(answer):
    for i in range(1,33):
        value = 2**i
        if value>=answer:
            return i


# calls a function that simply takes the new cidr and uses the mask calculator from cidr to find the new mask
def subnet_mask(new_cidr):
    first_submask_octade,second_submask_octade,third_submask_octade,fourth_submask_octade = mask_calculator_cidr(new_cidr)
    return first_submask_octade,second_submask_octade,third_submask_octade,fourth_submask_octade

# calls a function that takes in 8 arguments (4 octades for mask, 4 for ip), converts them to binary, compares them, and returns the sub-network address octades
def network_sub_address(s1,s2,s3,s4,a,b,c,d):
    SN1 = []
    SN2 = []
    SN3 = []
    SN4 = []
    for i in range(8):
        if s1[i]==1 and a[i]==1:
            SN1.append(1)
        else:
            SN1.append(0)
    for i in range(8):
        if s2[i]==1 and b[i]==1:
            SN2.append(1)
        else:
            SN2.append(0)
    for i in range(8):
        if s3[i]==1 and c[i]==1:
            SN3.append(1)
        else:
            SN3.append(0)
    for i in range(8):
        if s4[i]==1 and d[i]==1:
            SN4.append(1)
        else:
            SN4.append(0)
    return SN1,SN2,SN3,SN4


# calls a function that takes in the mask and the network address of the IPv4 address to compare them and return the sub-broadcast address octades
def broadcast_sub_address(a1,b1,c1,d1,ak,bk,ck,dk):
    a,b,c,d = ak[:],bk[:],ck[:],dk[:] # creates a fresh copy of the given lists
    for i in range(len(a1)):
        if a1[i]==0:
            a[i]=1
        if b1[i]==0:
            b[i]=1
        if c1[i]==0:
            c[i]=1
        if d1[i]==0:
            d[i]=1
    return a,b,c,d


# ---------------------------------------------- SUPERNET PORTION ----------------------------------------------








# ---------------------------------------------- MAIN PROGRAM ----------------------------------------------

# IPV4 ADD-UP
print("SIMPLE IPV4 CALCULATOR")
while True:
    x = int(input("Enter the first octade of bytes in your IP address: "))
    first_octade = address_maker(x)
    if first_octade == -1:
        continue
    else:
        break
while True:
    x = int(input("Enter the second octade of bytes in your IP address: "))
    second_octade = address_maker(x)
    if second_octade == -1:
        continue
    else:
        break
while True:
    x = int(input("Enter the third octade of bytes in your IP address: "))
    third_octade = address_maker(x)
    if third_octade == -1:
        continue
    else:
        break
while True:
    x = int(input("Enter the fourth octade of bytes in your IP address: "))
    fourth_octade = address_maker(x)
    if fourth_octade == -1:
        continue
    else:
        break
ipv4_address = (f"{first_octade}.{second_octade}.{third_octade}.{fourth_octade}")
print(f"Your IP address is {ipv4_address}")



#CLASS MASK CIDR AND USABLE HOSTS
exception = 500
while True:
    ip_choice = str(input("Is this IPv4 address Classful or Classless? [classful/classless]: ")).strip().lower()
    if ip_choice in ("classful","ful"):
        mask_class = class_calculator(first_octade)
        print(f"Class: {mask_class}")
        first_mask_octade,second_mask_octade,third_mask_octade,fourth_mask_octade = mask_calculator_class(mask_class)
        cidr = cidr_calculator(first_mask_octade,second_mask_octade,third_mask_octade,fourth_mask_octade)
        usable_hosts = find_usable_hosts(cidr)
        break
    elif ip_choice in ("classless","less"):
        cidr = int(input("What is your CIDR? "))
        while cidr<0 or cidr >32:
            print("A valid CIDR must be between 0-32")
            cidr = int(input("What is your CIDR? "))
        if cidr==31:
            print(f"Note: IPv4 addresses with a /{cidr} CIDR are typically used for Point-to-point links (P2P) since they only have 2 addresses in total for Usable Hosts.")
        elif cidr==32:
            print(f"Note: IPv4 addresses with a /{cidr} CIDR are typically used in routing tables to identify specific hosts, since they only have 1 address in total.")
            exception = 1
        elif cidr==0:
            exception = 0
        first_mask_octade,second_mask_octade,third_mask_octade,fourth_mask_octade = mask_calculator_cidr(cidr)
        usable_hosts = find_usable_hosts(cidr)
        break
    else:
        print("Please give a legitimate answer")
        continue

if first_mask_octade == None: # Checks True only if a classful IP was given that was Class D/E
    print(f"Subnet Mask: {fourth_mask_octade}")
else:
    print(f"Subnet Mask: {first_mask_octade}.{second_mask_octade}.{third_mask_octade}.{fourth_mask_octade}")
if cidr==None:
    print(f"CIDR: N/A")
else:
    print(f"CIDR: /{cidr}")

if usable_hosts!=0:
    print(f"Usable Hosts: {usable_hosts}")
else:
    if cidr==31:
        print(f"Usable Hosts: 2 (CIDR: /{cidr})")
    else:
        print("No Usable Hosts")

# BINARY CONVERSION FOR NORMAL ADDRESSES
if cidr!=None:
    first_binmask_octade,second_binmask_octade,third_binmask_octade,fourth_binmask_octade = mask_binary(first_mask_octade,second_mask_octade,third_mask_octade,fourth_mask_octade) # Returns the mask in binary octades
    first_bin_octade,second_bin_octade,third_bin_octade,fourth_bin_octade = octade_binary(first_octade,second_octade,third_octade,fourth_octade) # Returns the IPv4 in binary octades



# NETWORK/BROADCAST ADDRESS
if cidr!=None:
    net1,net2,net3,net4 = network_address(first_binmask_octade,second_binmask_octade,third_binmask_octade,fourth_binmask_octade,first_bin_octade,second_bin_octade,third_bin_octade,fourth_bin_octade) # compares binary mask and octade for network binary octades
    first_net_octade = bin_to_dec(net1) # returns them back to decimal
    second_net_octade = bin_to_dec(net2)
    third_net_octade = bin_to_dec(net3)
    fourth_net_octade = bin_to_dec(net4)
    network_address = (f"{first_net_octade}.{second_net_octade}.{third_net_octade}.{fourth_net_octade}")
    print(f"Network Address: {network_address}")
    broad1,broad2,broad3,broad4 = broadcast_address(first_binmask_octade,second_binmask_octade,third_binmask_octade,fourth_binmask_octade,net1,net2,net3,net4) # compares mask and network binary for broadcast binary octades
    first_broad_octade = bin_to_dec(broad1) # returns them back to decimal
    second_broad_octade = bin_to_dec(broad2)
    third_broad_octade = bin_to_dec(broad3)
    fourth_broad_octade = bin_to_dec(broad4)
    broadcast_address = (f"{first_broad_octade}.{second_broad_octade}.{third_broad_octade}.{fourth_broad_octade}")
    print(f"Broadcast Address: {broadcast_address}")
    nn1,nn2,nn3,nn4,bn1,bn2,bn3,bn4 = host_range(first_net_octade,second_net_octade,third_net_octade,fourth_net_octade,first_broad_octade,second_broad_octade,third_broad_octade,fourth_broad_octade,usable_hosts)
    if bn4==None:
        print("No Network Range")
    else:
        print(f"Usable Network Range: {nn1}.{nn2}.{nn3}.{nn4}-{bn1}.{bn2}.{bn3}.{bn4}")


#USER INPUT FOR SUBNET/SUPERNET/NOTHING
while True:
    z=str(input("Would you like to subnet this IPv4 address, supernet it or do nothing? [subnet/supernet/nothing]: ")).strip().lower()
    if z in ("subnet","sub"):
        yz = 1
        break
    elif z in ("supernet","super","sup"):
        yz = 0
        break
    elif z in ("nothing","n","none"):
        yz = -1
        break
    else:
        print("Please give a legitimate answer")
        continue


#SUBNET INPUTS/CALCULATIONS
if cidr!=None and yz==1 and exception!=1:
    y = int(input("How many subnets would you like? "))
    while y>2**(32-cidr) or y<2:
        print(f"You can only have from {2} up to {2**(32-cidr)} subnets")
        y = int(input("How many subnets would you like? "))
    network_bits = network_bits_calculator(y)
    equal_subnets = 2**network_bits
    print(f"Your equal subnets will be {equal_subnets}")
    new_cidr = cidr+network_bits
    first_submask_octade,second_submask_octade,third_submask_octade,fourth_submask_octade = subnet_mask(new_cidr)
    print(f"New Subnet Mask: {first_submask_octade}.{second_submask_octade}.{third_submask_octade}.{fourth_submask_octade}")
    print(f"New CIDR: /{new_cidr}")
    usable_hosts = find_usable_hosts(new_cidr)
    if usable_hosts!=0:
        print(f"Usable Hosts: {usable_hosts}")
    else:
        print("No Usable Hosts")
    first_binsubmask_octade,second_binsubmask_octade,third_binsubmask_octade,fourth_binsubmask_octade = mask_binary(first_submask_octade,second_submask_octade,third_submask_octade,fourth_submask_octade) # turns the subnet mask octades in binary
    subnet1,subnet2,subnet3,subnet4 = network_sub_address(first_binsubmask_octade,second_binsubmask_octade,third_binsubmask_octade,fourth_binsubmask_octade,first_bin_octade,second_bin_octade,third_bin_octade,fourth_bin_octade) # finds the network address binary octades through the subnet mask octades (in binary from above) compared to the normal IPv4 octades in binary
    first_subnet_octade = bin_to_dec(subnet1) # returns them back to decimal
    second_subnet_octade = bin_to_dec(subnet2)
    third_subnet_octade = bin_to_dec(subnet3)
    fourth_subnet_octade = bin_to_dec(subnet4)
    subnetwork_address = (f"{first_subnet_octade}.{second_subnet_octade}.{third_subnet_octade}.{fourth_subnet_octade}")
    print(f"Sub-Network Address: {subnetwork_address}")
    subbroad1,subbroad2,subbroad3,subbroad4 =  broadcast_sub_address(first_binsubmask_octade,second_binsubmask_octade,third_binsubmask_octade,fourth_binsubmask_octade,subnet1,subnet2,subnet3,subnet4) # compares subnet mask and subnetwork octades for sub broadcast address
    first_subbroad_octade = bin_to_dec(subbroad1) # returns them back to decimal
    second_subbroad_octade = bin_to_dec(subbroad2)
    third_subbroad_octade = bin_to_dec(subbroad3)
    fourth_subbroad_octade = bin_to_dec(subbroad4)
    subbroadcast_address = (f"{first_subbroad_octade}.{second_subbroad_octade}.{third_subbroad_octade}.{fourth_subbroad_octade}")
    print(f"Sub-Broadcast Address: {subbroadcast_address}")
elif cidr!=None and yz==1 and exception==1:
    print(f"Cannot be subnetted further since it has only 1 network. (/{cidr} CIDR)")


#SUPERNET INPUTS/CALCULATIONS
elif cidr!=None and yz==0 and exception!=0:
    print("later")

elif cidr!=None and yz==0 and exception==0:
    print(f"Cannot be supernetted further since it already covers the entire IPv4 range. (/{cidr} CIDR)")







elif cidr!=None and yz==-1:
    print("Understood")


if cidr==None:
    if mask_class=="D":
        print("A Mulitcast IPv4 address cannot be subnetted")
    else:
        print("An Expirimental/Reserved IPv4 address cannot be subnetted")
#0. Fix all edge cases, try to optimize by reusing network and broadcast function for sub/supernet
#1. Work on supernetting
#2. Add exceptValueError parameters
#3. figure out a DECENT way to finish all this shit by adding network/broadcast address for each SUBnet, then the usuable range
#4. Close this shit with the READme.md on github and check for error handling
