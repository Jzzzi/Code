import xlrd
import xlwt

readbook = xlrd.open_workbook('./成绩.xls', formatting_info=True)
writebook = xlwt.Workbook()
for num_sheet in range(readbook.nsheets):
    readsheet = readbook.sheet_by_index(num_sheet)
    writesheet = writebook.add_sheet(readsheet.name,cell_overwrite_ok=True)
    for row_index in range(readsheet.nrows):
        for col_index in range(readsheet.ncols):
            cell_value = readsheet.cell_value(row_index, col_index)
            if row_index >= 2 and col_index >=3 and cell_value != '':
                cell_value = int(cell_value)
            writesheet.write(row_index, col_index, cell_value)
    # for row_index in range(2,readsheet.nrows):
    #     total = 0
    #     for i in range(3,11):
    #         sign = 0
    #         if readsheet.cell_value(row_index,i) != '':
    #             total += readsheet.cell_value(row_index,i)
    #             sign = 1
    #     if sign == 1:
    #         writesheet.write(row_index,11,total)

sheet_change = input('第几张表：')
readsheet = readbook.sheet_by_index(int(sheet_change)-1)
writesheet = writebook.get_sheet(int(sheet_change)-1)
row_score = []
for row_index in range(2,readsheet.nrows):
    cell_value = readsheet.cell_value(row_index,11)
    if cell_value == '':
        continue
    row_score.append([row_index,cell_value])
row_score.sort(key=lambda x:x[1],reverse=True)
for i in range(len(row_score)):
    if i == 0:
        rank = 1
    else:
        if int(row_score[i][1]) < int(row_score[i-1][1]):
            rank = i+1
    writesheet.write(row_score[i][0],12,rank)
#保存表格
writebook.save('./成绩.xls')
print('保存成功')
input('回车退出')
