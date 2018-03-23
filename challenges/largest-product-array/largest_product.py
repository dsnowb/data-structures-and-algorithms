def largest_product(arr):
    # Check param type and values
    if type(arr) is not list:
        raise TypeError('Parameter must of be of type <list>')
    if not (len(arr[0]) > 1 and len(arr) > 1):
        raise ValueError('Function expects 2 x 2 list or greater')

    # Initialize our max product
    max_p = arr[0][0] * arr[1][0]

    # Loop through matrix, left to right then top to bottom
    row = 0
    for i in range(len(arr) - 1):
        col = 0
        va = arr[row][0] * arr[row + 1][0]
        if va > max_p:
            max_p = va
        for j in range(len(arr[0]) - 1):
            # Compute new products
            ha = arr[row][col] * arr[row][col + 1]
            hb = arr[row + 1][col] * arr[row + 1][col + 1]
            vb = arr[row][col + 1] * arr[row + 1][col + 1]
            da = arr[row][col] * arr[row + 1][col + 1]
            db = arr[row][col + 1] * arr[row + 1][col]
            if ha > max_p:
                max_p = ha
            if hb > max_p:
                max_p = hb
            if vb > max_p:
                max_p = vb
            if da > max_p:
                max_p = da
            if db > max_p:
                max_p = db

            print('ha{} hb{} vb{} da{} db{}'.format(ha,hb,vb,da,db))
            print(max_p)

            col += 1
        row += 1

    return max_p
