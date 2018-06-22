
```
import xlwt #写入数据
import xlutils #操作excel
#----xlrd库
#打开excel文件
workbook = xlrd.open_workbook('myexcel.xls')
#获取表单
worksheet = workbook.sheet_by_index(0)
#读取数据
data = worksheet.cell_value(0,0)
#----xlwt库
#新建excel
wb = xlwt.Workbook()
#添加工作薄
sh = wb.add_sheet('Sheet1')
#写入数据
sh.write(0,0,'data')
#保存文件
wb.save('myexcel.xls')
#----xlutils库
#打开excel文件
book = xlrd.open_workbook('myexcel.xls')
#复制一份
new_book = xlutils.copy(book)
#拿到工作薄
worksheet = new_book.getsheet(0)
#写入数据
worksheet.write(0,0,'new data')
#保存
new_book.save()
```
