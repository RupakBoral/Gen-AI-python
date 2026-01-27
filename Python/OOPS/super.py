class Base:
    value: str
    type: str

    def __init__(self, value, type_):
        self.value = value
        self.type = type_


class Derived(Base):
    name: str

    def __init__(self, value, type_, name):
        super().__init__(value, type_)
        self.name = name


obj = Derived(type_="integer", value="10", name="Rupak")
print(obj.value)
print(obj.type)
print(obj.name)
