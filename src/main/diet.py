class Diet:
  minimum_price = 10
  maximum_price = 20
  
  def __init__(self, factor, pounds_per_month, minimum_price = Diet.minimum_price, maximum_price = Diet.maximum_price):
    self.factor = factor
    self.pounds_per_month = pounds_per_month
    self.minimum_price = minimum_price
    self.maximum_price = maximum_price
  
  def unit_price(self):
    price = ((self.factor * (self.maximum_price - self.minimum_price))*(0.75**self.pounds_per_month) + self.factor * self.minimum_price)
    
    unit_price = price if price > self.minimum_price else self.minimum_price
    return round(unit_price, 2)
  
  def total_price(self):
    return self.unit_price() * self.pounds_per_month
  
  def calories(self):
    return (0.75**self.pounds_per_month)/1000