# ДЗ: прежде чем начинать - лучше прочитайте целиком.
# 1. Создать новый проект в гитхабе, склонировать его к себе в IDE (PyCharm)
# 2. Сесть, прежде чем кодить - на листке себе нарисовать и написать, какие вам нужно будет придумать классы - что какой будет делать.
# # 3. Что нужно будет сделать:
# - Написать код, который будет получать данные по погоде сейчас (на момент запуска) в разных городах (Москва, Валенсия, любые города ещё) и дописывать эту информацию в 1 csv файл - с датой и временем измерения. Список городов должен храниться в YAML файле и браться оттуда
# - Написать отдельные классы в отдельных файлах для:
# чтения списка городов из YAML файла (OptionsReader)
# отправки запросов (RequestSender)
# обработки полученного ответа (DataParser)
# записи данных (DataWriter)
# Можете использовать статические методы у классов (прочитать про них самостоятельно)
# 4. Так же весь код, особенно отправка запросов, парсер и запись в файл - должны быть покрыты обработкой ошибок.
# API для получения погоды: http://api.weatherapi.com/