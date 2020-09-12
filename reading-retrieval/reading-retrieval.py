#!/home/schenlyx/anaconda3/bin/python3

"""
我是读书记录检索小程序，可以用来记录检索所读数目哟。
"""

def read_file():
	"我是文件读取函数，可以提取文件信息"
	try:	
		with open("read_record.data", "r", encoding = 'UTF-8') as f:
			file_lists = f.readlines()
			return file_lists
	except FileNotFoundError:
		with open("read_record.data", "w", encoding = 'UTF-8') as f:
			return []
		
def get_data(file_lists):
	"我是数据读取函数，可以将文件信息中的数据提取出来"
	data_lists = []
	for i in file_lists:
		data_lists.append(i.split('|'))
		data_lists[-1][0] = int(data_lists[-1][0])
		data_lists[-1][-1] = data_lists[-1][-1].strip()
	#print(data_lists)
	return data_lists

def list_print(target_list):
	"我是结果打印函数，可以将查询的结果打印出来"
	print("书籍序号：%s" %(target_list[0]))
	print("书籍名称：《%s》" % (target_list[1]))
	print("书籍类别：%s" %(target_list[2]))
	print("核心概括：%s" %(target_list[3]))
	print("阅读进度：%s" %(target_list[4]))
	print("复阅评估：%s" %(target_list[5]), end="\n\n")
	

def retrieval(data_lists):
	try:
		"我是条件检索函数，可以具有序号检索、名称检索、类别检索、复阅检索、全部检索功能"
		print("检索条件提供：1.序号检索 2.名称检索 3.类别检索 4.复阅检索 5.全部检索")
		condition = int(input("请输入检索条件对应序号:"))

		if condition == 1:
			print("————————————————————————————————")
			serial_number = int(input("请输入需要检索的序号:"))
			print("————————————————————————————————")
			
			if_find = False

			for i in data_lists:
				if serial_number == i[0]:
					print("检索结果如下：")
					list_print(i)
					if_find = True
					break
			
			if if_find == False:
				print("未找到对应序号为%s的记录" %(serial_number))

			print("————————————————————————————————")

		elif condition == 2:
			print("————————————————————————————————")
			name_book = input("请输入需要检索的书籍名称:")
			print("————————————————————————————————")

			if_find = False

			for i in data_lists:
				if name_book == i[1]:
					print("检索结果如下：")
					list_print(i)
					if_find = True
					break
			
			if if_find == False:
				print("未找到书籍名称为《%s》的记录" %(name_book))

			print("————————————————————————————————")

		elif condition == 3:
			print("————————————————————————————————")
			print("现可供检索的类别：")
			temp_list = []
			for i in data_lists:
				if i not in temp_list:
					temp_list.append(i)
					print(i[2], end=",")
			print("\n————————————————————————————————")
			category_book = input("请输入需要检索的书籍类别：")
			print("————————————————————————————————")

			if_find = False

			for i in data_lists:
				if category_book == i[2]:
					if if_find == False:
						print("检索结果如下：")
						if_find = True
					list_print(i)

			if if_find == False:
				print("未找到书籍类别为%s的记录" %(category_book))

			print("————————————————————————————————")

		elif condition == 4:
			print("————————————————————————————————")
			print("提示：可供检索的复阅类型\n是（推荐复阅），否（不推荐复阅），自选（可供选择复阅）")
			evaluation_book = input("\n请输入需要检索的复阅类型：")
			print("————————————————————————————————")
			
			if_find = False

			if evaluation_book in ["是", "否", "自选"]:
				for i in data_lists:
					if evaluation_book == i[5]:
						if if_find == False:
							print("检测结果如下：")
							if_find = True
						list_print(i)
			else:
				print("输入格式有误")

			if if_find == False:
				print("未找到复阅类型为%s的记录" %(evaluation_book))

			print("————————————————————————————————")	

		elif condition == 5:
			print("————————————————————————————————")
			if len(data_lists) == 0:
				print("当前没有读书记录")
			else:
				for i in data_lists:
					list_print(i)
			print("————————————————————————————————")



	except ValueError:
		print("输入格式有误")

if __name__ == "__main__":
	file_lists = read_file()
	#print(file_lists)
	data_lists = get_data(file_lists)
	#list_print(data_lists[1])
	retrieval(data_lists)