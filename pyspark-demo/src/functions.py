from Product import Product


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
