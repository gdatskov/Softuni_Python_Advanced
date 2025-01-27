from project.movie_specification.movie import Movie


class Action(Movie):
    DEFAULT_AGE_RESTRICTION = 12

    def __init__(self, title, year, owner, age_restriction=DEFAULT_AGE_RESTRICTION):
        # if age_restriction < self.DEFAULT_AGE_RESTRICTION:
        #     raise ValueError("Action movies must be restricted for audience under 12 years!")
        super().__init__(title, year, owner, age_restriction)

    def details(self):
        return f"Action - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, " \
               f"Likes:{self.likes}, Owned by:{self.owner.username}"

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < 12:
            raise ValueError("Action movies must be restricted for audience under 12 years!")
        self.__age_restriction = value