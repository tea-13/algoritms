# Алгоритм КМП (Кнута-Морриса-Прата) для нахождения подстроки
s = 'лилила'
j = 0
p = [0]*len(s)
for i in range(1, len(s)):
	if s[i] != s[j]:
		if j == 0:
			p[i] = 0
		else:
			j = p[i-1]
	else:
		p[i] = (j+1)
		j += 1

print(p)

a = 'лилилось лилилась'
m = len(a)
n = len(s)-1
j = 0
for i in range(m):
	if a[i] == s[j]:
		if j == n:
			print(f'string found: {a[i-n : i+1]} {[i-n, i]}')
			break
		j += 1
	else:
		if j > 0:
			j = p[j-1]

	if i == m-1:
		print('string not found')
