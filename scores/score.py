import xlrd
import xlwt
sheet_change = input('第几张表：')
while True:
    # 打开要修改的文件
    workbook = xlrd.open_workbook('./成绩.xls', formatting_info=True)

    # 创建一个可写的副本
    workbook_copy = xlwt.Workbook()

    # 读取数据并写入副本
    for num_sheet in range(workbook.nsheets):#获取工作表
        sheet = workbook.sheet_by_index(num_sheet)
        sheet_copy = workbook_copy.add_sheet(sheet.name,cell_overwrite_ok=True)#在副本中创建工作表
        for row_index in range(sheet.nrows):
            for col_index in range(sheet.ncols):
                cell_value = sheet.cell_value(row_index, col_index)
                sheet_copy.write(row_index, col_index, cell_value)
    # 开始修改副本
    # 选择工作表
    sheet = workbook.sheet_by_index(int(sheet_change)-1)
    sheet_copy = workbook_copy.get_sheet(int(sheet_change)-1)
    find = 0
    name = input('姓名：')
    if name == '退出':
        break
    for row_index in range(sheet.nrows):
        if sheet.cell_value(row_index,2) == name:
            row = row_index
            find = 1
    if find == 0:
        continue
    score = [0] * 8
    for i in range(8):
        col = i + 3
        temp = ''
        while temp=='':
            temp = input('第'+str(i+1)+'题成绩：')
        score[i]=int(temp)
        sheet_copy.write(row,col,temp)
    print('总分：'+str(sum(score)))
    sheet_copy.write(row,11,sum(score))
    workbook_copy.save('./成绩.xls')
    print('保存成功')
