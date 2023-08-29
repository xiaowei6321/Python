import markdown
from tabulate import tabulate

# 读取Markdown文件内容
with open('01准备数据.md', 'r', encoding='utf-8') as file:
    markdown_text = file.read()

# 解析Markdown内容
html = markdown.markdown(markdown_text)

# 提取表格数据
tables = []
table_start = False
for line in html.split('\n'):
    if line.startswith('<table>'):
        table_start = True
        table_rows = []
    elif line.startswith('</table>'):
        table_start = False
        tables.append(table_rows)
    elif table_start and line.startswith('<tr>'):
        table_rows.append([cell.strip() for cell in line.split('<td>')[1:]])

# 打印表格
for table in tables:
    print(tabulate(table, headers='firstrow', tablefmt='grid'))
