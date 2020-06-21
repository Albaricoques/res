# res

HTML_CSS/page/test.html 
практика различных подходов к оформлению веб-страницы и вставки html-блоков различной направленности.

PARSER/PARSER_edx_course_downloader.py 
Скачивает курс edX, на который записан данный аккаунт, для доступа оффлайн в течение любого времени. 
Создает папку с именем курса, скачивает туда по папкам каждую страницу курса с её видео и субтитрами

bash 
Скрипты bash: калькулятор, наибольший общий делитель, интерфейс.

nginx_gunicorn_wsgi/init.sh
nginx в ответ на запрос GET к
1) 127.0.0.1/uploads/%?% - выгружает %?% из папки uploads, 
2) 127.0.0.1/%?/file.extension% - выгружает %?/file.extension% из папки public, 
3) 127.0.0.1/hello/%?% - проксирует на 0.0.0.0:8080/ 
gunicorn в ответ на запрос GET к 0.0.0.0:8080 вызывает wsgi-обработчик, который выводит все параметры запроса GET построчно.

opencv_PyQt5/
Различные применения opencv и pyqt5 в Python:
‌OBJ_CUT/AUTO/OBJ_CUT.py - автоматическое вырезание однотонных объектов с белого фона картинки в отдельные файлы с сохранением их координат (для последующей реализации Drag-and-Drop интерфейса интерактивного вопроса в опроснике),
‌OBJ_CUT/MANUAL/l_button_click.py - вырезание объектов с картинки вручную щелчками курсора, #идея: набор щелчками курсора-пипетки палитры цветов, задействованных в отрисовке объекта вырезания, и автоматическое вырезание предыдущим скриптом#
‌DnD_STEP_QUIZ/QUIZ.py - интерфейс одного из интерактивных вопросов опросника на тему молекулярной биологии, в котором необходимо разместить нужные на данной стадии сплайсинга белки на правильных местах пре-мРНК,
‌QUIZ/QUIZ.py - интерфейс опросника на темы молекулярной биологии,
‌MANY_PICS_CUT_RENAME.py - одновременная обрезка и переименование большого числа картинок;

tcp/
tcp_server_127_0_0_1_1234.py и tcp_client_NEWTAB.py - обмен произвольными сообщениями с сервером;
‌tcp_server_127_0_0_1_1234_WITH_EXACT_FUNCTIONS.py и tcp_client_NEWTAB_WITH_EXACT_FUNCTIONS.py - обмен сообщениями фиксированной длины с сервером с учётом возможной потери соединения в процессе (недоотправленные данные отправляются в следующем пакете);
‌tcp_server_html_127_0_0_1_1234.py и tcp_client_html_NEWTAB.py - скачивание файлов с сервера;
