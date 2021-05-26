import argparse
import os
import sys
import math
import re
class Pattern:
    def __init__(self):
        self.args = self.parse_command_line()
    def parse_command_line(self):
        my_parser = argparse.ArgumentParser(description='Generate patten of get offset from eip address for binary exploitation')
        my_parser.add_argument( '-l',
                                '--lenght',
                                action='store',
                                type=int,
                                help='the lenght of generated pattern')
        my_parser.add_argument( '-f',
                                '--offset',
                                action='store',
                                type=str,
                                required=False,
                                help='the eip address to get offset from it')
        return my_parser
    def generate_pattern(self,lenght=int(math.pow(62,3))):
        pattern = ""
        for i in range(1,9):
            for upper in range(ord('A'),ord('Z')+1):
                for lower in range(ord('a'),ord('z')+1):
                    for number in range(10):
                        pattern += f"{chr(upper)}{chr(lower)}{number}"*i
                        if len(pattern)>=lenght:
                            break   
                    if len(pattern)>=lenght:
                        break
                if len(pattern)>=lenght:
                    break
            if len(pattern)>=lenght:
                break
        return pattern[:lenght]
    def get_offset_from_hex(self,addr:str):
        addr = addr[2:] if addr.startswith('0x') else addr
        addr = addr if len(addr)%2==0 else "0"+addr
        pattern_set = ""
        pattern = self.generate_pattern()
        for x in range(0,len(addr)-1,2):
            pattern_set += chr(int("0x"+addr[x:x+2],16))
        return pattern.index(pattern_set)
    def run(self):
        args  = self.args.parse_args()
        if(args.lenght==None and args.offset==None):
            self.args.print_help()
        elif args.lenght!=None:
            print(self.generate_pattern(args.lenght))
        elif args.offset!=None:
            print(f"Lenght of offset is : {self.get_offset_from_hex(args.offset)}")
Pattern().run()