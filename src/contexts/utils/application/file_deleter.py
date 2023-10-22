import os


class FileDeleter:
    def delete(self, filename: str):
        try:
            if os.path.exists(filename):
                os.remove(filename)
            else:
                raise Exception(f"File {filename} not found")
        except Exception as e:
            raise e
