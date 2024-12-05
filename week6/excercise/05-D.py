from dataclasses import dataclass

@dataclass
class Relation:
    name: str
    age: int
    nexus: str

    def compare(self, other):
        if not isinstance(other, Relation):
            return NotImplemented
        return self.name == other.name and self.age == other.age and self.nexus == other.nexus

quads = input().split(sep=",")
species = []
for specie in quads:
    specie = specie.strip().split(sep=" ")
    species.append(Relation(specie[0], int(specie[1]), specie[2]))

final = [item for specie in species for item in (species[0].compare(specie), str(specie))]

print(final)