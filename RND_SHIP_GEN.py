from random import random
#const
WIDTH=7
HEIGHT=7
ROT_NONE  = [0, 0]
ROT_UP    = [-1,0]
ROT_LEFT  = [0, 1]
ROT_DOWN  = [1, 0]
ROT_RIGTH = [0,-1]
VIS_NONE  = ' '
VIS_WALL  = '█'
VIS_COLL  = 'O'
VIS_DOOR  = '#'
BAG_COMPONENTS =   {"BDoor":2,  "SDoor":2,  "BWall":1,  "SWall":2,  "-Coll":6   }
BRD_COMPONENTS =   {"BDoor":[], "SDoor":[], "BWall":[], "SWall":[], "-Coll":[]  }
DEBUG = True
#data
field = None
bag_components = None
brd_components = None
def reset_data():
    global field, bag_components, brd_components, vis_components
    field = [[VIS_NONE for _ in range(WIDTH)] for _ in range(HEIGHT)]
    bag_components = dict(BAG_COMPONENTS)
    brd_components = {x[0]:x[1] for x in BRD_COMPONENTS.items()}
def show_field():
    for row in range(HEIGHT):
        for col in range(WIDTH):
            print(field[row][col],end='')
        print()
#supporters
def rand_rot():
    return rand_sort([ROT_UP, ROT_LEFT, ROT_DOWN, ROT_RIGTH])[0]
def rand_sort(arr):
    return sorted(arr, key=lambda x:random())


def add_to_board(comp_pos, comp_tag, comp_rot=ROT_NONE):
    global field, bag_components, brd_components
    comp_con = [comp_pos[1]+comp_rot[1], comp_pos[0]+comp_rot[0]]
    err = None
    #validation
    if comp_tag not in bag_components:
        err = "comp_tag not found"
    elif bag_components[comp_tag] == 0:
        err = "component rаn out"
    elif not (0<=comp_pos[1]<WIDTH and 0<=comp_pos[0]<HEIGHT): 
        err = "comp_pos out of bounds"
    elif not (0<=comp_con[1]<WIDTH and 0<=comp_con[0]<HEIGHT): 
        err = "comp_con out of bounds"
    elif field[comp_pos[1]][comp_pos[0]]!=VIS_NONE or field[comp_con[0]][comp_con[1]]!=VIS_NONE:
        err = "comp_pos occupied"
    if err: 
        if DEBUG: print(f"ERR:{err}; tag:{comp_tag}; pos:{comp_pos}; con:{comp_con}")
        return False
    #comp_vis
    if comp_tag=="BDoor":
        comp_vis = [VIS_DOOR,VIS_DOOR]
    if comp_tag=="SDoor":
        comp_vis = [VIS_DOOR,VIS_WALL]
    if comp_tag=="BWall":
        comp_vis = [VIS_WALL,VIS_WALL]
    if comp_tag=="SWall":
        comp_vis = rand_sort([VIS_WALL,VIS_WALL])
    if comp_tag=="-Coll":
        comp_vis = [VIS_COLL,VIS_COLL]
    #field
    field[comp_pos[1]][comp_pos[0]] = comp_vis[0]
    field[comp_con[0]][comp_con[1]] = comp_vis[1]
    #bag
    bag_components[comp_tag] -= 1
    #brd
    brd_components[comp_tag].append(comp_pos)
    if comp_pos != comp_con: brd_components[comp_tag].append(comp_con)
    return True

def gen():
    reset_data()

    add_to_board([WIDTH//2,HEIGHT//2],"-Coll")

    while bag_components["-Coll"]:
        coll_old_pos = rand_sort(brd_components["-Coll"])[0]
        coll_new_dir = rand_rot()
        coll_new_pos = [coll_old_pos[0]+coll_new_dir[0]*3, coll_old_pos[1]+coll_new_dir[1]*3]
        coll_new_con = [coll_old_pos[0]+coll_new_dir[0], coll_old_pos[1]+coll_new_dir[1]]
        if add_to_board(coll_new_pos,"-Coll"):
            comps = []
            for type in ["BDoor","SDoor","BWall"]: comps += [type] * bag_components[type]

            if coll_old_pos == [WIDTH//2,HEIGHT//2]:
                for type in ["BDoor","SDoor"]: comps += [type] * bag_components[type]
                if not comps:
                    return False
            else:
                for type in ["BDoor","SDoor","BWall"]: comps += [type] * bag_components[type]

            add_to_board(coll_new_con,rand_sort(comps)[0],coll_new_dir)
    return True
    
        


# if __name__ == "__init__":
while True:
    if gen():
        input()
        show_field()