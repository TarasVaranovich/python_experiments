import csv
import io

from Product import Product
from constants import BATCH_SIZE
from constants import DESTINATION_DIR


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


def product_to_csv(product: Product) -> str:
  output = io.StringIO()
  writer = csv.writer(output)
  writer.writerow([
    product.index,
    product.name,
    product.description,
    product.brand,
    product.category,
    product.price,
    product.currency,
    product.stock,
    product.ean,
    product.color,
    product.size,
    product.availability,
    product.internal_id
  ])
  return output.getvalue().rstrip('\r\n')


def reduce_to_accum(
    batch_counter: int,
    accum: list[Product],
    prev: Product,
    next: Product
) -> Product:
  accum.append(prev)
  accum.append(next)
  if sum(list(map(lambda x: x.row_size, accum))) > BATCH_SIZE:
    print(len(accum))
    batch_counter = batch_counter + 1
    with open(f"{DESTINATION_DIR}_{batch_counter}.csv", "wt", 8192) as f:
      for row in accum:
        f.write(product_to_csv(row))
      f.close()
    accum.clear()
  return prev
