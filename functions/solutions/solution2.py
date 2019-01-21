def calculate_tax(bill, taxrate):
  """(number, number) -> number
  
  Returns the mount of tax to be paid on bill
  when the tax rate is taxrate.abs

  >>> calculate_tax(100, 0.23)
  23.0
  >>> calculate_tax(5, 0) 
  0
  """
  return bill*taxrate