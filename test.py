def validBookObject(bookObject):
    if("name" in bookObject and "price" in bookObject and "isbn" in bookObject):
        return True
    else:
        return False
valid_object =  {
        'name': 'Green Eggs and Ham',
        'price': 7.99,
        'isbn': 9090990888
}
missing_name =  {
        'price': 7.99,
        'isbn': 9090990888
}
missing_price =  {
        'name': '99 Red Baloons',
        'isbn': 9090990888
}
missing_isbn =  {
        'name': 'Green Eggs and Ham',
        'price': 7.99
}