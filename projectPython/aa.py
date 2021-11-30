import pymongo


class DatabaseClass:
    def __init__(self, toSerachName):
        self.connection = pymongo.MongoClient("localhost", 27017)
        self.database = self.connection["bank"]
        self.collection = self.database["bank"]
        self.toSerachName = toSerachName

    def databaseMethod(self):
        toReturn = ''
        try:
            myQuery = {'name': self.toSerachName}
            data = self.collection.find(myQuery).count_documents()
            # dat = data.count()

            #     for z in data:
            #         print(type(z))
            #         if z['name'] == self.toSerachName:
            #             print(z)
            #             findingData = self.collection.find(myQuery)
            #             for i in findingData:
            #                 toReturn = i['address']
            # else:
            #     toReturn = self.toSerachName + " is not found :3"

            return toReturn

        except Exception as err:
            print(err)


if __name__ == "__main__":
    db = DatabaseClass('John')
    #db = DatabaseClass('ohn')
    data = db.databaseMethod()
    print(data)
