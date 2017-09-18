import re

# meta characters --> .^$*+{}[]\()

#regex = re.compile('a')
#regex = re.compile('[abc]')
#regex = re.compile('[a-zA-Z]') # match
regex = re.compile('[^a-zA-Z]') # donot match ( compliment )
print (regex.match('2'))

r = re.compile('[a*]')
print (r.match ('aaaaaaaaaaaaaaaaaaaaaaaaa'))
r = re.compile('[a-c]*')
print (r.match ('abcabbcbbccbba'))
r = re.compile('[a]+')
print (r.match ('aa')) # minumum one
r = re.compile('a?b') # a can comes and can not but only once
print (r.match('b'))
r = re.compile('a{2,3}') # a can comes 2-3 times
print (r.match('aa'))

r = re.compile('^abc') # a can comes 2-3 times
print (r.match('abc'))

r = re.compile('a|b') # a or b
print (r.match('aa'))

r = re.compile('abc$') # ending of the string
print (r.match('aa'))
