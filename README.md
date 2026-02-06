# IPv4 Calculator
A CLI tool I built from scratch to learn Python and understand how IPv4 networking actually works under the hood. No libraries or external packages.

## What it does
Calculates all the IPv4 network info you'd normally use an online calculator for:
- Subnet masks (from class or CIDR)
- Network and broadcast addresses  
- CIDR notation (/0 through /32)
- Network class detection (A, B, C, D, E)
- Usable host ranges
- Subnetting (split networks into smaller ones)
- Supernetting (combine networks into bigger ones)
- Full subnet enumeration (lists every subnet with network/broadcast addresses)

Also handles both classful and classless addressing.

## Why I built this
Started because I wanted to actually understand IPv4 networking to its core, and whilst I can do the math on paper, it would be extremely beneficial for me to actually try to make a program for it - not just for my networking skills but especially for my Python ones. 

Obviously, it ended up being way more of a Python learning project than a networking one. Spent most of the time writing binary/decimal converters and handling all the edge cases. But that was kind of the point I guess.

## Installation & Usage
**Linux/macOS:**
```bash
git clone https://github.com/DarkF4de/ipv4-calculator.git
cd ipv4-calculator
python3 ipv4_calculator.py
```

**Windows:**
```cmd
git clone https://github.com/DarkF4de/ipv4-calculator.git
cd ipv4-calculator
python ipv4_calculator.py
```

> Note: If Python isn't installed, grab it from [python.org](https://www.python.org/downloads/)

## Example
```
IPV4 CALCULATOR
Enter the first octade of bytes in your IP address [0-255]: 192
Enter the second octade of bytes in your IP address [0-255]: 168
Enter the third octade of bytes in your IP address [0-255]: 1
Enter the fourth octade of bytes in your IP address [0-255]: 0

Your IP address is 192.168.1.0

Is this IPv4 address Classful or Classless? [classful/classless]: classless
What is your CIDR? [0-32]: 24

Subnet Mask: 255.255.255.0
CIDR: /24
Usable Hosts: 254
Network Address: 192.168.1.0
Broadcast Address: 192.168.1.255
Usable Network Range: 192.168.1.1 - 192.168.1.254

Would you like to Subnet this IPv4 address, Supernet it or do nothing? [subnet/supernet/nothing]:
```

## What I learned

### Python Skills
- **Algorithm design** - Building binary/decimal conversion functions from scratch
- **Data structure manipulation** - List operations, slicing, and transformations
- **Type handling** - Converting between strings, integers, and binary representations
- **Error handling** - Exception handling and input validation
- **Edge case management** - Handling special cases like /31, /32, and /0 CIDRs

### Networking Concepts
- How IPv4 addressing works at the bit level
- Subnet mask calculation and CIDR notation
- Network and broadcast address determination
- Subnetting and supernetting operations
- Classful vs classless addressing schemes

## Technical details
- Built entirely from scratch - no imports, no libraries, just core Python
- All subnet calculations done with custom binary/decimal conversion functions
- Input validation and error handling for user inputs
- Handles special cases (/0, /31, /32)

## Requirements
Python 3.x

## Notes
The subnet enumeration can get pretty long if you're splitting into a lot of subnets (like /24 to /30 = 64 subnets). Added a confirmation prompt if it goes over 1024 subnets so you don't accidentally spam your terminal.

---

Built for learning. Feel free to use for educational purposes or if you want to make your life easier.
