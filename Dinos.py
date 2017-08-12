import math

class Dino():
    _registry = []
    def __init__(self, name, leg_length, diet, stride_length, stance):
        self.name = name
        self.leg_length = float(leg_length)
        self.diet = diet
        self.stride_length = float(stride_length)
        self.stance = stance
        self._registry.append(self)

    def speed_calc(self):
        g = float(9.8)
        speed = ((self.stride_length / self.leg_length) - 1) * math.sqrt(self.leg_length * g)
        return speed

    def __str__(self):
        return self.name

    @staticmethod
    def pull_data():
        dinos = {}
        with open('dataset1.txt') as f1:
            for line in f1.readlines()[1:]:
                name, leg_length, diet = line.split(',')
                dinos[name] = [leg_length, diet.strip('\n')]
        with open('dataset2.txt') as f2:
            for line in f2.readlines()[1:]:
                name, stride_length, stance = line.split(',')
                dinos[name].append(stride_length)
                dinos[name].append(stance.strip('\n'))
        return dinos

    @classmethod
    def constructor(cls,k,v):
        dinospeed = {}
        name = k
        leg_length = v[0]
        diet = v[1]
        stride_length = v[2]
        stance = v[3]
        # v[0] =
        return cls(name,leg_length,diet,stride_length,stance)

    # @classmethod
    # def constructor(cls):
    #     dinospeed = {}
    #     for k,v in Dino.pull_data().items():
    #         k = Dino(k,v[0],v[1],v[2],v[3])
    #         k.speed = Dino.speed_calc(k)
    #         if k.stance == 'bipedal':
    #             dinospeed[k.name] = k.speed
    #     for k,v in sorted(dinospeed.items(),key=lambda x:x[1],reverse=True):
    #         print (k)

dinos = Dino.pull_data()

for k,v in dinos.items():
    dinospeed = {}
    dino = Dino.constructor(k,v)
    # print (dino.name,dino.stance)
    dino.speed = Dino.speed_calc(dino)
    if dino.stance == 'bipedal':
        dinospeed[dino.name] = dino.speed
    for k, v in sorted(dinospeed.items(), key=lambda x: x[1], reverse=True):
        print (k)
    # Hadrosaurus
    # Struthiomimus
    # Velociraptor
    # Tyrannosaurus Rex


for d in Dino._registry:
    print ('Dino name: ',d)