import time
# ---------------------------------------------- BASIC CALCULATOR PORTION ----------------------------------------------
# Calls a function that stores every octade of the user's IP address
def address_maker(x):
    while True:
        if x>=0 and x<256:
            return x
            break
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


# calls a giant function that takes in 8 arguments (4 octades for ip, 4 for mask), converts them to binary, compares them, and returns the network address octades
def network_address(a1,b1,c1,d1,a,b,c,d):
    first_sub_octade = dec_to_bin(a1)
    second_sub_octade = dec_to_bin(b1)
    third_sub_octade = dec_to_bin(c1)
    fourth_sub_octade = dec_to_bin(d1)
    first_bin_octade = dec_to_bin(a)
    second_bin_octade = dec_to_bin(b)
    third_bin_octade = dec_to_bin(c)
    fourth_bin_octade = dec_to_bin(d)
    N1 = []
    N2 = []
    N3 = []
    N4 = []
    for i in range(8):
        if first_sub_octade[i]==1 and first_bin_octade[i]==1:
            N1.append(1)
        else:
            N1.append(0)
    for i in range(8):
        if second_sub_octade[i]==1 and second_bin_octade[i]==1:
            N2.append(1)
        else:
            N2.append(0)
    for i in range(8):
        if third_sub_octade[i]==1 and third_bin_octade[i]==1:
            N3.append(1)
        else:
            N3.append(0)
    for i in range(8):
        if fourth_sub_octade[i]==1 and fourth_bin_octade[i]==1:
            N4.append(1)
        else:
            N4.append(0)
    return N1,N2,N3,N4



# ---------------------------------------------- SUBNET PORTION ----------------------------------------------
# calls a function that determines the bits that should be given to the Network ID of the IPv4 depending on user choice
def network_bits_calculator(answer):
    for i in range(1,33):
        value = 2**i
        if value>=answer:
            return i


# will be made later for the subnet addresses
# ---------------------------------------------- MAIN PROGRAM ----------------------------------------------

print("SIMPLE IPV4 CALCULATOR")
time.sleep(1.5)
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

while True:
    ip_choice = str(input("Is this IPv4 address Classful or Classless? [classful/classless]: ")).strip().lower()
    if "classful" in ip_choice:
        mask_class = class_calculator(first_octade)
        print(f"Class: {mask_class}")
        first_mask_octade,second_mask_octade,third_mask_octade,fourth_mask_octade = mask_calculator_class(mask_class)
        cidr = cidr_calculator(first_mask_octade,second_mask_octade,third_mask_octade,fourth_mask_octade)
        break
    elif "classless" in ip_choice:
        cidr = int(input("What is your CIDR? "))
        while cidr<0 or cidr >32:
            print("A valid CIDR must be between 0-32")
            cidr = int(input("What is your CIDR? "))
        first_mask_octade,second_mask_octade,third_mask_octade,fourth_mask_octade = mask_calculator_cidr(cidr)
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

if cidr!=None:
    net1,net2,net3,net4 = network_address(first_mask_octade,second_mask_octade,third_mask_octade,fourth_mask_octade,first_octade,second_octade,third_octade,fourth_octade)
    first_net_octade = bin_to_dec(net1)
    second_net_octade = bin_to_dec(net2)
    third_net_octade = bin_to_dec(net3)
    fourth_net_octade = bin_to_dec(net4)
    network_address = (f"{first_net_octade}.{second_net_octade}.{third_net_octade}.{fourth_net_octade}")
    print(f"Network Address: {network_address}")

if cidr!=None:
    y = int(input("How many subnets would you like? "))
    network_bits = network_bits_calculator(y)
    equal_subnets = 2**network_bits
    print(f"Your equal subnets will be {equal_subnets}")
else:
    if mask_class=="D":
        print("A Mulitcast IPv4 address cannot be subnetted")
    else:
        print("An Expirimental/Reserved IPv4 address cannot be subnetted")
# Maybe there is a way to clump up all that information in like a seperate function or SOMETHING? its huge clutter in my opinion
# add a check for class D/E and a parameter check for possible subnets later
