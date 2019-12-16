import openpyxl as xl

book = xl.load_workbook('/media/siceyo/562A6D9B2A6D793F/Users/SiCeYo/Documents/cons.xlsx')
col = book['cons']['b']
for i in range(1, 116):
    try:
        # print(col[i].value)
        if col[i].value>10000000000.00:
            col='+249'+str(col[i].value)

    except Exception as e:
        print(e)
        print('ignoring' + str(i))
book.save('test.xlsx')