from pygame import mixer

mixer.init()

mixer.music.load('./Fake Love Song.mp3')
mixer.music.play()
x = input('Digite algo para parar...')
