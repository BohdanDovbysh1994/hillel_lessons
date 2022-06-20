from xml.etree import ElementTree


class Movie:
    def __init__(
            self, title: str, format: str, year: int, rating: str, description: str):
        self.title = title
        self.format = format
        self.year = year
        self.rating = rating
        self.description = description

    @classmethod
    def from_xml(cls, path: str):
        tree = ElementTree.parse(path)
        collection = tree.getroot()
        movies = []
        for movie in collection.iter('movie'):
            data = {"title": movie.attrib["title"]}
            for child in movie:
                data[child.tag] = child.text
            movies.append(cls(**data))
        return movies

    def __str__(self):
        data = ""
        for key, value in self.__dict__.items():
            data += f"\t{key}: {value}\n"
        return f"{{\n{data[:len(data)]}\n}}"


if __name__ == '__main__':
    movies = Movie.from_xml("example_xml.xml")
    for movie in movies:
        print(movie)
