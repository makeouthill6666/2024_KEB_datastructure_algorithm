def print_poly(f_x) -> str : #다항식 출력
	term = len(f_x) - 1
	poly_str = "f(x) = "
	
	for i in range(len(fx)) :
		coefficient= f_x[i] #계수

		if (coefficient >= 0) :
			poly_str = poly_str + "+"
		poly_str = poly_str + f'{coefficient}x^{term} '
		term -= 1

	return poly_str


def calc_poly(x_value, f_x) :
	retValue = 0
	term = len(f_x) - 1	# 최고차항 숫자 = 배열길이-1
	
	for i in range(len(fx)) :
		coefficient = f_x[i]	# 계수
		retValue += coefficient * x_value ** term
		term = term - 1

	return retValue


## 전역 변수 선언 부분 ## 
fx = [2, 3, 4, 0, -9]			# = 2x^4 +3x^3 +4x^2 +0x^1 -9x^0


## 메인 코드 부분 ## 
if __name__ == "__main__" :


	print(print_poly(fx))

	print(calc_poly(int(input("X 값 : ")), fx))

	
