import convert
import sys

#python example.py 10 ft m
stuff = convert.convert(sys.argv[1], sys.argv[2], sys.argv[3])
print("converted {}{} to {}{}".format(sys.argv[1], sys.argv[2], stuff, sys.argv[3]))
#converted 10ft to 3.048m