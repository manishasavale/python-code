import traceback

try:
    print (1/0)
except:
    print('Error trying to divide by zero')

# Try to get a file name
try:
    fn = raw_input('My name is Manisha:   ').strip()

    # Numbering lines
    for i, s in enumerate(file(fn)):
        print(i + 1, s ,)

# If en error happens
except:
    # show it on the screen
    trace = traceback.format_exc()

    # And save it into a file
    print('An error happened:\n', trace)
    file('trace.log', 'a').write(trace)

    #end the program
    raise SystemExit
