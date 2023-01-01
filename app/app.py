from flask import Flask, render_template, request
#pytube es una biblioteca de Python para descargar videos desde Youtube
from pytube import YouTube
#El módulo os en Python proporciona los detalles y la funcionalidad del sistema operativo.
import os

#E Modulo pathlib sirve para manipular las rutas de sistemas de archivos
from pathlib import Path

#Declarando nombre de la aplicación e inicializando
app = Flask(__name__)


     
#Creando un Decorador
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('public/index.html')



@app.route("/descargar-video", methods=['GET', 'POST'])
def descargarVideo():
    if request.method == 'POST':
        urlVideo              = request.form['urlVideo']
        print(urlVideo)
        videoYT = YouTube(urlVideo)

        path   = "Mis_Descargas"
        folder = "VideosYT"
        #Directorio para almacenar las descargas
        url_Descargas = str(Path.home() / path)
        print(Path.home())
        ##¿Descarga el video y lo guardo en "VideosYT" dentro de la carpeta de descargas
        videoYT.streams.get_highest_resolution().download(output_path=os.path.join(url_Descargas, folder))
        print(videoYT)
        return render_template('public/index.html')
    else:
        return render_template('public/index.html')
    
    
    
def interface():
    # python terminal input
    url = input('url: ')
    yt = YouTube(url)

    #the directory to store the downloads
    url_Descargas = str(Path.home() / "Downloads")

    # download the video and store it in a folder called "YoutubeVideos" inside the downloads folder
    yt.streams.get_highest_resolution().download(output_path=os.path.join(url_Descargas, 'YoutubeVideos'))

# calling the function
interface()

    
#Redireccionando cuando la página no existe
@app.errorhandler(404)
def not_found(error):
    return 'Ruta no encontrada'


if __name__ == '__main__':
    app.run(debug=True, port=5000)