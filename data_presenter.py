open_file = open("cupcakeInvoices.cvs")

day_total = 0

for line in open_file:
    print(line)

for line in open_file:
    line = line.rstrip('\n').split(',')
    print(line[2])

for line in open_file:
  line = line.rstrip('\n').split(',')
  total = round(int(line[3])*float(line[4]), 2)
  print(total)
  day_total = round(day_total + total, 2)

print(day_total)

open_file.close()
