from datetime import datetime


class Customer:
    
    _totalCustomers = 0
    
    def __init__(self, customerId, firstName, lastName, email, 
                 phoneNumber=None, shippingAddress=None):
        self.__customerId = customerId
        self._firstName = firstName
        self._lastName = lastName
        self._email = email
        self._phoneNumber = phoneNumber
        self._shippingAddress = shippingAddress
        self._registrationDate = datetime.now()
        Customer._totalCustomers += 1
    
    def getFullName(self):
        return f"{self._firstName} {self._lastName}"
    
    def getCustomerId(self):
        return self.__customerId
    
    def getEmail(self):
        return self._email
    
    def setEmail(self, value):
        if "@" in value:
            self._email = value
        else:
            print("Помилка: Невірний формат email")
    
    def getInfo(self):
        phone = self._phoneNumber if self._phoneNumber else "Не вказано"
        address = self._shippingAddress if self._shippingAddress else "Не вказано"
        dateStr = self._registrationDate.strftime('%d.%m.%Y %H:%M')
        
        info = f"Клієнт #{self.__customerId}: {self.getFullName()}\n"
        info += f"Email: {self._email}\n"
        info += f"Телефон: {phone}\n"
        info += f"Адреса: {address}\n"
        info += f"Зареєстрований: {dateStr}"
        return info
    
    def updateContactInfo(self, email=None, phone=None, address=None):
        if email:
            self.setEmail(email)
        if phone:
            self._phoneNumber = phone
        if address:
            self._shippingAddress = address
        print(f"Контактні дані клієнта {self.getFullName()} оновлено")
    
    def calculateDiscount(self, baseAmount):
        return baseAmount
    
    def getTotalCustomers():
        return Customer._totalCustomers
    
    def __str__(self):
        return f"Customer({self.getCustomerId()}, {self.getFullName()})"


class LoyaltyProgram:
    
    def __init__(self, loyaltyPoints=0):
        self._loyaltyPoints = loyaltyPoints
        self._loyaltyLevel = "Bronze"
    
    def getLoyaltyPoints(self):
        return self._loyaltyPoints
    
    def addPoints(self, points):
        self._loyaltyPoints += points
        self._updateLoyaltyLevel()
        print(f"Додано {points} балів. Всього: {self._loyaltyPoints}")
    
    def _updateLoyaltyLevel(self):
        if self._loyaltyPoints >= 1000:
            self._loyaltyLevel = "Gold"
        elif self._loyaltyPoints >= 500:
            self._loyaltyLevel = "Silver"
        else:
            self._loyaltyLevel = "Bronze"
    
    def getLoyaltyInfo(self):
        return f"Рівень: {self._loyaltyLevel}, Бали: {self._loyaltyPoints}"


class PremiumCustomer(Customer):
    
    def __init__(self, customerId, firstName, lastName, email, 
                 phoneNumber=None, shippingAddress=None, premiumSince=None):
        super().__init__(customerId, firstName, lastName, email, 
                        phoneNumber, shippingAddress)
        if premiumSince:
            self._premiumSince = premiumSince
        else:
            self._premiumSince = datetime.now()
        self._discountRate = 0.15
    
    def calculateDiscount(self, baseAmount):
        discount = baseAmount * self._discountRate
        finalAmount = baseAmount - discount
        print(f"Преміум знижка 15%: -{discount:.2f} грн")
        return finalAmount
    
    def getInfo(self):
        baseInfo = super().getInfo()
        dateStr = self._premiumSince.strftime('%d.%m.%Y')
        premiumInfo = f"\nПреміум статус з: {dateStr}"
        return baseInfo + premiumInfo
    
    def getPremiumSupport(self):
        print(f"{self.getFullName()} отримав доступ до пріоритетної підтримки 24/7")


class VIPCustomer(Customer, LoyaltyProgram):
    
    def __init__(self, customerId, firstName, lastName, email, 
                 phoneNumber=None, shippingAddress=None, personalManager=None):
        Customer.__init__(self, customerId, firstName, lastName, email, 
                         phoneNumber, shippingAddress)
        LoyaltyProgram.__init__(self, loyaltyPoints=1500)
        self._personalManager = personalManager
        self._discountRate = 0.25
    
    def calculateDiscount(self, baseAmount):
        discount = baseAmount * self._discountRate
        finalAmount = baseAmount - discount
        print(f"VIP знижка 25%: -{discount:.2f} грн")
        return finalAmount
    
    def getInfo(self):
        baseInfo = super().getInfo()
        manager = self._personalManager if self._personalManager else "Не призначено"
        vipInfo = f"\nVIP статус\n"
        vipInfo += f"Персональний менеджер: {manager}\n"
        vipInfo += self.getLoyaltyInfo()
        return baseInfo + vipInfo
    
    def assignPersonalManager(self, managerName):
        self._personalManager = managerName
        print(f"Персональний менеджер {managerName} призначений для {self.getFullName()}")
    
    def useVipLounge(self):
        print(f"{self.getFullName()} отримав доступ до VIP зони")


def printSeparator(title=""):
    print("\n" + "=" * 60)
    if title:
        print(f"  {title}")
        print("=" * 60)


def processOrder(customer, orderAmount):
    print(f"\nОбробка замовлення для {customer.getFullName()}")
    print(f"Сума замовлення: {orderAmount:.2f} грн")
    finalAmount = customer.calculateDiscount(orderAmount)
    print(f"До сплати: {finalAmount:.2f} грн")


def main():
    printSeparator("СИСТЕМА КЕРУВАННЯ КЛІЄНТАМИ")
    
    
    regularCustomer = Customer(
        customerId=1001,
        firstName="Іван",
        lastName="Петренко",
        email="ivan.petrenko@email.com",
        phoneNumber="+380501234567",
        shippingAddress="вул. Шевченка, 10, Львів"
    )
    
    premiumCustomer = PremiumCustomer(
        customerId=1002,
        firstName="Марія",
        lastName="Коваленко",
        email="maria.kovalenko@email.com",
        phoneNumber="+380502345678",
        shippingAddress="вул. Франка, 25, Київ"
    )
    
    vipCustomer = VIPCustomer(
        customerId=1003,
        firstName="Олександр",
        lastName="Шевченко",
        email="alex.shevchenko@email.com",
        phoneNumber="+380503456789",
        shippingAddress="вул. Грушевського, 5, Одеса",
        personalManager="Наталія Іванова"
    )
    
    print(f"Створено {Customer.getTotalCustomers()} клієнтів")
    
    printSeparator("ІНФОРМАЦІЯ ПРО КЛІЄНТІВ")
    
    print("\nЗвичайний клієнт:")
    print(regularCustomer.getInfo())
    
    print("\nПреміум клієнт:")
    print(premiumCustomer.getInfo())
    
    print("\nVIP клієнт:")
    print(vipCustomer.getInfo())
    
    printSeparator("ОНОВЛЕННЯ КОНТАКТНИХ ДАНИХ")
    
    regularCustomer.updateContactInfo(
        phone="+380507654321",
        address="вул. Лесі Українки, 15, Львів"
    )
    
    printSeparator("ОБРОБКА ЗАМОВЛЕНЬ (ПОЛІМОРФІЗМ)")
    
    orderAmount = 5000.0
    
    processOrder(regularCustomer, orderAmount)
    processOrder(premiumCustomer, orderAmount)
    processOrder(vipCustomer, orderAmount)
    
    printSeparator("ПРОГРАМА ЛОЯЛЬНОСТІ")
    
    print(f"\n{vipCustomer.getFullName()}:")
    vipCustomer.addPoints(250)
    vipCustomer.useVipLounge()
    
    printSeparator("ДОДАТКОВІ ПОСЛУГИ")
    
    premiumCustomer.getPremiumSupport()
    vipCustomer.assignPersonalManager("Олена Сидоренко")
    
    printSeparator("СТАТИСТИКА")
    print(f"\nЗагальна кількість клієнтів в системі: {Customer.getTotalCustomers()}")
    
    
    print(f"\nПовне ім'я: {vipCustomer.getFullName()}")
    print(f"ID клієнта: {vipCustomer.getCustomerId()}")
    print(f"Email: {vipCustomer.getEmail()}")
    
    vipCustomer.setEmail("new.email@example.com")
    print(f"Email оновлено: {vipCustomer.getEmail()}")
    

main()