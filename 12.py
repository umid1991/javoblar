car0 = {
        'model':'lasit',
        'rang':'op',
        'yil':'2008',
        'narh':'1300',
        'km':'5000',
        'karopka':'avtomat'
        }

car1 = {
        'model':'nehiy',
        'rang':'op',
        'yil':'2008',
        'narh':'1300',
        'km':'5000',
        'karopka':'avtomat'
        }

car2 = {
        'model':'gentra',
        'rang':'op',
        'yil':'2008',
        'narh':'1300',
        'km':'5000',
        'karopka':'avtomat'
        }

# car = car0
# print(f"{car['model'].title()}, "
#       f"{car['rang']} rang, "
#       f"{car['yil']}-yil, {car['narh']}$"
#       )


cars = [car0, car1, car2]

# for car in cars:
#     print(f"{car['model'].title()}, "
#            f"{car['rang']} rang, "
#            f"{car['yil']}-yil, {car['narh']}$"
#            )

dasturchi = {
    'ali':['python', 'c++'],
    'vali':['html', 'c++'],
    'shali':['php', 'c++'],
    'ahmat':['c==', 'c++'],
    'tuhmat':['python', 'c++'],
    }

for ism, tillar in dasturchi.items():
    print(f"\n {ism.title()} quydagi daturlash tillarin biladi")
    for til in tillar:
        print(til.upper())