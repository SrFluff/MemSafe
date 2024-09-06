#MemSafe v1.3.0
#Licensed under MIT
#Made by Franco M.

slot = []
sat = []
log = []

def addlog(text):

    log.append(text)

def slotset(slot_set):

    global slot
    global sat
    global log

    i = 1

    while i <= slot_set:

        slot.append(0)
        sat.append(0)

        i += 1

    log.append('Max slots set to ' + str(slot_set))

def alloc(slot_set, val):

    global slot
    global sat
    global log

    try:

        try:

            if sat[slot_set] == 0:

                slot[slot_set] = val
                sat[slot_set] = 1

                log.append('Allocated slot ' + str(slot_set))

            elif sat == 1:

                print('Error - Slot is occupied')

        except IndexError:

            print('Error - List index out of range')

    except TypeError:

        print('Error - Incorrect type')

def dealloc(slot_set):

    global slot
    global sat
    global log

    try:

        try:

            if sat[slot_set] == 1:

                sat[slot_set] = 0
                slot[slot_set] = 0

                log.append('Deallocated slot ' + str(slot_set))

            elif sat[slot_set] == 0:

                print('Warning - Slot is not allocated, did not deallocate')

        except IndexError:

            print('Error - List index out of range')

    except TypeError:

        print('Error - incorrect type')

def var():

    global slot
    global sat

    i = 0

    while i < len(slot):

        print(f'{i}: {slot[i]} {sat[i]}')
        i += 1

def logsh():

    i = 0

    while i < len(log):

        print(f'{log[i]}')

        i += 1

def init():

    main = True

    print('MemSafe debugging shell')
    print('MemSafe v1.3.0')
    print("Type 'help' for a list of commands")

    while main:

        a = input('shell: ')

        if a == 'var':

            var()

        elif a == 'exit':

            exit()

        elif a == 'log':

            a = input('log: ')

            addlog(a)

        elif a == 'logsh':

            logsh()

        elif a == 'help':

            print('var - prints all slots, values, and availability status')
            print('log - adds a custom message to the log')
            print('logsh - prints the log')
            print('exit - exits the MemSafe debugging shell')
