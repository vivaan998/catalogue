# In this file there should be NO reference/import to flask or SQLAlchemy.
# TODO-1: Finish the implementation of existing methods and add the new methods if needed
# TODO-1: Perform unit test on the methods exposed here

from .core import retrieve_data 


# def create():
#     create.execute()
#     pass


def get(languageISO):
    categories = retrieve_data.read_category(languageISO)

    print('HERE IN GET BACK')
    print(categories)
    results = list()

    for category in categories:
        temp = dict()
        temp['UUID'] = category.UUID
        temp['value'] = category.ValueName

        results.append(temp)

    return results


# def edit():
#     pass
