revenue = int(input("Enter the company's revenue: "))
costs = int(input("Enter the company's costs: "))
if revenue > costs:
    print('The company is in profit')
    profit = (revenue - costs)/revenue
    print(f'Profitability {profit}')
    number_emp = int(input('Enter the number of employees: '))
    emp_profit = (revenue - costs)/number_emp
    print(f'Profit per employee {emp_profit}')
if revenue <= costs:
    print('The company suffers losses')