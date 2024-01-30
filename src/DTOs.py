class Product:
    def __init__(self, id, title, description, price, thumbnail, category):
        self.id = id
        self.title = title
        self.description = description
        self.price = price
        self.thumbnail = thumbnail
        self.category = category

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "thumbnail": self.thumbnail,
            "category": self.category,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            title=data["title"],
            description=data["description"],
            price=data["price"],
            thumbnail=data["thumbnail"],
            category=data["category"],
        )

    def __repr__(self):
        return f"Product(id={self.id}, title={self.title})"


class Category:
    def __init__(self, name):
        self.name = name
