current_movies= {'the glich': '11:30am',
                 'Rudolph':'1:00pm',
                 'Frostry the Snowman':'3:00pm',  
                 'Christmas vacation':'5:00pm'}

print(" we're showing the following movies: ")
for i in current_movies:
    print(i)

  

movie = input("What movies would you like the show time")

showtime = current_movies.get(movie)
if showtime == None:
    print("Requested movie is not available")
else:
    print(movie ,"is playing at", showtime)