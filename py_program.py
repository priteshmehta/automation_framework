candy = [1,1,1,1,1,1,3,2,5,6,7,8,9,12,13,14]
total_candy = len(candy)
give_away_candy = total_candy/2
unique_candy_list = list(set(candy))
unique_candy = len(unique_candy_list)




if unique_candy <= give_away_candy:
    print "remaining Candy: ",unique_candy
else:
    duplicate_candy = total_candy - unique_candy
    tmp = give_away_candy-duplicate_candy
    unique_candy = unique_candy - tmp
    print "remaining Candy: ", unique_candy