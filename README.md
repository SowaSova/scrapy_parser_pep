# Парсинг документов PEP

Парсер поможет собрать статусы документов PEP, а также получить информацию, сколько из них в каждом статусе.

## Используемые технологии

 - Python 3.7
 - Scrapy (фреймворк для парсинга)
 
## Установка

1. Клонируйте репозиторий
```bash
git clone https://github.com/SowaSova/scrapy_parser_pep.git
```

2. Создайте и активируйте виртуальное окружение
```bash
python3.7 -m venv venv
```

* Если у вас Linux/macOS

    ```bash
    source venv/bin/activate
    ```

* Если у вас windows

    ```bash
    source venv/scripts/activate
    ```

3. Обновите pip до последней версии
```bash
python3 -m pip install --upgrade pip
```

4. Установите зависимости из файла requirements.txt
```bash
pip install -r requirements.txt
```


## Запуск

Для запуска сбора информации о документах PEP, отправьте "паука" pep:
```bash
scrapy crawl pep
```

После завершения сбора информации в папке results появится два файла:
* pep_yyyy-mm-ddThh-mm-ss.csv - все документы PEP с их статусами
* status_summary_yyyy-mm-dd_hh-mm-ss.csv - количество документов PEP 
в каждом статусе
