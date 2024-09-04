#MemSafe v1.1.0
#Licensed under MIT
#Made by Franco M.

slot = []
sat = []
log = []

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
