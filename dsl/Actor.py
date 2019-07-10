from dsl.Person import Person


class Actor(Person):
    def __init__(self, film):
        super().__init__(film, Person.ACTOR)
        self._role_: str or None = None

    def in_role(self, role: str):
        self._role_ = role
        return self

    def role(self) -> str or None:
        return self._role_

    def __str__(self):
        return super().__str__() + (" in the role of " + self.role() if self.role() is not None else "")
