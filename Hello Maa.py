from os import environ

name=environ.get('NAME','WORLD')
print('Hello {}'.format(name))
