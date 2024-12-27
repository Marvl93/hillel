tasks = []

while True:
    print("\nМеню:")
    print("1. Добавить задачу")
    print("2. Показать задачи")
    print("3. Обновить задачу")
    print("4. Удалить задачу")
    print("5. Выйти")

    choice = input("Выберите опцию: ")

    if choice == "1":
        title = input("Введите описание задачи: ")
        tasks.append({"title": title, "status": "не выполнено"})
        print(f"Задача '{title}' добавлена.")

    elif choice == "2":
        filtered_tasks = tasks

        if filtered_tasks:
            print("\nСписок задач:")
            for idx, task in enumerate(filtered_tasks, 1):
                print(f"№{idx}. Задача: {task['title']}, Статус: {task['status']}")
        else:
            print("Нет задач для отображения.")

    elif choice == "3":
        if tasks:
            print("\nСписок задач для обновления:")
            for idx, task in enumerate(tasks, 1):
                print(f"№{idx}. Задача: {task['title']}, Статус: {task['status']}")

            try:
                # Запрашиваем номер задачи для изменения
                task_index = int(input("Введите номер задачи для обновления: ")) - 1

                if 0 <= task_index < len(tasks):
                    new_title = input("Введите новое описание задачи (или оставьте пустым): ").strip()
                    new_status = input("Введите новый статус (выполнено/не выполнено) или оставьте пустым: ").strip()

                    if new_title:
                        tasks[task_index]["title"] = new_title
                    if new_status:
                        tasks[task_index]["status"] = new_status
                    print(f"Задача №{task_index + 1} обновлена.")
                else:
                    print(f"Задача с номером {task_index + 1} не найдена.")
            except ValueError:
                print("Номер задачи должен быть числом.")
        else:
            print("Нет задач для обновления.")

    elif choice == "4":
        try:
            task_index = int(input("Введите номер задачи для удаления: ")) - 1
            if 0 <= task_index < len(tasks):
                del tasks[task_index]
                print(f"Задача №{task_index + 1} удалена.")
            else:
                print(f"Задача с номером {task_index + 1} не найдена.")
        except ValueError:
            print("Номер задачи должен быть числом.")

    elif choice == "5":
        print("Выход из программы. До свидания!")
        break

    else:
        print("Некорректный выбор. Попробуйте снова.")
