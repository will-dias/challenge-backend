from odmantic import Model, ObjectId


class CatalogProduct(Model):
    title: str
    description: str
    price: float


class Catalog(Model):
    category_title: str
    category_description: str
    itens: list[CatalogProduct]


class CatalogResponse(Model):
    owner: ObjectId
    catalog: list[Catalog]
