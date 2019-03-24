from os import environ

name=environ.get('NAME')
print('Hello {}'.format(name))
