import zipfile
import time
import os

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['C:\\Cods', 'C:\\Docs']

# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'E:\\диск1\\YandexDisk\\Backup'

# 3. Файлы помещаются в zip-архив.
# 4. Именем для zip-архива служит текущая дата и время.
today = target_dir + os.sep + time.strftime('%Y%m%d')
# Текущее время служит именем zip-архива
now = time.strftime('%H%M%S')

# Запрашиваем комментарий пользователя для имени файла
comment = input('Введите комментарий --> ')
if len(comment) == 0:  # проверяем, введён ли комментарий
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

# Создаём каталог, если его ещё нет
if not os.path.exists(today):
    os.mkdir(today)  # создание каталога
    print('Каталог успешно создан', today)

# Запускаем создание резервной копии

try:
    # Обход всего дерева директории и сжатие файлов в каждой папке
    my_zip = zipfile.ZipFile(target, 'w')
    print('Архив создан в ' + target)
    for select_folder in source:
        archDirName = ''
        for dir, subdirs, files in os.walk(select_folder):
            # Имя текущей директории в архиве
            archDirName = os.sep.join([archDirName, os.path.basename(dir)]).strip(os.sep)
            # Добавить в архив текущую директорию
            my_zip.write(dir, archDirName)
            # Добавить в архив все файлы из текущей директории
            for file in files:
                # Имя текущего файла в архиве
                archFileName = archDirName + os.sep + file
                my_zip.write(os.path.join(dir, file), archFileName)
except ValueError:
    print('Тут что-то не так, переделывай')
