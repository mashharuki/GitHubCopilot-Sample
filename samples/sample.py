# Pythonの基本 - 変数、データ型、リスト、ループ、関数

# 変数とデータ型
# 整数型
num = 10
print(num)  # 10

# 文字列型
str = "Hello, Python!"
print(str)  # Hello, Python!

# リスト
# リストは複数の要素を持つことができます
list = ["apple", "banana", "cherry"]
print(list)  # ['apple', 'banana', 'cherry']

# ループ
# forループを使用してリストの要素を一つずつ表示します
for item in list:
    print(item)

# 関数
# 関数は特定のタスクを実行するコードのブロックです
def greet(name):
    print("Hello, " + name)

greet("Python Learner")  # Hello, Python Learner


# ToDoリストアプリ
# ToDoリストはタスクのリストを管理するためのシンプルなアプリです

# ToDoリストを格納するための空のリストを作成します
todo_list = []

# タスクを追加する関数
def add_task(task):
    todo_list.append(task)

# タスクを削除する関数
def delete_task(task):
    if task in todo_list:
        todo_list.remove(task)

# ToDoリストを表示する関数
def display_tasks():
    for task in todo_list:
        print(task)

# タスクを追加します
add_task("Pythonを学ぶ")
add_task("コードを書く")

# ToDoリストを表示します
display_tasks()

# タスクを削除します
delete_task("コードを書く")

# ToDoリストを再度表示します
display_tasks()