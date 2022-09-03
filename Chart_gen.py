import random
# ▲ ⚜ ⚰ ⚙ ☸ ⚀ ⚁ ⚂ ⚃ ⚄ ⚅
# ①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳
# ▤▥▦▧▨▩▢▣◌◻◼◽◾

class PlanetTile:
	pass

class PlanetChart:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.data = 0

	def print(self):
		pass

chart_h_chars=[" ","░","▒","▓","█"]
chart_l_chars=["◻","◼","◽","◾"]
		
def chart_char(height):
	pass


def convert_chart(chart):
	for y in range(len(chart)):
		for x in range(len(chart[y])):
			if chart[y][x]//chart_diff>=len(chart_chars):
				chart[y][x] = "E"
			else:
				chart[y][x] = chart_chars[chart[y][x]//chart_diff]
	return chart
def print_chart(chart):
	chart=convert_chart(chart)
	print('\n'.join([''.join(l) for l in chart]))



def chart_gen(width,heigt, test=0, max_val=4):
	new_chart = [[0 for _ in range(width)] for _ in range(heigt)]

	for _ in range(test):
		h, w = random.randint(0,heigt-1), random.randint(0,width-1)
		if new_chart[h][w]<max_val:
			new_chart[h][w]+=1
	# print(new_chart)
	return(new_chart)



# c_width,c_heigt = 7,5

# for i in range(10):
# 	print("-"*c_width)
# 	print_chart(chart_gen(c_width,c_heigt,10))
# 	print("-"*c_width)

def adjacent_min(noise):
    output = []
    for i in range(len(noise) - 1):
        output.append(min(noise[i], noise[i+1]))
    return output

from math import sin
mapsize = 100
mult=10
test=[int((sin(i*0.511)+1)*mult) for i in range(mapsize)]
for i in test:
    print("█"*i)
print(0, [sin(i*0.293) for i in range(mapsize)])
for i in range(5):
    # random.seed(i)
    noise = [random.randint(1, 3) for i in range(mapsize)]
    print_chart(i, adjacent_min(adjacent_min(noise)))

# import noise
# # help(noise.pnoise3)
# # print(dir(noise))
# c_width,c_heigt= 20,20
# print(type(noise.pnoise1(1)))
# print([noise.pnoise1(x) for x in range(c_width)])

# value = [[] for i in range(c_heigt)]

# for y in range(c_heigt):
#     for x in range(c_width): 
#         nx = x/c_width - 0.5
#         ny = y/c_heigt - 0.5
#         value[y][x] = noise(nx, ny)

