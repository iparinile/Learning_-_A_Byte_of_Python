import sys

print('Аргументы командной строки:')
print(sys.argv)

for i in sys.argv:
    print(i)
print('\n\nПеременная PYTHONPATH содержит', sys.path, '\n')
