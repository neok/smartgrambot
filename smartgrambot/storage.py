import pickle
import os


class FileObjectStorage:

    def save(self, filename, object):
        try:
            with open(filename, 'wb') as output:
                pickle.dump(object, output, pickle.HIGHEST_PROTOCOL)
        except Exception as e:
            pass

    def get_file(self, filename):
        pass
