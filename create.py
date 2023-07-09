from db_config import Message


# インスタンスを作成してから保存
def create_message():
    message = Message(user="Bob", content="Hello Tom!")
    message.save()

    # インスタンを生成しないで保存するcreate()メソッド
    Message.create(user="Tom", content="Hello Bob!")


if __name__ == "__main__":
    create_message()
