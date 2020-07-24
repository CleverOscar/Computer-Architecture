# ls8.py file

imports CPU module, invoke load() and run()
assuming load() loads up the memory
and run() runs the script

#cpu.py file

imports sys module.

CPU Class, initilize cpu constructor,

load function,


#### Questions

Is address acting as our PC?

program holds our commands in binary form.



# Where to store variables if we have too many for the registers?

# Stack: Push, pop, storage

# RAM == Memory

# Registers, caches, RAM, hard drive

# Memory: away to store info and get it back



FF: 00
FE: 00
FD: 00
FC: 00
FB: 00
FA: 00
F9: 00
F8: 00
F7: 00
F6: 00
F5: 00
F4: 00
F3: 99 <-- SP
F2: 99 <-- SP
F1: 00
F0: 00
EF: 00
EE: 00
ED: 00



0
03
02
01
00


Challenge
---------
What happens if you PUSH too many items on the stack?

What happens if you POP from an empty stack?

How can you detect if the stack is empty?

What information must be saved on the stack when the CPU is servicing an interrupt? Why?
