import pygame
import numpy as np
import pyaudio
from scipy import signal

# Инициализация Pygame
pygame.init()
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()

# Инициализация PyAudio
p = pyaudio.PyAudio()
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 2048

stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK
)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Чтение аудиоданных из потока
    data = stream.read(CHUNK)

    # Преобразование байтовых данных в числовой массив
    audio = np.frombuffer(data, dtype=np.int16)

    # Расчет спектрограммы
    frequencies, times, spectrogram_data = signal.spectrogram(
        audio, fs=RATE, window='hann', nperseg=2048, noverlap=1024
    )

    # Отображение спектрограммы на экране Pygame
    screen.fill((0, 0, 0))  # Очистка экрана
    # Ваш код для отображения спектрограммы на экране Pygame

    pygame.display.flip()  # Обновление экрана
    clock.tick(30)  # Ограничение FPS

# Завершение работы PyAudio
stream.stop_stream()
stream.close()
p.terminate()

# Завершение работы Pygame
pygame.quit()
