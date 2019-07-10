from datetime import date

from dsl.Actor import Actor
from dsl.Builder import Builder
from dsl.Person import Person


class Film(Builder):

    def __init__(self, manager):
        self.manager = manager
        self._producers_: [Person] = []
        self._directors_: [Person] = []
        self._casting_: [Actor] = []
        self.realisationDate: str or None = None
        self.releaseDate: str or None = None
        self._title_: str or None = None

    def producer(self, first_name: str or None = None, last_name: str or None = None):
        if first_name is None and last_name is None:
            return Person(self, Person.PRODUCER)
        else:
            producer: Person = Person(self, Person.PRODUCER)
            if first_name is not None:
                producer.first_name(first_name)
            if last_name is not None:
                producer.last_name(last_name)
            if last_name is not None and first_name is not None:
                producer.build()
            return self

    def actor(self, first_name: str or None = None, last_name: str or None = None, role: str or None = None):
        if first_name is None and last_name is None and role is None:
            return Actor(self)
        else:
            actor: Actor = Actor(self)
            if first_name is not None:
                actor.first_name(first_name)
            if last_name is not None:
                actor.last_name(last_name)
            if role is not None:
                actor.in_role(role)
            if last_name is not None and first_name is not None and role is not None:
                actor.build()
            return self

    def director(self, first_name: str or None = None, last_name: str or None = None):
        if first_name is None and last_name is None:
            return Person(self, Person.DIRECTOR)
        else:
            director: Person = Person(self, Person.DIRECTOR)
            if first_name is not None:
                director.first_name(first_name)
            if last_name is not None:
                director.last_name(last_name)
            if last_name is not None and first_name is not None:
                director.build()
            return self

    def producers(self):
        return self._producers_

    def casting(self):
        return self._casting_

    def directors(self):
        return self._directors_

    def title(self, title: str or None = None) -> str or None:
        if title is None:
            return self._title_
        self._title_ = title
        return self

    def realisation_date(self, realisation_date: date or None = None):
        if realisation_date is None:
            return self.realisationDate
        self.realisationDate = realisation_date
        return self

    def release_date(self, release_date: date or None = None):
        if release_date is None:
            return self.releaseDate
        self.releaseDate = release_date
        return self

    def build(self):
        self.manager.films.append(self)
        return self.manager

    def __str__(self):
        film_string = ""
        realisation_date: date = self.realisation_date()
        release_date: date = self.release_date()

        film_string += self.title() + " - " \
            + ("0" + str(release_date.day) if release_date.day < 10 else str(release_date.day)) + "/" \
            + ("0" + str(release_date.month) if release_date.month < 10 else str(release_date.month)) + "/" \
            + str(release_date.year) + "\n"
        film_string += "\t- Realised on " + ("0" + str(realisation_date.day) if realisation_date.day < 10 else str(realisation_date.day)) + "/" \
            + ("0" + str(realisation_date.month) if realisation_date.month < 10 else str(realisation_date.month)) + "/" \
            + str(realisation_date.year) + "\n"
        film_string += "\t- Directed by "

        if self.directors().__len__() > 1:
            film_string += ": \n"
            for director in self.directors():
                film_string += "\t\t - " + str(director) + "\n"
        elif self.directors().__len__() is 1:
            film_string += str(self.directors()[0]) + "\n"

        film_string += "\t- Produced by "
        if self.producers().__len__() > 1:
            film_string += ": \n"
            for producer in self.producers():
                film_string += "\t\t - " + str(producer) + "\n"
        elif self.producers().__len__() is 1:
            film_string += str(self.producers()[0]) + "\n"

        film_string += "\t- With actors :\n"
        for actor in self.casting():
            film_string += "\t\t- " + str(actor) + "\n"
        return film_string
