from flask import abort


def get_paginated_list(results, url, start, limit):
    start = int(start)
    limit = int(limit)
    count = len(results)
    if count == 0:
        obj = {'start': start, 'limit': limit, 'count': count, 'previous': '', 'next': '', 'results': results}
        return obj
    if count < start or limit < 0:
        abort(404)
    obj = {'start': start, 'limit': limit, 'count': count}
    # make previous url
    if start == 1:
        obj['previous'] = ''
    else:
        start_copy = max(1, start - limit)
        limit_copy = start - 1
        if '?search=' not in url and '?start=' not in url:
            obj['previous'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy)
        elif '&start=' in url:
            url = url[:url.index('&start=')]
            obj['previous'] = url + '&start=%d&limit=%d' % (start_copy, limit_copy)
        elif '?start=' in url:
            url = url[:url.index('?start=')]
            obj['previous'] = url + '?start=%d&limit=%d' % (start_copy, limit)
        else:
            obj['previous'] = url + '&start=%d&limit=%d' % (start_copy, limit_copy)
    # make next url
    if start + limit > count:
        obj['next'] = ''
    else:
        start_copy = start + limit
        if '?search=' not in url and '?start=' not in url:
            obj['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)
        elif '&start=' in url:
            url = url[:url.index('&start=')]
            obj['next'] = url + '&start=%d&limit=%d' % (start_copy, limit)
        elif '?start=' in url:
            url = url[:url.index('?start=')]
            obj['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)
        else:
            obj['next'] = url + '&start=%d&limit=%d' % (start_copy, limit)
    # finally extract result according to bounds
    obj['results'] = results[(start - 1):(start - 1 + limit)]
    return obj
