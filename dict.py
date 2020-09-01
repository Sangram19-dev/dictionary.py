#python dictionary

#it is a data type

'''d={keys:value} #key value pair'''
'''dic={}
print(type(dic))'''

'''dic={1:'apple',2:'banana'} #integer key dict
dic2={"name":'sangram',"surname":"gupta"} #string key dict
print(dic2)'''

#Accessing elements
'''d={'name':'sangram','age':21}
print(d['name'])
print(d.get('age'))
print(d.get('address'))'''

#Changing/adding elements

'''d={'name':'sangram','age':21}
#update elements
d['age']=25
print(d)
#add a key:value pair in dict
d['address']="kolkata"
print(d)'''

#removing elements
'''s={1:1,2:4,3:9,4:16,5:25}
#remove a particuler item
print(s.pop(4))
print(s)

#remove an arbitary item
print(s.popitem())
print(s)

s.clear()
print(s)'''

#dict comprehention
'''squres={x: x*x for x in range(6)}
print(squres)'''
'''squres={}
for x in range(6):
  squres[x]=x*x
print(squres)'''

#membership test
s={1:1,2:4,3:9,4:16,5:25}
print(1 in s)
print(2 not in s)
print(25 in s)
