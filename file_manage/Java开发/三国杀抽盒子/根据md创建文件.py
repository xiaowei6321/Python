import os
def main():
	cwd = os.getcwd()
	filename = '30设计接口.md'
	process_md_file(cwd, filename)




def process_md_file(dir, filename):
	with open(dir + '/' + filename, 'r', encoding='utf-8') as f:
		lines = f.readlines()
	current_file_name = None
	current_file_content = []
	in_code_block = False
	for i in range(len(lines)):
		line = lines[i]

		# 如果是代码块起始
		if line.startswith('```') and not in_code_block:
			in_code_block = True
			continue

		# 将代码块内容写入文件
		if line.startswith('```') and in_code_block:

			in_code_block = False

			path = dir + '/' + current_file_name.strip()
			# 如果文件不存在
			path_dir = os.path.dirname(path)
			if current_file_name.strip() != '':

				if not os.path.exists(path_dir):
					# 从路径中获取文件夹路径，不包含文件名 python代码:

					os.makedirs(path_dir)

				with open(path, 'w', encoding='u8') as f:

					f.writelines(current_file_content)
			current_file_content = []
			continue

		# 如果不在代码块
		if not in_code_block:
			current_file_name = line
		# 如果是代码块起始
		if in_code_block:
			current_file_content.append(line)


def process_md_content(filecontent):
	# with open(dir+'/'+filename, 'r', encoding='utf-8') as f:
	#     lines = f.readlines()
	lines = filecontent.split('\n')

	current_file_name = None
	current_file_content = []
	in_code_block = False
	for i in range(len(lines)):
		line = lines[i]

		# 如果是代码块起始
		if line.startswith('```') and not in_code_block:
			in_code_block = True
			continue

		# 将代码块内容写入文件
		if line.startswith('```') and in_code_block:

			in_code_block = False

			path = dir + '/' + current_file_name.strip()
			# 如果文件不存在
			path_dir = os.path.dirname(path)
			if current_file_name.strip() != '':

				if not os.path.exists(path_dir):
					# 从路径中获取文件夹路径，不包含文件名 python代码:

					os.makedirs(path_dir)

				with open(path, 'w', encoding='u8') as f:

					f.writelines(current_file_content)
			current_file_content = []
			continue

		# 如果不在代码块
		if not in_code_block:
			current_file_name = line
		# 如果是代码块起始
		if in_code_block:
			current_file_content.append(line)


if __name__ == '__main__':
	main()
