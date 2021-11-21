import tkinter as tk
from tkinter import messagebox
import webbrowser
from resources.SpotifyResources import getMinePlaylists, getPlaylist, copyPlaylist
from resources.RepositoryController import getLocalSavesPlaylists

#####  def metods

def avisoLicencia():
	messagebox.showwarning("Localfy", "Producto bajo licencia de Iván Cárdenas Meneses")

def salirAplicacion():
	valor = messagebox.askokcancel("Salir", "¿Deseas salir de la aplicacion?")
	if valor == True:
		index.destroy()

def showMinePlaylists():

    # Devuelve las playlist del usuario de Spotify

    playlists = getMinePlaylists()

    ##### View Show Mine Playlists

    showPlaylistView = tk.Toplevel(index)
    showPlaylistView.title('Mis Playlists')
    showPlaylistView.iconbitmap('images/localfy_favicon1.ico')

    frameShowPlaylistView = tk.Frame(showPlaylistView, width=800, height=600)
    frameShowPlaylistView.config(bd=25)
    frameShowPlaylistView.config(bg="white")
    frameShowPlaylistView.pack()

    i = 0

    for playlist in playlists:

        label = tk.Label(frameShowPlaylistView, text=playlist.getName())
        label.config(bg="white")
        label.grid(row=i, column=0, sticky="w", padx=20, pady=10)
        idPlaylist=playlist.getId()
        boton = tk.Button(frameShowPlaylistView, text="Ver", background="lightblue", command=lambda idPlaylist=idPlaylist : searchPlaylistById(idPlaylist))
        boton.grid(row=i, column=2, padx=10, pady=10 )
        i = i + 1

def showMineLocalPlaylists():

    # Muestra las playlists que estan guardadas localmente.

    try:

        lista = getLocalSavesPlaylists()

        ##### View Show Mine Playlists

        showPlaylistView = tk.Toplevel(index)
        showPlaylistView.title('Mis Playlists Guardadas (Local)')
        showPlaylistView.iconbitmap('images/localfy_favicon1.ico')

        frameShowPlaylistView = tk.Frame(showPlaylistView, width=800, height=600)
        frameShowPlaylistView.config(bd=25)
        frameShowPlaylistView.config(bg="white")
        frameShowPlaylistView.pack()

        i = 0

        for l in lista:

            label = tk.Label(frameShowPlaylistView, text=l)
            label.config(bg="white")
            label.grid(row=i, column=0, sticky="w", padx=20, pady=10)
            boton = tk.Button(frameShowPlaylistView, text="Ver", background="lightblue", command=lambda: searchPlaylistById(lista[l]))
            boton.grid(row=i, column=2, padx=10, pady=10)
            i = i + 1
    except:
        messagebox.showwarning("Localfy",'Error')

def searchPlaylistById(id):

    # Recibe un id de playlist y devuelve las canciones de dicha playlist con su id.

    try:

        playlist = getPlaylist(id)

        ##### View Show Mine Playlists

        showPlaylistView = tk.Toplevel(index)
        showPlaylistView.iconbitmap('images/localfy_favicon1.ico')
        showPlaylistView.title('Playlist Encontrada')

        frameShowPlaylistView = tk.Frame(showPlaylistView, width=800, height=600)
        frameShowPlaylistView.config(bd=25)
        frameShowPlaylistView.config(bg="white")
        frameShowPlaylistView.pack()

        nombreLabel = tk.Label(frameShowPlaylistView, text=str(playlist.getName()))
        nombreLabel.config(bg="white")
        nombreLabel.grid(row=0, column=0, sticky="w", padx=20, pady=25)

        buttonCopyPlaylist = tk.Button(frameShowPlaylistView, text="Guardar esta Playlist", background="lightblue", command=lambda: copyPlaylistView(id))
        buttonCopyPlaylist.grid(row=0, column=1, padx=10, pady=25)

        i = 0

        for track in playlist.getTracks():
            label = tk.Label(frameShowPlaylistView, text=str(track.getName()+' - '+track.getArtist().getName()))
            print(track.getName()+' - '+track.getArtist().getName()+' - '+track.getId())
            label.config(bg="white")
            label.grid(row=i +1, column=0, sticky="w", padx=20, pady=10)
            idtrack = track.getId()
            buttonListen = tk.Button(frameShowPlaylistView, text="Abrir en Reproductor", background="lightblue", command= lambda idtrack = idtrack: listenSong(idtrack))
            buttonListen.grid(row=i+1, column=1, padx=10, pady=10)
            i = i + 1
    except:
        messagebox.showwarning("Localfy", "La ID introducida no es válida.")

def copyPlaylistView(id):
    
    # Copia una playlist cualquiera en tus playlist

    try:
        copyPlaylist(id)
        messagebox.showwarning("Localfy","Playlist guardada con éxito.")
    except:
        messagebox.showwarning("Localfy","No ha podido copiarse la playlist.")

def listenSong(id):
    # el id puede ser de artista, de cancion o de album
    # se ejecuta la url dada
    try:
        webbrowser.open('https://open.spotify.com/embed/track/' + id)
    except:
        print('ERROR LISTEN SONG')
    # el id puede ser de artista, de cancion o de album 

#####   Index Interface

index = tk.Tk()
index.title('Localfy')
index.iconbitmap('images/localfy_favicon1.ico')
frameIndex = tk.Frame(index, width=800, height=600)
frameIndex.config(bd=25)
frameIndex.config(bg="white")

frameIndex.pack()

logo_image = tk.PhotoImage(file="images/localfy_logo.png")
label_logo = tk.Label(frameIndex, image=logo_image)
label_logo.grid(row=0, column=1, padx=10, pady=10)

barraMenu = tk.Menu(index)
index.config(menu=barraMenu, width=300, height=300)

form_playlist = tk.Entry(frameIndex)
form_playlist.grid(row=1, column=1, padx=20, pady=10)
form_playlist.config(fg="blue", justify="center", width=50)

buttonSearch = tk.Button(frameIndex, text="Buscar Playlist", background="lightblue", command= lambda: searchPlaylistById(form_playlist.get()))
buttonSearch.grid(row=2, column=1, padx=10, pady=10)

buttonMinePlaylists = tk.Button(frameIndex, text="Mis Playlist Spotify", background="lightblue", command= showMinePlaylists)
buttonMinePlaylists.grid(row=6, column=1, padx=10, pady=10)

buttonMineLocalPlaylist = tk.Button(frameIndex, text="Mis Playlist Guardadas", background="lightblue", command=showMineLocalPlaylists)
buttonMineLocalPlaylist.grid(row=7, column=1, padx=10, pady=10)

##### Mantener abierto 

index.mainloop()
