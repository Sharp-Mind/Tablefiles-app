# Приложение для просмотра табличных файлов / Application for viewing table files

### Language/Язык

- [English](#en_lang)
- [Русский](#ru_lang)

## <a name="ru_lang"></a> RU

### Описание

Приложения для добавления и просмотра .csv файлов, с защитой авторизацией. (Реализация через Docker находится в работе)

## Установка на локальный компьтер

1. Скопировать папку с проектом на локальный компьютер;
2. Создать виртуальное окружение и активировать его;
3. Установить зависимости командой

   ```bash
   pip install requirements.txt
   ```

4. Запустить проект командой

   ```bash
   python3 manage.py runserver
   ```

5. Перейти по адресу ```localhost:8000```, откроется форма авторизации;
6. Стандартный логин: ```admin```, стандартный пароль: ```admin```.

## Функционал

После авторизации, откроется форма добавления и просмотра списка файлов. После добавления файлов, их можно будет открывать по одному для просмотра, или удалить любой из них. Во время просмотра табличного файла можно выбирать количество строк на страницу и делать сортировку по одному столбцу в прямом или обратном порядке.

Просмотреть и удалить файл можно только авторизовавшись.

## Учётные записи

Откройте панель администратора, чтобы создать или изменить учётную запись: ```localhost:8000\admin```

---

## <a name="en_lang"></a> EN

### Description

Applications for adding and viewing .csv files with built-in authorization. (Implementation via Docker is in the works)

## Installation on local computer

1. Copy project from the project on the local computer;
2. Create a virtual environment and activate it;
3. Install any command

     ``` bash
     Requirements for installing pip.txt
     ```

4. Launch a team project

     ``` bash
     python3 Manage.py launch server
     ```

5. Go to ```localhost:8000```, the authorization form will open;
6. Default login is: ```admin```, default password is: ```admin```.

## Functionality

After authorization, a form for adding and viewing a list of files will open. After adding files, you can open them one by one for viewing or delete any of them. While viewing a spreadsheet file, you can select the number of rows per page and sort by one column in forward or reverse order.

You can view and delete a file only after logging in.

## Accounts

Open the admin panel to create or edit an account: ```localhost:8000\admin```
