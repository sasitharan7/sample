#import /usr/local/lib64/python2.7/site-packages/matplotlib as plt
import os

def find_area(area_length,area_width):
    """This function is to calculate the area by multiplying length and width and returns the caulcated area in acres"""
    one_acre = 43560
    area = (area_length*area_width)/one_acre
    return(round(area,2))

def find_number_of_wines(area, row_space,wine_space):
    """This function is to find the number of wines planted by passing total area, row spacing and wine spacing"""
    one_acre = 43560
    number_of_wines = area*one_acre/(row_space*wine_space)
    return(int(number_of_wines))

def generate_wine_names(verity,total_wines,r_space,w_space,row_length,column_length):
    """This function is to generate the wine names  in a
       by passing the verity of the wine, total number of wines, number os rows and number of wines per row"""
    wine_names = []
    for row in range(1, int((column_length/r_space))+1):
        if total_wines <=0 :
            break
        else:
            for column in range(1, int((row_length/w_space)) + 1):
                if total_wines <= 0:
                    break
                else:
                    total_wines -= 1
                    wine_names.append(verity + str(row) + str(column))
    return (wine_names)

def display_wines(total_wines,r_space,w_space,row_length,column_length,verity):
    """This function is to display the wines
       by passing the verity of  total number of wines, number os rows and number of wines per row"""
    plt.xlabel("Wines")
    plt.ylabel("Rows")
    plt.title("Graphical view of the wines in zone " + verity)
    for row in range(1, int((column_length / r_space)) + 1):
        if total_wines <=0 :
            break
        else:
            for column in range(1, int((row_length / w_space)) + 1):
                if total_wines <= 0:
                    break
                else:
                    total_wines -= 1
                    plt.scatter(column,row,marker='*',edgecolors=None)
    plt.show()

def time_to_strip_spray(wine_list):
    strip_spary = 0.0
    time_per_strip_spray = 120
    strip_spary = time_per_strip_spray * (len(wine_list))
    return(strip_spary)

def time_to_spray(wine_list):
    spary = 0.0
    time_per_spray = 180
    spary = time_per_spray * (len(wine_list))
    return (spary)


def time_to_longprune(wine_list):
    longprune = 0.0
    time_per_longprune = 180
    longprune = time_per_longprune * (len(wine_list))
    return (longprune)

def time_to_prune(wine_list):
    prune = 0.0
    time_per_prune = 120
    prune = time_per_prune * (len(wine_list))
    return (prune)

def time_to_wire_down(wine_list):
    wire_down = 0.0
    time_per_down = 60
    wire_down = time_per_down * (len(wine_list)/3)
    return(wire_down)

def time_to_wire_up(wine_list):
    wire_up = 0.0
    time_per_up = 240
    wire_up = time_per_up * (len(wine_list)/3)
    return(wire_up)

def time_to_check_irrigation(wine_list):
    irrigation = 0.0
    time_per_irrigation = 60
    irrigation = time_per_irrigation * (len(wine_list))
    return(irrigation)


def time_to_cluster_count(wine_list):
    clustercount = 0.0
    time_per_clustercount = 120
    clustercount = time_per_clustercount * (len(wine_list))
    return (clustercount)

def time_to_trunk_sucker(wine_list):
    trunk_sucker = 0.0
    time_per_trunk_sucker = 120
    trunk_sucker = time_per_trunk_sucker * (len(wine_list))
    return (trunk_sucker)

def time_to_crown_sucker(wine_list):
    crown_sucker = 0.0
    time_per_crown_sucker = 120
    crown_sucker = time_per_crown_sucker * (len(wine_list))
    return (crown_sucker)

def time_to_leaf_thin(wine_list):
    leaf_thin = 0.0
    time_per_leaf_thin = 120
    leaf_thin = time_per_leaf_thin * (len(wine_list))
    return (leaf_thin)

def time_to_fruit_thin(wine_list):
    fruit_thin = 0.0
    time_per_fruit_thin = 180
    fruit_thin = time_per_fruit_thin * (len(wine_list))
    return (fruit_thin)

def time_to_pick(wine_list):
    pick = 0.0
    time_per_pick = 120
    pick = time_per_pick * (len(wine_list))
    return (pick)

def cluster_count(wine_list):
    pass

def water_usage(wine_list):
    pass

def leaf_count(wine_list):
    pass

def fruit_count(wine_list):
    pass

def sec_to_time(sec):
    seconds_in_day = 86400
    seconds_in_hour = 3600
    seconds_in_minute = 60
    seconds = sec
    days = seconds // seconds_in_day
    seconds = seconds - (days * seconds_in_day)
    hours = seconds // seconds_in_hour
    seconds = seconds - (hours * seconds_in_hour)
    minutes = seconds // seconds_in_minute
    seconds = seconds - (minutes * seconds_in_minute)
    print("{0:.0f} days, {1:.0f} hours, {2:.0f} minutes, {3:.0f} seconds.".format(
        days, hours, minutes, seconds))


total_area = 0.0
total_number_of_wines = 0
total_strip_spray = 0.0
total_spray = 0.0
total_long_prune = 0.0
total_prune = 0.0
total_wire_down = 0.0
total_wire_up = 0.0
total_irrigation = 0.0
total_trunk_sucker = 0.0
total_crown_sucker = 0.0
total_cluster_count = 0.0
total_leaf_thin = 0.0
total_fruit_thin = 0.0
total_harvest = 0.0
wine_list = []
#zones = int(input("Enter number of Zones to calculate: "))
zones = int(os.environ["ZONES"])
print(zones)
while zones > 0:
    '''
    length = float(input("enter Length of the area "))
    width = float(input("enter Width of the area "))
    row_space = int(input("enter space between two rows "))
    wine_space = int(input("enter space between two wines "))
    wine_verity = (input("enter the wine verity "))
    '''
    length = float(os.environ["LENGTH"]) 
    width = float(os.environ["WIDTH"])
    row_space = int(os.environ["ROW_SPACE"])
    wine_space = int(os.environ["WINE_SPACE"])
    wine_verity = os.environ["ZONE_NAME"]
    area = find_area(length,width)
    total_area += area
    print("#" * 50)
    print("total " + wine_verity + " area is " + str(area)+ " acres")
    number_of_wines = find_number_of_wines(area,row_space,wine_space)
    total_number_of_wines += number_of_wines
    print("Total number of wines planted in area " + wine_verity + " is " + str(number_of_wines))
    wines_name = generate_wine_names(wine_verity,number_of_wines,row_space,wine_space,int(length),int(width))
    t_to_strip_spray = time_to_strip_spray(wines_name)
    total_strip_spray += t_to_strip_spray
    print("Time to do strip spray for " + wine_verity )
    sec_to_time(t_to_strip_spray)
    t_to_spray = time_to_spray(wines_name)
    total_spray += t_to_spray
    print("Time to do spray for " + wine_verity )
    sec_to_time(t_to_spray)
    t_to_longprune = time_to_longprune(wines_name)
    total_long_prune += t_to_longprune
    print("Time to do long prune for " + wine_verity )
    sec_to_time(t_to_longprune)
    t_to_prune = time_to_prune(wines_name)
    total_prune += t_to_prune
    print("Time to do prune for " + wine_verity )
    sec_to_time(t_to_prune)
    t_to_wiredown = time_to_wire_down(wines_name)
    total_wire_down += t_to_wiredown
    print("Time to do wire down for " + wine_verity )
    sec_to_time(t_to_wiredown)
    t_to_wireup = time_to_wire_up(wines_name)
    total_wire_up += t_to_wireup
    print("Time to do wire up for " + wine_verity )
    sec_to_time(t_to_wireup)
    t_to_irrigation = time_to_check_irrigation(wines_name)
    total_irrigation += t_to_irrigation
    print("Time to do irrigation check for " + wine_verity )
    sec_to_time(t_to_irrigation)
    t_to_trunk_sucker = time_to_trunk_sucker(wines_name)
    total_trunk_sucker += t_to_trunk_sucker
    print("Time to do trunk sucker for " + wine_verity )
    sec_to_time(t_to_trunk_sucker)
    t_to_crown_sucker = time_to_crown_sucker(wines_name)
    total_crown_sucker += t_to_crown_sucker
    print("Time to do crown sucker for " + wine_verity )
    sec_to_time(t_to_crown_sucker)
    t_to_clustercount = time_to_cluster_count(wines_name)
    total_cluster_count += t_to_clustercount
    print("Time to do cluster count for " + wine_verity )
    sec_to_time(t_to_clustercount)
    t_to_leaf_thin = time_to_leaf_thin(wines_name)
    total_leaf_thin += t_to_leaf_thin
    print("Time to do leaf thin for " + wine_verity )
    sec_to_time(t_to_leaf_thin)
    t_to_fruit_thin = time_to_fruit_thin(wines_name)
    total_fruit_thin += t_to_fruit_thin
    print("Time to do fruit thin for " + wine_verity )
    sec_to_time(t_to_fruit_thin)
    t_to_pick = time_to_pick(wines_name)
    total_harvest += t_to_pick
    print("Time to do harvest for " + wine_verity )
    sec_to_time(t_to_pick)
    wine_list.append(wines_name)
    #print("Displaying the wines names ", next(wines_name))
    #display_wines(number_of_wines,row_space,wine_space,int(length),int(width),wine_verity)
    zones -= 1
    print("#" * 50)
print("Total area planted in acres is %.2f" %(total_area))
print("Total number of wines planted is %2d" %(total_number_of_wines))
print("total time to do strip spray ")
sec_to_time(total_strip_spray)
print("total time to do spray ")
sec_to_time(total_spray)
print("total time to do long prune ")
sec_to_time(total_long_prune)
print("total time to do prune ")
sec_to_time(total_prune)
print("total time to do wire down ")
sec_to_time(total_wire_down)
print("total time to do wire up ")
sec_to_time(total_wire_up)
print("total time to do check irrigation ")
sec_to_time(total_irrigation)
print("total time to do trunk sucker ")
sec_to_time(total_trunk_sucker)
print("total time to do crown sucker ")
sec_to_time(total_crown_sucker)
print("total time to do cluster count ")
sec_to_time(total_cluster_count)
print("total time to do leaf thin ")
sec_to_time(total_leaf_thin)
print("total time to do fruit thin ")
sec_to_time(total_fruit_thin)
print("total time to do harvest ")
sec_to_time(total_harvest)
print("#" * 50)

