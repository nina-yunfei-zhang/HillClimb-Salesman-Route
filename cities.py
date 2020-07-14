import random
from math import sqrt
from tkinter import *

def all_pairs(size,shuffle=random.shuffle):
    r1=list(range(size))
    r2=list(range(size))
    if shuffle:
        shuffle(r1)
        shuffle(r2)
    for i in r1:
        for j in r2:
            yield (i,j)
    #passed tests

def reversed_sections(tour):
    '''generator to return all possible variations where the section between two cities are swapped'''
    for i,j in all_pairs(len(tour)):
        if i != j:
            copy=tour[:]
            if i < j:
                copy[i:j+1]=reversed(tour[i:j+1])
            else:
                copy[i+1:]=reversed(tour[:j])
                copy[:j]=reversed(tour[i+1:])
            if copy != tour:
                yield copy
    # passed tests

def swap_cities(tour):
    for i,j in all_pairs(len(tour)):
        if i < j:
            copy=tour[:]
            copy[i]=tour[j]
            copy[j]=tour[i]
            yield copy
    # passed tests

def shift_cities(tour):
    for i,j in all_pairs(len(tour)):
        if i < j:
            copy=[]
            if  j<len(tour):
                copy.extend(tour[0:i])
                copy.extend(tour[j:j+1])
                copy.extend(tour[i:j])
                copy.extend(tour[j+1:])
            elif  j==len(tour):
                copy.extend(tour[1,j])
                copy.extend(tour[0:1])
            if copy != tour:
                yield copy

    # passed tests

def cartesian_matx(coords):
    '''create a distance matrix for the city coords that uses straight line distance'''
    matrix={}
    for i,(x1,y1) in enumerate(coords):
        for j,(x2,y2) in enumerate(coords):
            dx,dy=x1-x2,y1-y2
            dist=sqrt(dx*dx + dy*dy)
            matrix[i,j]=dist
    return matrix

def read_cities(coord_file):

    infile=open(coord_file,"r")
    coords=[]
    for line in infile:
        s,c,x,y=line.split("\t")
        coords.append((round(float(x),2),round(float(y),2)))
    return coords

    #coords is a list of coordinates

def read_cities_with_name(coord_file):

    infile=open(coord_file,"r")
    coords_with_name=[]
    for line in infile:
        s,c,x,y=line.split("\t")
        coords_with_name.append((str(c),((round(float(x),2)+90.00)*7,(round(float(y),2)+180.00)*7)))
    return coords_with_name

def compute_total_distance(cartesian_matx,tour):
    '''total up the total length of the tour based on the cartesian_matx'''
    total=0
    num_cities=len(tour)
    for i in range(num_cities):
        j=(i+1)%num_cities
        (xi,yi)=tour[i]
        (xj,yj)=tour[j]
        dx,dy=xi-xj,yi-yj
        total+=sqrt(dx*dx + dy*dy)
    return total

    # passed tests

def run_hillclimb(init_function,move_operator,objective_function,max_iterations):
    from hillclimb import hillclimb_and_restart
    iterations,score,best=hillclimb_and_restart(init_function,move_operator,objective_function,max_iterations)
    return iterations,score,best

def find_best_cycle(init_function,move_operator,objective_function,max_iterations):
    iterations,score,best=run_hillclimb(init_function,move_operator,objective_function,max_iterations)

    return iterations,score,best

def print_cities(matrix,best_tour):
    print("The route is ", best_tour)
    print("Total distance is ",compute_total_distance(matrix,best_tour))
    
def visualise(canv, city_list,name_final_list):
    """draws city"""
    for city in city_list:
        draw_city(canv, name_final_list, city[0], city[1])
        draw_city(canv, name_final_list, city_list[0][0], city_list[0][1], color='red', name='Start')
        
    #draw lines between them
    for i in range(len(city_list)-1):
        canv.create_line(city_list[i][0],city_list[i][1],city_list[i+1][0],city_list[i+1][1])

    #draw a line that goes from the last city back to our home
    canv.create_line(city_list[-1][0], city_list[-1][1],city_list[0][0], city_list[0][1])
    
def draw_city(canv, name_final_list, x, y, color='yellow', name=None):
    """draws a city at coordinate position"""
    canv.create_oval(x-3, y-3, x+3, y+3, fill=color)

    # city name
    for i in range(len(name_final_list)):
      if name_final_list[i][1][0]== x and  name_final_list[i][1][1]== y:
          canv.create_text(x, y+5, text=name_final_list[i][0])
    
def main():
    #read file
    coords=read_cities("city-data.txt")
    
    #initialize random tour
    init_function=coords
    
    #construct distance matrix
    distance_matrix=cartesian_matx(coords)

    #Define objective function
    objective_function=lambda tour: -compute_total_distance(distance_matrix, tour)
    
    max_iterations=10000


    """
                                             Note
    _______________________________________________________________________________________________________
        Your can choose move_operator as  (Please put # in the front of the method you do not want to use)
            (1)reversed_sections   or 
            (2)shift_cities or swap_cities
        According to my test, the result of (1)reversed_section method is more reasonable.
    ________________________________________________________________________________________________________
    """

    #move_operator= reversed_sections                     #Choice (1)
    move_operator= shift_cities or swap_cities            #Choice (2)


    result=find_best_cycle(init_function,move_operator,objective_function,max_iterations)

    print_cities(distance_matrix,result[2])
    route_print=result[2]

    #--------------------------------Visualization------------------------------------

    """                                       Note
                     ________________________________________________________________
                       (1)The size of canvas is limited, so sometime when the 
                       coordinate is negative(like the data file provided 
                       in the initial setup document), the map will not
                       be shown in the middle of the canvas.(it may disappeared)
                       Therefore, I shift the map by adding 90.00 to latitude and 
                       180.00 to longitude.
                       
                       (2)The size of map is uncontrolled. Sometimes it is too 
                       compact. The route and city's name shown are unclear. 
                       Therefore, I multipled 7 to zoom the map.
                       (You can choose any zoom ratio by change this number) 
                     ________________________________________________________________
                       
    """

    route_print_final = []
    for i in range(len(route_print)):
        lattitude = (round(float(route_print[i][0]),2)+90.00)*7
        longtitude = (round(float(route_print[i][1]),2)+180.00)*7
        coordinates = (lattitude, longtitude)
        route_print_final.append(coordinates)

    #add name list
    name_final_list=read_cities_with_name("city-data.txt")

    #prepare window
    window = Tk()
    window.title('Visualize road maps')
    window.geometry('2000x2000')

    #prepare canvas
    canvas = Canvas(window, bg='#ADD8E6', height=2000, width=2000)
    canvas.pack()
    
    #add compass
    txtid=canvas.create_text(500,0, font=("Purisa", 30),anchor="nw")
    canvas.insert(txtid,1,"<--South   North -->")
    
    #draw route    
    city_list =route_print_final
    visualise(canvas,city_list,name_final_list)
    mainloop()
    
if __name__ == "__main__":
    main()
