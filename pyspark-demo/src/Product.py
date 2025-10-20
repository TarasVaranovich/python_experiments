class Product:
  def __init__(
      self,
      index,
      name,
      description,
      brand,
      category,
      price,
      currency,
      stock,
      ean,
      color,
      size,
      availability,
      internal_id,
      row_size
  ):
    self.__index: int = index
    self.__name: str = name
    self.__description: str = description
    self.__brand: str = brand
    self.__category: str = category
    self.__price: float = price
    self.__currency: str = currency
    self.__stock: int = stock
    self.__ean: int = ean
    self.__color: str = color
    self.__size: str = size
    self.__availability: str = availability
    self.__internal_id: int = internal_id
    self.__row_size: int = row_size

  @property
  def index(self) -> int:
    return self.__index

  @property
  def name(self) -> str:
    return self.__name

  @property
  def brand(self) -> str:
    return self.__brand

  @property
  def category(self) -> str:
    return self.__category

  @property
  def price(self) -> float:
    return self.__price

  @property
  def currency(self) -> str:
    return self.__currency

  @property
  def stock(self) -> int:
    return self.__stock

  @property
  def ean(self) -> int:
    return self.__ean

  @property
  def color(self) -> str:
    return self.__color

  @property
  def size(self) -> str:
    return self.__size

  @property
  def availability(self) -> str:
    return self.__availability

  @property
  def internal_id(self) -> int:
    return self.__internal_id

  @property
  def row_size(self) -> int:
    return self.__row_size

  def __repr__(self):
    return (f"Product("
            f"index={self.__index}, "
            f"name={self.__name}, "
            f"description={self.__description}, "
            f"brand={self.__brand}, "
            f"category={self.__category}, "
            f"price={self.__price},"
            f"currency={self.__currency}, "
            f"stock={self.__stock}, "
            f"ean={self.__ean},"
            f"color={self.__color},"
            f"size={self.__size}, "
            f"availability={self.__availability}, "
            f"internal_id={self.__internal_id},"
            f"row_size={self.__row_size}"
            f")"
            )
