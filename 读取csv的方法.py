def open_CSV_file(file_name):
    import pandas as pd
    import csv
    try:
        f = open(file_name, 'r', encoding='utf-8')
        data1 = pd.read_csv(f, engine='python')
    except Exception:
        print('method1 died')
    try:
        csv_reader = csv.reader(open(file_name, encoding='utf-8'))
        data2 = pd.DataFrame(csv_reader)
    except Exception:
        print('method2 died')
    try:
        data3 = pd.read_csv(file_name, encoding='gbk', header=None)
    except Exception:
        print('method3 died')
    try:
        csv_reader = csv.reader(open(file_name, encoding='gbk'))
        data4 = pd.DataFrame(csv_reader)
    except Exception:
        print('method4 died')
    try:
        data5 = pd.read_csv(file_name, header=0, encoding='gbk', error_bad_lines=False)
    except Exception:
        print('method5 died')
    try:
        f = open(file_name, 'r', encoding='ISO-8859-1')
        data6 = pd.read_csv(f, engine='python')
    except Exception:
        print('method6 died')
    try:
        f = open(file_name, 'r', encoding='gb18030')
        data7 = pd.read_csv(f, engine='python')
    except Exception:
        print('method7 died')


open_CSV_file('test.csv')

