# import json

# # json string data
# employee_string = '{"first_name": "Michael", "last_name": "Rodgers", "department": "Marketing"}'
#
# # check data type with type() method
# print(type(employee_string))
#
# # convert string to  object
# json_object = json.loads(employee_string)
#
# # check new data type
# print(type(json_object))
#
# # output
# # <class 'dict'>
#
# # access first_name in dictionary
# print(json_object["first_name"])
#
# ####################
# employees_string = '''
# {
#     "employees" : [
#        {
#            "first_name": "Michael",
#            "last_name": "Rodgers",
#            "department": "Marketing"
#
#         },
#        {
#            "first_name": "Michelle",
#            "last_name": "Williams",
#            "department": "Engineering"
#         }
#     ]
# }
# '''
#
# data = json.loads(employees_string)
#
# print(type(data))
# # output
# # <class 'dict'>
#
# # access first_name
# for employee in data["employees"]:
#     print(employee["first_name"])
#
# json_str = json.dumps(data)
# print(json_str)
# print(type(json_str))

###############
# import json
# import os
#
# PATH_TO_TODO_LIST = "myTodoList.json"
#
#
# def create_todo_list_json_file(path_to_storage: str) -> None:
#     if not os.path.exists(path_to_storage):
#         with open(path_to_storage, "w", encoding="utf-8") as file:
#             todos_dict: dict = {"todos": []}
#             file.write(json.dumps(todos_dict))
#     else:
#         raise FileExistsError("File already exists!")
#
#
# def get_todo_items(path_to_storage: str) -> dict:
#     with open(path_to_storage, 'r', encoding="utf-8") as file:
#         return json.load(file)
#
#
# def add_todo_item(path_to_storage: str, todo_item: str) -> str:
#     current_todos = get_todo_items(path_to_storage)
#     current_todos["todos"].append(todo_item)
#     with open(path_to_storage, 'w', encoding="utf-8") as file:
#         json.dump(current_todos, file, indent=4)
#         return todo_item
#
#
# def remove_todo_item(path_to_storage: str, todo_item: str) -> str:
#     current_todos = get_todo_items(path_to_storage)
#     current_todos["todos"].remove(todo_item)
#     with open(path_to_storage, 'w', encoding="utf-8") as file:
#         json.dump(current_todos, file, indent=4)
#         return todo_item
#
#
# if __name__ == "__main__":
#     if os.path.exists(PATH_TO_TODO_LIST):
#         # print(get_todo_items(PATH_TO_TODO_LIST))
#         # add_todo_item(PATH_TO_TODO_LIST, "second item")
#         remove_todo_item(PATH_TO_TODO_LIST, "first item")
#         print(get_todo_items(PATH_TO_TODO_LIST))
#     else:
#         create_todo_list_json_file(PATH_TO_TODO_LIST)

# дописать меню
# добавить функцию изменения по порядковому номеру (от 1 до ...)
# протестировать все функции

#######################

import os

import requests
from bs4 import BeautifulSoup
import urllib.request

# URL = 'https://ru.wallpaper.mob.org/gallery/tag=priroda/'
# response = requests.get(URL)
# print(response)
# print(response.url)
# print(response.status_code)
# print(response.content)
# print(response.headers['content-type'])
# print(response.encoding)
#
# bs = BeautifulSoup(response.text, 'lxml') # 'html.parser'
# print(bs)

####
# text parsing
# temp = bs.find('div', 'tag-mini-widget__title-wrap')
# print(temp)
# print(temp.text.strip())

# titles = bs.find_all('div', 'tag-mini-widget__title-wrap')
#
# for title in titles:
#     print(title.text.strip())

##################
# image parsing

# bs = BeautifulSoup(response.text, 'lxml') # 'html.parser'
# images = bs.findAll('img', 'image-gallery-image__image')
#
# # print(images)
#
# image_links = []
# for image in images:
#     image_links.append(image.get("src"))
#
# # print(image_links)
#
# current_file = 1
#
# for link in image_links:
#     print(f"Downloading {current_file} from {len(image_links)}...")
#     folder_name = "nature_images/"
#     if not os.path.exists(folder_name):
#         os.mkdir(folder_name)
#     file_name = link[link.rfind('/') + 1:]
#     response = requests.get(link, allow_redirects=True)
#     open(folder_name + file_name, 'wb').write(response.content)
#     current_file += 1

####
# SITE_URL = 'https://mixkit.co/'
#
#
# def get_video_links():
#     request = urllib.request.Request(SITE_URL, headers={'User-Agent': 'Mozilla/5.0'})
#     webpage = urllib.request.urlopen(request, timeout=10).read()
#     soup = BeautifulSoup(webpage, "html.parser")
#     rows = soup.find_all(class_="item-grid-video-player__overlay-link")
#
#     links_to_video_pages = []
#
#     for row in rows:
#         links_to_video_pages.append(SITE_URL[:-1] + row.get("href"))
#
#     print("Started processing...")
#     counter = 0
#     result_video_links = []
#
#     for link in links_to_video_pages:
#         counter += 1
#         print(f"Processing {counter} from {len(links_to_video_pages)}...")
#         request = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
#         webpage = urllib.request.urlopen(request, timeout=10).read()
#         soup = BeautifulSoup(webpage, "html.parser")
#         rows = soup.find_all(class_="video-player__viewer")
#
#         for row in rows:
#             result_video_links.append(row.get("src"))
#
#     return result_video_links
#
#
# def download_videos(links, path_to_save):
#     if not os.path.exists(path_to_save):
#         os.makedirs(path_to_save)
#
#     counter = 0
#     for link in links:
#         counter += 1
#         print(f"Downloading file {counter} from {len(video_links)}...")
#         file_name = str(counter) + "_" + link.split("/")[-1]
#         response = requests.get(link, stream=True)
#         with open(path_to_save + file_name, "wb") as video_file:
#             for chunk in response.iter_content(chunk_size=1024 * 1024):
#                 if chunk:
#                     video_file.write(chunk)
#         print(f"Downloading file {counter} finished!")
#
#     print("All done!")
#
#
# if __name__ == "__main__":
#     video_links = get_video_links()
#     download_videos(video_links, "videos/")
