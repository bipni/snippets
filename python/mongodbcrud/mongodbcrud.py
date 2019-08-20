from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.test


def insert():
    pid = int(input('Enter ID: '))
    name = input('Enter name: ')
    age = int(input('Enter age: '))

    db.data.insert_one(
        {
            "id": pid,
            "name": name,
            "age": age
        }
    )

    print("Data Inserted")

def read():
    data = db.data.find()
    print("All Data: ")

    for d in data:
        print(d)


def update():
    pid = int(input("Enter ID: "))
    name = input('Enter name: ')
    age = int(input('Enter age: '))

    db.data.update_one(
        {"id": pid},
        {
            "$set": {
                "name": name,
                "age": age
            }
        }
    )
    print("Data Updated")


def delete():
    pid = int(input('\nEnter id: '))
    db.data.delete_many({"id":pid})
    print('Data Deleted')


def main():
    # insert()
    # read()
    # update()
    # delete()


if __name__ == '__main__':
    main()