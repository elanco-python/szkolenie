
# przeciązanie operatorów

class Vector:

    def __init__(self, x ,y):
        self.x = x
        self.y = y

    def add_vector(self, other_vector):
        return Vector( self.x+other_vector.x , self.y+other_vector.y )

    def __str__(self):
        return f"[ {self.x}, {self.y} ]"

    def __add__(self, other):
        if type(other) is Vector:
            return Vector( self.x+other.x , self.y+other.y )
        if type(other) in [int, float]:
            return Vector(self.x + other, self.y + other)
        raise TypeError("Dupa")

    def __sub__(self, other):
        super.__sub__(other)

    def __lt__(self, other):
        pass

    def __eq__(self, other):
        return  self.x==other.x and self.y==other.y

class SuperVektor(Vector):
    def add_vector(self, other_vector):
        #return Vector( self.x-other_vector.x , self.y-other_vector.y )
        v = super().add_vector(other_vector)
        return Vector(-1*v.x, -1*v.y)

wektor1 = Vector(2, 3)
print(wektor1)
wektor2 = Vector(2, 3)
print(wektor2)
print("="*80)
print(wektor1.add_vector(wektor2))
print(wektor1+wektor2)
print(wektor1+3)
print(wektor1+3.0)

try:
    print(wektor1 + (-1,1) )
except Exception as exc:
    print(exc)

print(wektor1 == wektor2)

#wektor1.set(10, 10)

print("="*80)
sv1 = SuperVektor(2,2)
sv2 = SuperVektor(2,2)
print(sv1.add_vector(sv2))
