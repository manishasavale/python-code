# new list of 70s TV programs
progs = ['yes', 'genesis', 'pink floyd', 'ELP']


for prog in progs:
    print (prog)


progs[-1] = 'King Crimson'

progs.append('Camel')

progs.remove('pink floyd')

progs.sort()

progs.reverse()


#prints with number order
for i, prog in enumerate(progs):
     print(i + 1, '=>', prog)


# prints from de second item
print(progs[1:])

my_list = ['A', 'B', 'C']
print ('List:', my_list)

#The empty list is evaluated as false
while my_list:
      #In queues, the first item is the first to go out
      # pop(0) removes and returns the first item
      print('Left', my_list.pop(0), ',remain', len(my_list))

# More items on the list
my_list += ['D', 'E', 'F']
print('list:', my_list)

while my_list:
    # On stacks, the first item is the last to go out
    # pop() removes and returns the last item
    print('Left', my_list.pop(), ',remain', len(my_list))

