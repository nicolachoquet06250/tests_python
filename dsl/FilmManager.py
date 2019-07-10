from dsl.Film import Film


class FilmManager(object):

    def __init__(self):
        self.films: [Film] = []
        self._title_: str or None = None
        pass

    def film(self, title: str or None = None) -> Film or None:
        if title is None:
            return Film(self)
        for film in self.films:
            if film.title() is title:
                return film
        return None

    def title(self, title: str or None = None):
        if title is None:
            return self._title_
        self._title_ = title
        return self

    def __str__(self):
        films_string = " == " + self.title() + " == \n"
        for film in self.films:
            films_string += " - " + str(film)
        return films_string
