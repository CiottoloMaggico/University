import sys

def printer_controller():
    statues_left = int(sys.stdin.readline().strip())
    day, n_printers = 1, 1
    while n_printers * 2 < statues_left:
        n_printers *= 2
        day += 1
    while statues_left > 0:
        statues_left -= n_printers
        day += 1
    return day-1

print(printer_controller())