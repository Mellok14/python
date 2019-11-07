from sys import argv
script_name, total_h, per_h, bonus = argv
sal = (int(total_h)*int(per_h)) + int(bonus)
print(sal)

sal_v2 = (int(argv[1])*int(argv[2])) + int(argv[3])
print(sal_v2)