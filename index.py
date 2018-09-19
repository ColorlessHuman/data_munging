from difference_calculator import MinDifferenceCalculator as mindiff

filepath = input('Enter path of data file: ')
col1 = int(input('Enter column 1 of difference pair: '))
col2 = int(input('Enter column 2 of difference pair: '))
result_col = int(input('Enter the column which is to be displayed: '))

mindiff_object = mindiff(filepath, col1, col2, result_col)
print('Result:', mindiff_object.get_min_difference())
