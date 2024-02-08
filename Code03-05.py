def print_poly(t_x, f_x) -> str:  # 다항식 출력

	poly_str = "f(x) = "

	for i in range(len(f_x)):
		term = t_x[i] #지수
		coefficient = f_x[i]  # 계수

		return_value = poly_str + f'{coefficient}x^{term} '

	return return_value


def calc_poly(x_value, t_x, f_x):
	retValue = 0
	term = len(f_x) - 1  # 최고차항 숫자 = 배열길이-1

	for i in range(len(f_x)):
		term = t_x[i]
		coefficient = f_x[i]  # 계수
		retValue += coefficient * x_value ** term

	return retValue


## 전역 변수 선언 부분 ##
tx = [300, 20, 0]
fx = [7, -4, 5]  # = 2x^4 +3x^3 +4x^2 +0x^1 -9x^0

## 메인 코드 부분 ##
if __name__ == "__main__":
	print(print_poly(tx, fx))

	print(calc_poly(int(input("X 값 : ")), tx, fx))



