# 1
class Money:
	def __init__(self, whole = 0, cents = 0):
		self.whole = int(whole)
		self.cents = int(cents)
		self.normalize()

	def normalize(self):
		total_cents = self.whole * 100 + self.cents
		self.whole = total_cents // 100
		self.cents = total_cents % 100
		if self.whole == 0 and self.cents < 0:
			self.whole -= 1
			self.cents += 100

	def set_values(self, whole, cents):
		self.whole = int(whole)
		self.cents = int(cents)
		self.normalize()

	def __str__(self):
		total = self.to_cents()
		sign = ''
		if total < 0:
			sign = '-'
		w = abs(total) // 100
		c = abs(total) % 100
		return f"{sign}{w}.{c:02d}"

	def to_cents(self):
		return self.whole * 100 + self.cents

	def __sub__(self, other):
		if isinstance(other, Money):
			total_cents = self.to_cents() - other.to_cents()
			return Money(total_cents // 100, total_cents % 100)
		elif isinstance(other, (int, float)):
			delta = int(round(float(other) * 100))
			total_cents = self.to_cents() - delta
			return Money(total_cents // 100, total_cents % 100)
		return NotImplemented

	def __add__(self, other):
		if isinstance(other, Money):
			total_cents = self.to_cents() + other.to_cents()
			return Money(total_cents // 100, total_cents % 100)
		elif isinstance(other, (int, float)):
			delta = int(round(float(other) * 100))
			total_cents = self.to_cents() + delta
			return Money(total_cents // 100, total_cents % 100)
		return NotImplemented

	def __iadd__(self, other):
		res = self + other
		self.whole, self.cents = res.whole, res.cents
		return self

	def __isub__(self, other):
		res = self - other
		self.whole, self.cents = res.whole, res.cents
		return self


class Product:
	def __init__(self, name, price):
		self.name = name
		self.price = price

	def reduce_price(self, amount):
		self.price -= amount

	def __str__(self):
		return f"{self.name}: {self.price}"


# 2
import math


class Circle:
	def __init__(self, radius):
		self.radius = float(radius)

	def circumference(self):
		return 2 * math.pi * self.radius

	def __eq__(self, other):
		if isinstance(other, Circle):
			return math.isclose(self.radius, other.radius, rel_tol=1e-9, abs_tol=1e-12)
		return NotImplemented

	def __lt__(self, other):
		if isinstance(other, Circle):
			return self.circumference() < other.circumference()
		return NotImplemented

	def __le__(self, other):
		if isinstance(other, Circle):
			return self.circumference() <= other.circumference()
		return NotImplemented

	def __gt__(self, other):
		if isinstance(other, Circle):
			return self.circumference() > other.circumference()
		return NotImplemented

	def __ge__(self, other):
		if isinstance(other, Circle):
			return self.circumference() >= other.circumference()
		return NotImplemented

	def __add__(self, value):
		if isinstance(value, (int, float)):
			return Circle(self.radius + float(value))
		return NotImplemented

	def __sub__(self, value):
		if isinstance(value, (int, float)):
			return Circle(self.radius - float(value))
		return NotImplemented

	def __iadd__(self, value):
		if isinstance(value, (int, float)):
			self.radius += float(value)
			return self
		return NotImplemented

	def __isub__(self, value):
		if isinstance(value, (int, float)):
			self.radius -= float(value)
			return self
		return NotImplemented


# 3
class Airplane:
	def __init__(self, plane_type, max_passengers, passengers = 0):
		self.plane_type = plane_type
		self.max_passengers = int(max_passengers)
		self.passengers = max(0, min(int(passengers), self.max_passengers))

	def __eq__(self, other):
		if isinstance(other, Airplane):
			return self.plane_type == other.plane_type
		return NotImplemented

	def __lt__(self, other):
		if isinstance(other, Airplane):
			return self.max_passengers < other.max_passengers
		return NotImplemented

	def __le__(self, other):
		if isinstance(other, Airplane):
			return self.max_passengers <= other.max_passengers
		return NotImplemented

	def __gt__(self, other):
		if isinstance(other, Airplane):
			return self.max_passengers > other.max_passengers
		return NotImplemented

	def __ge__(self, other):
		if isinstance(other, Airplane):
			return self.max_passengers >= other.max_passengers
		return NotImplemented

	def __add__(self, value):
		if isinstance(value, int):
			new_passengers = max(0, min(self.passengers + value, self.max_passengers))
			return Airplane(self.plane_type, self.max_passengers, new_passengers)
		return NotImplemented

	def __sub__(self, value):
		if isinstance(value, int):
			new_passengers = max(0, min(self.passengers - value, self.max_passengers))
			return Airplane(self.plane_type, self.max_passengers, new_passengers)
		return NotImplemented

	def __iadd__(self, value):
		if isinstance(value, int):
			self.passengers = max(0, min(self.passengers + value, self.max_passengers))
			return self
		return NotImplemented

	def __isub__(self, value):
		if isinstance(value, int):
			self.passengers = max(0, min(self.passengers - value, self.max_passengers))
			return self
		return NotImplemented


# 4
class Flat:
	def __init__(self, area, price):
		self.area = float(area)
		self.price = float(price)

	def __eq__(self, other):
		if isinstance(other, Flat):
			return math.isclose(self.area, other.area, rel_tol=1e-9, abs_tol=1e-12)
		return NotImplemented

	def __ne__(self, other):
		if isinstance(other, Flat):
			return not self.__eq__(other)
		return NotImplemented

	def __lt__(self, other):
		if isinstance(other, Flat):
			return self.price < other.price
		return NotImplemented

	def __le__(self, other):
		if isinstance(other, Flat):
			return self.price <= other.price
		return NotImplemented

	def __gt__(self, other):
		if isinstance(other, Flat):
			return self.price > other.price
		return NotImplemented

	def __ge__(self, other):
		if isinstance(other, Flat):
			return self.price >= other.price
		return NotImplemented

