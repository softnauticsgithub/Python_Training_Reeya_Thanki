#Topic : BASIC PYTHON
#Exercise Number : 27
##PROBLEM STATEMENT:
#Write a python code to generate the json file using python "json" module
#which will contain the serial communication parameters taken from user
#using "Argparser". i.e. port, baud rate, parity ,stop bit and etc.
# Python Version : 3.7
"""
- Your json file will contains the all possible serial
 communication parameters in key-value pair, "port":odd and etc.
    NOTE: Explore the the various serial communication
    parameters. what is baud rate, parity and etc.
"""
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--port", type=str)
parser.add_argument("--budRate", type=int)
parser.add_argument("--parity", type=str)
parser.add_argument("--stopBit", type=int)
parser.add_argument("--timeOut", type=float)
parser.add_argument("--dataBit", type=int)
args = parser.parse_args()
serial_params={
    "port":args.port,
    "bud-rate":args.budRate,
    "parity":args.parity,
    "stop-bit":args.stopBit,
    "time-out":args.timeOut,
    "data-bit":args.dataBit,
}
with open("ex_27.json",'w') as json_file:
    json.dump(serial_params,json_file)
