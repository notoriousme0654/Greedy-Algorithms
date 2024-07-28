# 11. Find maximum meetings in one room

class meeting:
	def __init__(self, start, end, pos):
		self.start = start
		self.end = end
		self.pos = pos
def maxMeeting(l, N):
	ans = []
	l.sort(key=lambda x: x.end)
	ans.append(l[0].pos)
	time_limit = l[0].end
	for i in range(1, N):
		if l[i].start > time_limit:
			ans.append(l[i].pos)
			time_limit = l[i].end
	for i in ans:
		print(i + 1, end=" ")
	print()
if __name__ == '__main__':
	s = [1, 3, 0, 5, 8, 5]
	f = [2, 4, 6, 7, 9, 9]
	N = len(s)
	l = []
	for i in range(N):
		l.append(meeting(s[i], f[i], i))
	maxMeeting(l, N)
