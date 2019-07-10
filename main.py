# -*- encode: utf8 -*-
from datetime import date

from dsl.FilmManager import FilmManager

if __name__ == '__main__':
    manager: FilmManager = FilmManager()\
        .title("MCU - Marvel Cinematic Universe")\
        .film().title("Spider Man - Homecoming")\
            .release_date(date.today())\
            .realisation_date(date.fromisoformat("2010-12-25"))\
            .actor("Samuel L.", "Jackson", "Nick Furry")\
            .actor("Tom", "Holland", "Peter Parker / Spider Man")\
            .producer("Le", "producteur").producer("Le deuxième", "producteur")\
            .director("Le", "réalisateur").director("Le deuxième", "réalisateur")\
            .build()

    print(manager)


