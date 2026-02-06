# IPv4 Calculator

A light-weight CLI (command line interface) tool that calculates IPv4 network information **without using any external libraries**. Built from scratch to understand networking fundamentals at a low level.

## Features

### Basic Information
- **Subnet Mask** - Calculated from class or CIDR
- **Network Class** - Automatic detection (A, B, C, D, E)
- **CIDR Notation** - Supports /0 through /32
- **Network Address** - First address in the subnet
- **Broadcast Address** - Last address in the subnet
- **Usable Host Range** - Range between the first and the last Usable Networks

### Advanced Operations
- **Classful & Classless** - Support for both addressing schemes
- **Supernetting** - Combine multiple networks into one
- **Subnetting** - Divide networks into smaller subnets
- **Subnet Enumeration** - Lists all possible subnets with their network and broadcast addresses

## Installation

### Linux/macOS
1. Clone the repository:
```bash
git clone https://github.com/DarkF4de/ipv4-calculator.git
cd ipv4-calculator
```

2. Run the calculator:
```bash
python3 ipv4_calculator.py
```

### Windows
1. Clone the repository:
```cmd
git clone https://github.com/DarkF4de/ipv4-calculator.git
cd ipv4-calculator
```

2. Run the calculator:
```cmd
python ipv4_calculator.py
```

**Note:** Windows users may need to use `python` instead of `python3`. If you don't have Python installed, download it from [python.org](https://www.python.org/downloads/).

## Usage Example
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

## Technical Details

- **No libraries or imports** - Built entirely from scratch using core Python
- **Manual binary operations** - All subnet calculations done through custom binary/decimal conversion functions
- **Error handling** - Input validation and edge case handling
- **Supports special cases** - Parameters and Notes for /31 (point-to-point), /32 (host routes), /0 (default route)

## Learning Goals

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

## Requirements

- Python 3.x

## License

This project is open source and available for educational purposes.
