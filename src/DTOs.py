class ProductDTO:
    def __init__(self, product_id, title, description, price, thumbnail, category):
        self.product_id = product_id
        self.title = title
        self.description = description
        self.price = price
        self.thumbnail = thumbnail
        self.category = category
        self.category_id = None

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "thumbnail": self.thumbnail,
            "category_id": self.category_id,
        }

    @classmethod
    def from_dict(cls, data: dict):
        if "id" in data:
            data["product_id"] = data.pop("id")
        return cls(
            product_id=data["product_id"],
            title=data["title"],
            description=data["description"],
            price=data["price"],
            thumbnail=data["thumbnail"],
            category=data["category"],
        )

    def __repr__(self):
        return f"Product(id={self.product_id}, title={self.title})"


class CategoryDTO:
    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {
            "name": self.name,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
        )

    def __repr__(self):
        return f"Category(name={self.name})"
