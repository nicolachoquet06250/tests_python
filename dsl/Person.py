from dsl.Builder import Builder


class Person(Builder):
    ACTOR = "actor"
    PRODUCER = "producer"
    DIRECTOR = "director"

    def __init__(self, film, person_type: str = "actor"):
        self.film = film
        self.personType: str = person_type
        self.firstName: str or None = None
        self.lastName: str or None = None

    def first_name(self, first_name: str or None = None):
        if first_name is None:
            return self.firstName
        self.firstName = first_name
        return self

    def last_name(self, last_name: str or None = None):
        if last_name is None:
            return self.lastName
        self.lastName = last_name
        return self

    def build(self):
        if self.personType is self.ACTOR:
            self.film.casting().append(self)
        elif self.personType is self.PRODUCER:
            self.film.producers().append(self)
        elif self.personType is self.DIRECTOR:
            self.film.directors().append(self)
        return self.film

    def __str__(self):
        return self.first_name() + " " + self.last_name()
