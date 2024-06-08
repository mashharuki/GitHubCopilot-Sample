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

# ユーザーからの入力を処理する関数
def handle_input():
    while True:
        print("\n1. タスクを追加")
        print("2. タスクを削除")
        print("3. ToDoリストを表示")
        print("4. 終了")
        user_input = input("選択してください(1-4): ")

        if user_input == "1":
            task = input("追加するタスクを入力してください: ")
            add_task(task)
        elif user_input == "2":
            task = input("削除するタスクを入力してください: ")
            delete_task(task)
        elif user_input == "3":
            display_tasks()
        elif user_input == "4":
            break
        else:
            print("無効な入力です。もう一度お試しください。")

# メイン関数
def main():
    handle_input()

# スクリプトとして実行された場合にmain関数を呼び出します
if __name__ == "__main__":
    main()