#СОЗДАЕТ ПАПКУ С ИМЕНЕМ КУРСА, СКАЧИВАЕТ ТУДА ПО ПАПКАМ КАЖДУЮ СТРАНИЦУ КУРСА С ЕЕ ВИДЕО И СУБТИТРАМИ


# в каждой скачанной едэикс.хтмл несколько доунлоад видео файл - все видео данного блока

#if video/srt/txt/html status_code != '200', add the name to an object-line with all these unsuccessful names, and print it in the end

email = 'email@mail.com'
password = 'password'

course_name = 'MITx+7.28.3x+1T2020' #from the address of the opened page of course which I m enrolled in. after 'course-v1:'

import requests
import re
import os

s = requests.Session()

login_page = 'https://courses.edx.org/login'
login_page_api = 'https://courses.edx.org/user_api/v1/account/login_session/'
course_page_template = 'https://courses.edx.org/courses/course-v1:{}/course/'
course_page = course_page_template.format(course_name)


user_agent_val = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0'

headers = {'User-Agent': user_agent_val}


r = s.get(login_page, headers = headers)

s.headers.update({'Referer':login_page})


csrftoken = s.cookies['csrftoken']

params = {
    'backUrl': 'https://courses.edx.org/',
    'email': email,
    'password': password,
    'csrfmiddlewaretoken': csrftoken,
    'remember':'yes'
}

post_request = s.post(login_page_api, data=params, headers=headers)

print(post_request.url)
print('login status code', post_request.status_code)

r2 = s.get(course_page, headers = headers)

print('\n', r2.url)
print('loading course page: status code = ', r2.status_code)

'''
	вот что на этом сайте:
	href="https://courses.edx.org/courses/course-v1:MITx+7.28.1x+1T2020a/jump_to/block-v1:MITx+7.28.1x+1T2020a+type@sequential+block@2fce5b2544e94f83be48dbec66070be8"
                                class="subsection-text outline-button"
                                id="block-v1:MITx+7.28.1x+1T2020a+type@sequential+block@2fce5b2544e94f83be48dbec66070be8"
                            >
                                      <span class="icon fa fa-pencil-square-o" aria-hidden="true"></span>
                                      <h4 class="subsection-title">
                                          Learning Sequence: DNA Polymerase
                                          (16 Questions)'''

links = {}

#course_name = 'MITx+7.28.3x+1T2020'
#course_name.replace('+','.')

pattern = r'(id=\"block-v1:.+?type@sequential.block@(.*?)\"(\n.*?)+subsection-title.*?\n *(.*?)\n)'

text = r2.text.split('<h3 class=\"section-title\">')

#print('how many blocks?', len(text))
#print('line in each block', list(map(lambda p:p.count('\n'), text)))
	
for i in range(1, len(text)):
	endtitle = text[i].find('<')
	blockname = str(i) + '. ' + text[i][0:endtitle]
	blocklinks = re.findall(pattern,text[i])

	#print(name)
	#print(len(blocklinks), len(blocklinks[0]))
	#print('one of the names: ',blocklinks[0][3])

	for j in blocklinks:
		localname = blockname + '.. ' + j[3]
		#print(localname)
		links[localname] = [j[1], blockname, j[3]]







block_page_template = 'https://courses.edx.org/courses/course-v1:{course_name}/jump_to/block-v1:{course_name}+type@sequential+block@{blocklink}'

videoname_pattern = r'hd-2&#34;&gt;(.+?)&lt;(.*?\n)*?.*?video_(.+?)&#34;(.*?\n)*?.*?(https://edx-video.net/.+?mp4)'

srt_txt_post_template = 'https://courses.edx.org/courses/course-v1:{course_name}/xblock/block-v1:{course_name}+type@video+block@{code}/handler/xmodule_handler/save_user_state'
srt_txt_get_template = 'https://courses.edx.org/courses/course-v1:{course_name}/xblock/block-v1:{course_name}+type@video+block@{code}/handler/transcript/download'


try:
	os.mkdir(course_name)
except FileExistsError:
	pass

#homepath = os.getcwd() #'/home/aleksandr/edx/molbiol'


for i in links:

	try:
		os.mkdir(course_name + '/' + links[i][1])
		number = 0
	except FileExistsError:
		pass
	
	number += 1

	address = course_name + '/' + links[i][1] + '/' + str(number) + '. ' + links[i][2] + '/'

	os.mkdir(address)

	filename = address + i + '.html'

	block_page = block_page_template.format(course_name = course_name, blocklink = links[i][0])
	print(i, '\n', block_page)

	res = s.get(block_page, headers = headers)
	print('GET status_code', res.status_code, end = '\n\n')

	with open(filename, 'w', encoding="utf-8") as f:
		f.write(res.text)
		print(filename, 'is created', end = '\n\n\n')



	a = res.text

	videos_and_links = re.findall(videoname_pattern, a)

	#print(videos_and_links[0][0], videos_and_links[0][2], videos_and_links[0][4])

	number2 = 0

	for i in videos_and_links:

		number2 += 1
		name = str(number2) + '. ' + i[0]
		srt_txt_code = i[2]
		videolink = i[4]

		print(name)
		
		video = s.get(videolink, headers=headers)
		print('video download status', video.status_code)
		print('Content?', video.headers['Content-Type'], end = '\n')
		with open(address+name+'.mp4', 'wb') as f:
			f.write(video.content)
		


		srt_txt_post = srt_txt_post_template.format(course_name = course_name, code = srt_txt_code)
		srt_txt_get = srt_txt_get_template.format(course_name = course_name, code = srt_txt_code)

		#params_srt = {
		#	'csrfmiddlewaretoken': csrftoken,
		#	'data-value':'srt', 
		#	'transcript_download_format':'srt'
		#}
		csrftoken = s.cookies['csrftoken']
		post = s.post(srt_txt_post, data={'csrfmiddlewaretoken': csrftoken, 'data-value':'srt', 'transcript_download_format':'srt'}, headers=headers)
		print('srt POST status', post.status_code)
		srt = s.get(srt_txt_get, headers=headers)
		print('srt GET status', srt.status_code, end = '\n')
		with open(address+name+'.srt','w') as f:
			f.write(srt.text)

		csrftoken = s.cookies['csrftoken']
		post = s.post(srt_txt_post, data={'csrfmiddlewaretoken': csrftoken,'data-value':'txt', 'transcript_download_format':'txt'}, headers=headers)
		print('txt POST status', post.status_code)
		txt = s.get(srt_txt_get, headers=headers)
		print('txt GET status', txt.status_code, end = '\n')
		with open(address+name+'.txt','w') as f:
			f.write(txt.text)

		#ВЫДЕЛИТЬ КУДА НИБУДЬ ПРАВИЛЬНЫЕ ОТВЕТЫ В ТЕСТАХ ПОКА ПОМНЮ КАК УСТРОЕН КОД (правильные ответы есть в тестах, поищи 2b179c672af042e187da6f93129d903f , правильные ответы 2 3 4 5)

		print('\n\n')

	print('\n\n NEXT BLOCKLINK \n\n')









#with open("links.txt","w",encoding="utf-8") as f:
#    f.write(links)




'''
#txtlinks = '\n\n\n'.join([i for i in links])

with open("edx3.html","w",encoding="utf-8") as f:
    f.write(r3.text)
'''

'''
import requests

url = 'https://courses.edx.org/login'

# Важно. По умолчанию requests отправляет вот такой
# заголовок 'User-Agent': 'python-requests/2.22.0 ,  а это приводит к тому , что Nginx
# отправляет 404 ответ. Поэтому нам нужно сообщить серверу, что запрос идет от браузера

user_agent_val = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0'

# Создаем сессию и указываем ему наш user-agent
session = requests.Session()
r = session.get(url, auth=(email, password), headers = {
    'User-Agent': user_agent_val,
})

# Указываем referer. Иногда , если не указать , то приводит к ошибкам.
session.headers.update({'Referer':url})

#Хотя , мы ранее указывали наш user-agent и запрос удачно прошел и вернул
# нам нужный ответ, но user-agent изменился на тот , который был
# по умолчанию. И поэтому мы обновляем его.
session.headers.update({'User-Agent':user_agent_val})

#print(session.cookies.items()) #ЗДЕСЬ МОЖНО ПОЛУЧИЬ НАЗВАНИЯ ПАРАМЕТРОВ!!

#Теперь разберемся для чего нужен _xsrf .
# Когда мы логинимся на сайте hh.ru , то мы просто вводим логин и пароль и все. Но при этом при POST запросе на сервер
# кроме введенных нами значений передается и параметр _xsrf, который нужен для защиты от CSRF-атак.
# Так вот значение этого параметра сервер hh.ru генерирует автоматически и хранит его в кукис файлах в браузере
# и чтобы получить это значение , нам нужно использовать объект Session библиотеки requests
#Объект Session позволяет сохранять определенные параметры в запросах.Он также сохраняет файлы cookie во всех запросах

## В куках у нас будет два значения _xsrf. Один для hh.ru , а другой moscow.hh.ru.Хотя , значение одно и тоже
## Если написать просто session.cookies.get('_xsrf') то возникнет исключение, и поэтому
## вот таким способом , что внизу получим значение _xsrf

#items = session.cookies.items()
for item in session.cookies.items():
    #items[item[0]] = item[1]
    if item[0] == 'csrftoken':
        csrftoken = item[1]
        print('csrf taken')
        break

# Осуществляем вход с помощью метода POST с указанием необходимых данных
post_request = session.post(url, params={
    'backUrl': 'https://courses.edx.org/',
    'login': email,
    'password': password,
    'csrfmiddlewaretoken': csrftoken, #универсальное имя параметра для передачи сsrftoken
    'remember':'yes',
})

#name taken from code of site, inspect element firefox
# items[0][0]: items[0][1],
# items[1][0]: items[1][1],
# items[2][0]: items[2][1],
# items[3][0]: items[3][1],
# items[4][0]: items[4][1],


#Вход успешно воспроизведен и мы сохраняем страницу в html файл
with open("edx.html","w",encoding="utf-8") as f:
    f.write(post_request.text)
'''
