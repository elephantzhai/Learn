complex = require "chapter15"
c1 = complex.new(10,20)
c2 = complex.new(30,40)
c = complex.add(c1,c2)
print(complex.tostring(c))