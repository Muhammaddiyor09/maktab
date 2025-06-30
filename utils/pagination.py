import math


def pagination(model, page, limit, db):
    offset = (page - 1) * limit
    page_count = db.query(model).count()
    result = db.query(model).limit(limit).offset(offset).all()
    return {
        "page": page,
        "limit": limit,
        "page_count": math.ceil(page_count/limit),
        "data": result
    }
