from data import Doc
from faker import Faker


def insert_fake_data():
    print("Inserting fake data ...")

    fake = Faker()
    for i in range(10000):
        data = {
            "name": fake.name(),
            "country": fake.country(),
            "state": fake.state(),
            "color": fake.safe_color_name()
        }

        d = Doc.create(data=data)
        print("%s %s" % (d.id, d.data))

        
def run_example_query():

    print("All the people who like purple")
    results = Doc.select().where(Doc.data["color"] == "purple")
    for d in results:
        print("%s %s" % (d.id, d.data))


if __name__ == '__main__':
    insert_fake_data()
    run_example_query()
