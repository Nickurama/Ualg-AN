import member as Member

class polynomial:
    def __init__(self):
        self.members = []
    
    @classmethod
    def from_string(cls, str: str):
        tokens = str.split("+")

        new_polynomial = cls()
        for token in tokens:
            new_member = Member.member.from_string(token)
            new_polynomial.add(new_member)

        return new_polynomial


    def add(self, member: Member):
        self.members.append(member)

    def calc(self, x: float) -> float:
        result = 0.0
        for member in self.members:
            result += member.calc(x)
        return result