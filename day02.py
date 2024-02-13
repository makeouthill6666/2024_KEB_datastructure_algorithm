import ast
# def is_stack_full() :
# 	global size, stack, top
# 	if (top >= size-1) :
# 		return True
# 	else :
# 		return False
#
# def is_stack_empty() :
# 	global size, stack, top
# 	if (top == -1) :
# 		return True
# 	else :
# 		return False
#
# def push(data) :
# 	global size, stack, top
# 	if (is_stack_full()) :
# 		print("스택이 꽉 찼습니다.")
# 		return
# 	top += 1
# 	stack[top] = data
#
# def pop() :
# 	global size, stack, top
# 	if (is_stack_empty()) :
# 		print("스택이 비었습니다.")
# 		return None
# 	data = stack[top]
# 	stack[top] = None
# 	top -= 1
# 	return data
#
# def peek() :
# 	global size, stack, top
# 	if (is_stack_empty()) :
# 		print("스택이 비었습니다.")
# 		return None
# 	return stack[top]

# def check_math_expression(expression):
#     try:
#         ast.parse(expression)
#         return True
#     except SyntaxError:
#         return False


def check_bracket(expr : str) -> bool:
	"""
	check bracket in expression
	:param expr: str
	:return: bool
	"""
	stack=list()
	table = {')':'(', '}':'{', ']':'[', '>':'<',}
	for char in expr:
		if char in table.values():
			# push(char)
			stack.append(char)
		elif char in table.keys():
			if not stack or table[char] != stack.pop():
				return False
	return len(stack) == 0



	# for ch in expression:
	# 	if ch in '([{<':
	# 		push(ch)
	# 	elif ch in ')]}>':
	# 		out = pop()
	# 		if ch == ')' and out == '(':
	# 			pass
	# 		elif ch == ']' and out == '[':
	# 			pass
	# 		elif ch == '}' and out == '{':
	# 			pass
	# 		elif ch == '>' and out == '<':
	# 			pass
	# 		else:
	# 			return False
	# 	else :
	# 		pass
	# if is_stack_empty() :
	# 	return True
	# else :
	# 	return False

## 전역 변수 선언 부분 ##
# size = 100
# stack = [ None for _ in range(size) ]
# top = -1

## 메인 코드 부분 ##
if __name__ == "__main__" :
	expression = input("Input expression : ")
	print(check_bracket(expression))
