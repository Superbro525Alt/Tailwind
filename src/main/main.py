"""Import sys and os module to add lib paths to system path"""
import sys
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir + "/lib")

"""Import util module"""
import util

