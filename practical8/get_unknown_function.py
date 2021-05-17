import re
x = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
y = ''
z = False
l = ''
for line in x:
    if line.startswith('>'):
       if z == True:
          l = l + ('>' + m + ' ' + str(len(y)) + '\n' + y + '\n')
          y = ''
          z == False
       if re.findall(r'unknown',line):
          m = re.findall(r'^>.+?_',line)    
          m = m[0]
          m = m[:-1]
          z = True
    else:
       if z == True:
            y = y + line.strip() + '\n'
x.close()
n = open('unknown_function.fa','w')
n.write(l)
n.close()
x = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
print(x.read())
x.close()
