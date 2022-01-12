#  Алгоритм Бойера-Мура-Хорспула для поиска образа строки

s = 'данные'
n = len(s)
d = {}

new_s = s[::-1]
for i in range(1, n):
	if new_s[i] not in d:
		d[new_s[i]] = i

print(d)


if s[-1] not in d:
	d[s[-1]] = d[list(d.keys())[-1]] + 1
print(d)




a = 'большие метеоданные'
