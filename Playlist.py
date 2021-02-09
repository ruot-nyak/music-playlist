from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None
  
  def add_song(self, title):
    new_song = Song(title)
    new_song.set_title(title)
    new_song.set_next_song(self.__first_song)
    self.__first_song = new_song


  def find_song(self, title):
    counter = 0
    current_song = self.__first_song

    while current_song.get_title() != title:
        counter += 1
        current_song = current_song.get_next_song()
        if current_song == None:
            return -1

    if current_song.get_title() == title:
        return counter


  
  def remove_song(self, title):
    current_song = self.__first_song
    if current_song.get_title() == title:
        #set the first song of the global list as the next song in the list
        self.__first_song = current_song.get_next_song()
        return print(f'{title} Deleted')
        #The function above only works if the song is in the first index

    else:
        #While the current song (first song in list) is not equal to the title,
        while current_song.get_title() != title:
            #If our current song equals the title
            if current_song.get_next_song().get_title() == title:
                current_song(current_song.get_next_song())
                return print(f'{title} Deleted')
        #Change the local current song to the next song
            else:
                current_song = current_song.get_next_song()


  def length(self):
    counter = 0
    current_song = self.__first_song

    while current_song != None:
        counter += 1
        current_song = current_song.get_next_song()
    return counter


  def print_songs(self):
    counter = 0
    current_song = self.__first_song

    while current_song != None:
        counter += 1
        print(f"{counter}. {current_song.get_title()}")
        current_song = current_song.get_next_song()

    if counter == 0:
        return False


