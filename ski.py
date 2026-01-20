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

# ---------------------------------------------- SUBNET PORTION ----------------------------------------------
# calls a function that determines the bits that should be given to the Network ID of the IPv4 depending on user choice
def network_bits_calculator(answer):
    for i in range(1,33):
        value = 2**i
        if value>=answer:
            return i


#def network_address(cidr,network_bits):   WILL BE DONE WHEN MASK CALCULATOR FROMMM CIDR IS MADE TO CALL IT IN NEW_MASK
 #   new_cidr = cidr+network_bits
  #  new_mask = new_cidr
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
    ip_choice = str(input("Is this IPv4 address classful or classless? [Classful/Classless]: ")).strip().lower()
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


if first_mask_octade == None:
    print(f"Subnet Mask: {fourth_mask_octade}")
else:
    print(f"Subnet Mask: {first_mask_octade}.{second_mask_octade}.{third_mask_octade}.{fourth_mask_octade}")
if cidr==None:
    print(f"CIDR: {cidr}")
else:
    print(f"CIDR: /{cidr}")
y = int(input("How many subnets would you like? "))
network_bits = network_bits_calculator(y)
equal_subnets = 2**network_bits
print(f"Your equal subnets will be {equal_subnets}")

