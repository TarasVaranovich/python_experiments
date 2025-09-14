import gzip
import io
from contextlib import AbstractContextManager


class GzipArchiver(AbstractContextManager):
  def __init__(self, file_prefix, file_size):
    self._source_file_name = file_prefix
    self._file_size = file_size
    self._file_name_counter = 0
    self._file_size_counter = 0
    self._buffer = io.BytesIO()
    self._gzip_file = gzip.open(self._buffer, "wb")
    self._destination_archive = open(
        f"output_part_{self._file_name_counter:04d}.csv.gz",
        "wb",
        8192
    )

  def __exit__(self, exc_type, exc_value, traceback):
    self._gzip_file.close()
    self._destination_archive.write(self._buffer.getvalue())
    self._destination_archive.close()
    self._buffer.close()

  def write(self, line: str):
    self._gzip_file.write(line.encode("utf-8"))
    self._file_size_counter += self._buffer.tell()
    self._destination_archive.write(self._buffer.getvalue())
    self._buffer.seek(0)
    self._buffer.truncate()
    if self._file_size_counter >= self._file_size:
      self._gzip_file.close()
      self._destination_archive.write(self._buffer.getvalue())
      self._destination_archive.close()
      self._buffer.seek(0)
      self._buffer.truncate()
      self._gzip_file = gzip.open(self._buffer, "wb")
      self._file_name_counter += 1
      self._file_size_counter = 0
      self._destination_archive = open(
          f"output_part_{self._file_name_counter:04d}.csv.gz",
          "wb",
          8192
      )

# TODO: apply properties instead of getters
def main():
  print("Starting the zipping process...")
  with (
    open("annual-enterprise-survey-2024-financial-year-provisional.csv", "rt",
         1) as source_file,
    GzipArchiver("output_part", 50000) as archiver
  ):
    for line in source_file:
      archiver.write(line)


main()
