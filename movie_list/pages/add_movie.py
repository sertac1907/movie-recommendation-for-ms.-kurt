import streamlit as st

def get_movies():
    with open("PyhtonMegaCourse/Streamlit/movie_list/movies.txt","r") as file:
        movies = file.readlines()
    return movies

def write_movies(local_movies):
    with open("PyhtonMegaCourse/Streamlit/movie_list/movies.txt","w") as file:        
        file.writelines(local_movies)




writen_movie = st.text_input("Write a movie")
add_button = st.button("ADD")

movies = get_movies()


if add_button and writen_movie != "":
    if writen_movie + "\n" not in movies :
        movies.append(writen_movie + "\n")
    else:
        st.write("This movie had already added.")


write_movies(movies)

#st.write(movies)
