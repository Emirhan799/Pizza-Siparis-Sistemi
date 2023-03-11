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


def Name_control(value):
    return not any(char.isdigit() for char in value)


def TC_control(value):
    value = str(value)
    
    # 11 hanelidir.
    if not len(value) == 11:
        return False
    
    # Sadece rakamlardan olusur.
    if not value.isdigit():
        return False
    
    # Ilk hanesi 0 olamaz.
    if int(value[0]) == 0:
        return False
    
    digits = [int(d) for d in str(value)]
    
    # 1. 2. 3. 4. 5. 6. 7. 8. 9. ve 10. hanelerin toplamından elde edilen sonucun
    # 10'a bölümünden kalan, yani Mod10'u bize 11. haneyi verir.
    if not sum(digits[:10]) % 10 == digits[10]:
        return False
    
    # 1. 3. 5. 7. ve 9. hanelerin toplamının 7 katından, 2. 4. 6. ve 8. hanelerin toplamı çıkartıldığında,
    # elde edilen sonucun 10'a bölümünden kalan, yani Mod10'u bize 10. haneyi verir.
    if not (((7 * sum(digits[:9][-1::-2])) - sum(digits[:9][-2::-2])) % 10) == digits[9]:
        return False
    
    # Butun kontrollerden gecti.
    return True


def CC_control(value):
    value = str(value)
    
    # 16 hanelidir.
    if not len(value) == 16:
        return False
    
    # Sadece rakamlardan olusur.
    if not value.isdigit():
        return False
    
    # Butun kontrollerden gecti.
    return True


def CC_pass_control(value):
    value = str(value)
    
    # 4 hanelidir.
    if not len(value) == 4:
        return False
    
    # Sadece rakamlardan olusur.
    if not value.isdigit():
        return False
    
    # Butun kontrollerden gecti.
    return True


# şuanın tarihini al ve formata uygun hale getir
def Time():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")


# main foksiyonu çağırılması (menünün yazılması)
if __name__ == '__main__':
    main()

# pizza seçimi koşulu sağlamıyorsa tekrar sor
while True:
    try:
        pizza_choice = int(input('Pizza seçiniz (1-4): '))
    except:
        print('Geçersiz pizza kodu.\n')
    else:
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
    

# sos seçimi koşulu sağlamıyorsa tekrar sor
while True:
    try:
        sauce_choice = int(input('Sos seçiniz (11-16): '))
    except:
        print('Geçersiz sos kodu.\n')
    else:
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

# sipariş onayı kontrol
while True:
    # sipariş onayı iste
    aprvl = input('Siparişi Onayla (e/h)').lower()

    # onay verilir ise gir
    if aprvl == 'e':
        
        #isim kontrol
        while True:
            name = input('\nLütfen isminizi giriniz: ')
            if Name_control(name) is True:
                break
            else:
                print('İsim rakam içeremez')

        #TC No kontrol
        while True:
            id_num = input('Lütfen TC kimlik numaranızı giriniz: ')
            if TC_control(id_num) is True:
                break
            else:
                print('Hatalı TC NO\n')

        #CC No kontrol
        while True:
            cc_num = input('Lütfen kredi kartı numaranızı giriniz: ')
            if CC_control(cc_num) is True:
                break
            else:
                print('Kart numarası 16 haneli ve rakamlardan oluşmalıdır\n')

        #CC password kontrol
        while True:
            cc_password = input('Lütfen kredi kartı şifrenizi giriniz: ')
            if CC_pass_control(cc_password) is True:
                break
            else:
                print('Kart şifresi 4 haneli ve rakamlardan oluşmalıdır\n')

        
        dt_string = Time()

        # csv dosyasını aç eğer yok ise oluştur ve kullanıcı bilgilerini, siparişi, tutarı ve zamanı yaz
        with open('Orders_Database.csv', 'a') as db_file:
            db_writer = csv.writer(db_file)
            db_writer.writerow([name, id_num, sauce.get_description(), total_cost, cc_num, cc_password, dt_string])

        print(f'\nTeşekkürler {name}! {sauce.get_description()} siparişiniz alınmıştır.')
        print(f'Toplam tutar: {total_cost:.2f} TL')
        break

    # onay verilmez ise iptal et ve çık
    elif aprvl == 'h':
        print('Seçiminiz iptal edildi')
        break
    else:
        print('\nHatalı giriş\nLütfen tekrar giriniz.\n')

