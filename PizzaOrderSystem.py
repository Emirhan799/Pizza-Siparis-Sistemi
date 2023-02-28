import csv
import datetime

# menü listesinin Menu.txt'den okunması
def read_menu_list():
    with open('Menu.txt', 'r') as menu_file:
        print(menu_file.read())

# main fonksiyonu (menüyü çağırır)
def main():
    read_menu_list()
    
# Pizza süper sınıfı
class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    # pizza açıklamasının okunması
    def get_description(self):
        return self.description

    # pizza fiyatının okunması
    def get_cost(self):
        return self.cost

# pizza çeşitleri, Pizza alt sınıfları
class KlasikPizza(Pizza):

    # pizza açıklaması ve fiyatı 
    def __init__(self):
        super().__init__('Klasik Pizza', 90.0)

class MargaritaPizza(Pizza):
    def __init__(self):
        super().__init__('Margarita Pizza', 110.0)

class TurkPizza(Pizza):
    def __init__(self):
        super().__init__('Türk Pizza', 100.0)

class SadePizza(Pizza):
    def __init__(self):
        super().__init__('Sade Pizza', 100.0)

# sosların süper sınıfı, Pizza'nın alt sınıfı
class Decorator(Pizza):
    def __init__(self, component, description, cost):
        super().__init__(description, cost)
        self.component = component

    # seçilen pizza ve sosun fiyarlarının toplanıp geri döndürülmesi
    def get_cost(self):
        return self.component.get_cost() + super().get_cost()

    # seçilen pizza ve sosun açıklamalarının geri döndürülmesi
    def get_description(self):
        return super().get_description() + ' ' + self.component.get_description()

# sos çeşitleri, Decorator'un alt sınıfı
class Olives(Decorator):
    # sos açıklaması ve fiyatı
    def __init__(self, component):
        super().__init__(component, 'Zeytinli', 5.0)

class Mushrooms(Decorator):
    def __init__(self, component):
        super().__init__(component, 'Mantarlı',7.0)

class GoatCheese(Decorator):
    def __init__(self, component):
        super().__init__(component, 'Keçi peynirli',10.0)

class Meat(Decorator):
    def __init__(self, component):
        super().__init__(component, 'Etli',15.0)

class Onions(Decorator):
    def __init__(self, component):
        super().__init__(component, 'Soğanlı',7.0)

class Corn(Decorator):
    def __init__(self, component):
        super().__init__(component, 'Mısırlı',5.0)

# main foksiyonu çağırılması (menünün yazılması)
if __name__ == '__main__':
    main()

# pizza seçimi koşulu sağlamıyorsa tekrar sor
while True:
    
    pizza_choice = int(input('Pizza seçiniz (1-4): '))

    # gelen veriye göre pizza seç
    if pizza_choice == 1:
        pizza = KlasikPizza()
        break
    elif pizza_choice == 2:
        pizza = MargaritaPizza()
        break
    elif pizza_choice == 3:
        pizza = TurkPizza()
        break
    elif pizza_choice == 4:
        pizza = SadePizza()
        break
    else:
        print('Geçersiz pizza kodu.\n')

# sos seçimi koşulu sağlamıyorsa tekrar sorr
while True:
    
    sauce_choice = int(input('Sos seçiniz (11-16): '))

    if sauce_choice == 11:
        sauce = Olives(pizza)
        break
    elif sauce_choice == 12:
        sauce = Mushrooms(pizza)
        break
    elif sauce_choice == 13:
        sauce = GoatCheese(pizza)
        break
    elif sauce_choice == 14:
        sauce = Meat(pizza)
        break
    elif sauce_choice == 15:
        sauce = Onions(pizza)
        break
    elif sauce_choice == 16:
        sauce = Corn(pizza)
        break
    else:   
        print('Geçersiz sos kodu.\n')


total_cost = sauce.get_cost()

# pizza, sos seçimini ve toplam fiyatı yazdır
print(f'\nSeçiminiz : {sauce.get_description()}\nToplam tutar: {total_cost:.2f} TL\n')

# sipariş onayı iste
aprvl = input('Siparişi Onayla (e/h)')

# onay verilir ise gir
if aprvl == 'e':
    
    name = input('\nLütfen isminizi giriniz: ')

    # TC no denetimi yap doğru değil ise tekrar sor
    while True:
        try:
            id_num = int(input('Lütfen TC kimlik numaranızı giriniz: '))
            if len(str(id_num)) == 11:
                break
            else:
                print('TC kimlik numarası 11 haneli ve rakamlardan oluşmalıdır\n')
        except:
            print('TC kimlik numarası 11 haneli ve rakamlardan oluşmalıdır\n')

    # CC no denetimi yap doğru değil ise tekrar sor        
    while True:
        try:
            cc_num = int(input('Lütfen kredi kartı numaranızı giriniz: '))
            if len(str(cc_num)) == 16:
                break
            else:
                print('Kart numarası 16 haneli ve rakamlardan oluşmalıdır\n')
        except:
            print('Kart numarası 16 haneli ve rakamlardan oluşmalıdır\n')
            
    cc_password = input('Lütfen kredi kartı şifrenizi giriniz: ')
    
    # şuanın tarihini al ve formata uygun hale getir
    now = datetime.datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    
    # csv dosyasını aç eğer yok ise oluştur ve kullanıcı bilgilerini, siparişi, tutarı ve zamanı yaz
    with open('Orders_Database.csv', 'a') as db_file:
        db_writer = csv.writer(db_file)
        db_writer.writerow([name, id_num, sauce.get_description(), total_cost, cc_num, cc_password, dt_string])
    
    print(f'\nTeşekkürler {name}! {sauce.get_description()} siparişiniz alınmıştır.')
    print(f'Toplam tutar: {total_cost:.2f} TL')

# onay verilmez ise iptal et ve çık
else:
    print('Seçiminiz iptal edildi')
    exit


















