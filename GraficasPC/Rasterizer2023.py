from gl import Renderer
import shaders

# El tama�o del FrameBuffer
width = 950
height = 950

# Se crea el renderizador
rend = Renderer(width, height)

# Le damos los shaders que se utilizar�s
rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.posterizationShader

# Cargamos los modelos que rederizaremos
rend.glLoadModel(filename = "model.obj",
                 textureName = "textures/model.BMP",
                 translate = (width/3, height/3, 0),
                 rotate = (45, 0, 0),
                 scale = (50,50,50))


# Se renderiza la escena
rend.glRender()

# Se crea el FrameBuffer con la escena renderizada
rend.glFinish("posterizationShader.bmp")