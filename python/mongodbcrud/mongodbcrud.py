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

def search():
    name = input("id: ")
    p = db.data.find_one({"_id": ObjectId(name)})

    print(p["name"])


def main():
    print("Operation:\n1. Insert\n2. Read\n3. Update\n4. Delete")
    op = int(input("Enter Operation Number: "))

    if op == 1:
        insert()
    elif op == 2:
        read()
    elif op == 3:
        update()
    elif op == 4:
        delete()
    elif op == 5:
        search()
    else:
        print("No Operation Selected!!!")


if __name__ == '__main__':
    main()