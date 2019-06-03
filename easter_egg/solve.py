import re
text = open("careers",'r').read()
text = re.findall('''<span style="color:white">.</span>''',text)
print ''.join([t[26:-7] for t in text])