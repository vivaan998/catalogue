# In this file there should be NO reference/import to flask or SQLAlchemy.
# TODO-1: Finish the implementation of existing methods and add the new methods if needed
# TODO-1: Perform unit test on the methods exposed here

from .core import retrieve_data


def get(languageISO):
    categories = retrieve_data.read_categories(languageISO)
    results = list()

    for category in categories:
        results.append({
            'uuid': category.UUID,
            'value': category.Value
        })
    return results
