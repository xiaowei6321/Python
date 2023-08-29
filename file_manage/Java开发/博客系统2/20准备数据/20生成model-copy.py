from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql+pymysql://root:123456@localhost/test')

metadata = MetaData()
metadata.reflect(bind=engine)



for table_name, table in metadata.tables.items():
	# ```
	# table_name=comments
	# table:comments
	#
	# allow_lambda = True 是否允许lambda表达式，无服务器计算服务，在需要时执行代码逻辑
	# autoincrement_column = None 自动增量列
	# columns:{
	# 	0:comments.userid,
	# 	1:comments.postsid,
	# 	2:comments.commentid,
	# 	3:comments.content
	# }
	# ```
	class_name = table_name.title()
	print(f'public class {class_name} {{')

	for column in table.c:
		column_name = column.name
		column_type = str(column.type)

		java_type = 'String'
		if 'int' in column_type or 'INT' in column_type:
			java_type = 'int'
		elif 'datetime' in column_type:
			java_type = 'Date'
		# 这里可以根据需要添加更多的类型映射

		print(f'    private {java_type} {column_name};')

	for column in table.c:
		column_name = column.name
		column_type = str(column.type)

		java_type = 'String'
		if 'int' in column_type:
			java_type = 'int'
		elif 'datetime' in column_type:
			java_type = 'Date'
		# 这里可以根据需要添加更多的类型映射

		capitalized_column_name = column_name[0].upper() + column_name[1:]
		print(f'    public {java_type} get{capitalized_column_name}() {{')
		print(f'        return {column_name};')
		print('    }')

		print(f'    public void set{capitalized_column_name}({java_type} {column_name}) {{')
		print(f'        this.{column_name} = {column_name};')
		print('    }')

	print('}')
