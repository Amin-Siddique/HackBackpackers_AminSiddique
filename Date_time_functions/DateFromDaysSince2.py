def get_DateFromDays2(date,daysToAddOrSubtract):
  '''
  date - date value could be pass as string or date
  daysToAddOrSubtract - Integer value to add or subtract from the date value. Could be a positive or negative value.
  '''
  return addDays(toDate(toString(date)),n)

eg:
Expression => addDays(toDate('1958-08-18'),-18250)
output => 1908-08-30
