import re
import zlib

pdf = open("demo.pdf", "rb").read()
stream = re.compile(rb'.*?FlateDecode.*?stream(.*?)endstream', re.S)

for s in stream.findall(pdf):
    s = s.strip(b'\r\n')
    try:
        print(zlib.decompress(s))
        print("")
    except:
        pass