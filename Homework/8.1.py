class Data:
  def __inut__(self,date):
    self.date = date
  @classmethod
  def date_int(cls, date):
    return list(map(int,date.split("-")))
  @staticmethod
  def valid(date):
    if Data.date_int(date)[0] >= 1 and Data.date_int(date)[0] <= 31:
      d = 'Значение "дня" корректно'
    else: d = 'Значение "дня" НЕ корректно'
    if Data.date_int(date)[1] >= 1 and Data.date_int(date)[1] <= 12:
      m = 'Значение "месяца" корректно'
    else: m = 'Значение "месяца" НЕ корректно'
    if Data.date_int(date)[2] > 1 and Data.date_int(date)[2] < 9999:
      y = 'Значение "года" корректно'
    else: y = 'Значение "года" НЕ корректно'
    return print(f"\n{d}", f"\n{m}", f"\n{y}" )

Data.valid('32-14-1993')
print('----------------------------')
Data.valid('12-5-2001')
print('----------------------------')
Data.valid('10-55-111234')