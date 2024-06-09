def total_sale_for_each_category():
    query = """
        SELECT 
        strftime('%d-%m-%Y', datetime(Orders.purchase_date, 'unixepoch')) as date,
        date('now', '-1 month') as Date,
        Categoreis.title,
        SUM(Products.price * OrderItems.quantity) AS total_value
        FROM OrderItems
        INNER JOIN Products ON OrderItems.product_id = Products.id
        INNER JOIN Categoreis ON Categoreis.id = Products.category_id
        INNER JOIN Orders ON OrderItems.order_id = Orders.id
        GROUP BY Orders.purchase_date, Categoreis.title
        LIMIT 100
    """
