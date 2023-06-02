def paginate(query, page=1, per_page=10):
    offset = (page - 1) * per_page
    limit = per_page
    return query.offset(offset).limit(limit)
