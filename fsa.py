from enum import Enum, unique

# -----------------------------------------------------------------------------
#   FSA
# -----------------------------------------------------------------------------
class FSA:

    @unique
    class State(Enum):
        Idle = 0
        Process1 = 1
        Process2 = 2
        Process3 = 3

    @unique
    class Event(Enum):
        Start = 0
        Next = 1
        Reset = 2

    def __init__(self):
        self.__state = FSA.State.Idle

    def __str__(self):
        return f'FSA [{self.__state}]'
    
    def __set_state(self, state):
        print(f'State: {state}')
        self.__state = state

    def __get_state(self):
        return self.__state

    state = property(__get_state)

    def SetEvent(self, event):
        print(f'Event: {event}')
        if event == FSA.Event.Start:
            if self.__state == FSA.State.Idle:
                self.__set_state(FSA.State.Process1)
        elif event == FSA.Event.Next:
            if self.__state == FSA.State.Process1:
                self.__set_state(FSA.State.Process2)
            elif self.__state == FSA.State.Process2:
                self.__set_state(FSA.State.Process3)
            elif self.__state == FSA.State.Process3:
                self.__set_state(FSA.State.Idle)
        elif event == FSA.Event.Reset:
            if self.__state != FSA.State.Idle:
                self.__set_state(FSA.State.Idle)

fsa = FSA()

print(fsa)

fsa.SetEvent(FSA.Event.Start)
fsa.SetEvent(FSA.Event.Start)
fsa.SetEvent(FSA.Event.Next)
fsa.SetEvent(FSA.Event.Next)
fsa.SetEvent(FSA.Event.Next)
fsa.SetEvent(FSA.Event.Next)
fsa.SetEvent(FSA.Event.Next)
fsa.SetEvent(FSA.Event.Next)

print(fsa.state)

# forbiden operations
#
# fsa.state = FSA.State.Process2
# fsa.__set_state(FSA.State.Process2)
