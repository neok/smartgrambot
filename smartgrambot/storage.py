import pickle
import os


class FileObjectStorage:

    def save(self, filename, object):
        try:
            with open(filename, 'wb') as output:
                pickle.dump(object, output, pickle.HIGHEST_PROTOCOL)
        except Exception as e:
            return False

    def file_exists(self, filename):

        return os.path.isfile(filename)

    def get_file(self, filename):

        try:
            with open(filename, 'rb') as fl:
                return pickle.load(fl)

        except Exception as e:
            return False
