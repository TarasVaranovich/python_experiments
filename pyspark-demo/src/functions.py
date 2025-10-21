import csv
import io
import time

from Product import Product
from constants import BATCH_SIZE
from constants import DESTINATION_DIR
from constants import FILE_BUFF


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


def row_size(*cols):
  return sum([len(str(c).encode('utf-8')) for c in cols])


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
  return output.getvalue()


def write_batches(
    accum: list[Product],
    prev: Product,
    next: Product
) -> Product:
  accum.append(prev)
  accum.append(next)
  if sum(list(map(lambda x: x.row_size, accum))) > BATCH_SIZE:
    f_size = sum(list(map(lambda x: x.row_size, accum)))
    with open(
        f"{DESTINATION_DIR}batch_size_{f_size}_{time.time_ns()}.csv", "wt", FILE_BUFF
    ) as f:
      for row in accum:
        f.write(product_to_csv(row))
      f.close()
      print(f"Written file size:{f_size}")
    accum.clear()
  return prev
