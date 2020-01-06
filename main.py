class Animal():
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.product = 0
    def feed(self):
        print(f'You just given {self.name} some food')
        self.product += 1
    def recognize_voice(self):
        if self.noize == 'honk':
            print('It is a goose!', self.noize)
        elif self.noize == 'coc':
            print('It is a hen!', self.noize)
        elif self.noize == 'krya':
            print('It is a duck!', self.noize)

class Bird(Animal):
    def collect_eggs(self):
        if self.product == 0:
            print('feed first')
        else:
            print(f'You just collected {self.product} eggs')
            self.product = 0

class Goose(Bird):
    noize = 'honk'

class Hen(Bird):
    noize = 'coc'

class Duck(Bird):
    noize = 'krya'

class Mammal(Animal):
    def get_milk(self):
        if self.product == 0:
            print('feed first')
        else:
            print(f'You took {self.product} milk buckets')
            self.product = 0

class Cow(Mammal):
    noize = 'moo'

class Goat(Mammal):
    noize = 'bee'

class Woolen(Animal):
    def grab_wool(self):
        if self.product == 0:
            print('feed first')
        else:
            print(f'Now you have {self.product} kg of wool')
            self.product = 0

class Sheep(Woolen):
    noize = 'mee'

seriy = Goose('Seriy', 4)
beliy = Goose('Beliy', 6)
barashek = Sheep('Barashek', 44)
kudryaviy = Sheep('Kudryaviy', 29)
manka = Cow('Manka', 100)
coco = Hen('Co-co', 2)
kukareku = Hen('kukareku', 3)
roga = Goat('Roga', 50)
kopita = Goat('Kopita', 39)
kryaqua = Duck('kryaqua', 3)

x = [seriy, beliy, barashek, kudryaviy, manka, coco, kukareku, roga, kopita, kryaqua]

def total_weight():
    weight = 0
    for animal in x:
        weight += animal.weight
    print(weight)

def max():
    weight = x[0].weight
    for animal in x[1:]:
        if animal.weight > weight:
            weight = animal.weight
    print(weight)
