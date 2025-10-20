from Product import Product

from constants import BATCH_SIZE


def row_to_product(row):
  return Product(
      row['Index'],
      row['Name'],
      row['Description'],
      row['Brand'],
      row['Category'],
      row['Price'],
      row['Currency'],
      row['Stock'],
      row['EAN'],
      row['Color'],
      row['Size'],
      row['Availability'],
      row['Internal ID'],
      row['row_size']
  )


def reduce_to_accum(
    accum: list[Product],
    prev: Product,
    next: Product
) -> Product:
  accum.append(prev)
  accum.append(next)
  if sum(list(map(lambda x: x.row_size, accum))) > BATCH_SIZE:
    print(len(accum))
    accum.clear()
  return prev
