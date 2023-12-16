class Car:
  def __init__(self, make, model, stkrprice):
      self.make, self.model, self.stkrprice = make, model, stkrprice
      self.discprice = 0.9 * stkrprice

  def info(self):
      print("Make:", self.make, "Model:", self.model,
            "Sticker Price: ${:,.2f}".format(self.stkrprice),
            "Discount Price: ${:,.2f}".format(self.discprice))

class Sport(Car):
  def __init__(self, make, model, stkrprice):
      super().__init__(make, model, stkrprice)
      self.optprices = {"SportWheels": 1000.00, "SportEngine": 3000.00, "SportInterior": 2000.00}
      self.options = {option: "N" for option in self.optprices}

  def applyoption(self, option):
      if option in self.optprices:
          self.options[option] = "Y"

  def pricewoptions(self):
      updtprice = self.discprice + sum(self.optprices[option] for option in self.options if self.options[option] == "Y")
      print("updated price with options: ${:,.2f}".format(updtprice))

sportcar = Sport("brand", "modelX", 30000.00)

print("car information:")
sportcar.info()

sportcar.applyoption("SportWheels")
sportcar.applyoption("SportEngine")

sportcar.pricewoptions()
