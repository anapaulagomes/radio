from datetime import datetime
import logging
import sounddevice
import soundfile
import time

logging.basicConfig(
    filename='logs/radio-{}.log'.format(datetime.now().date()),
    filemode='a',
    level=logging.DEBUG,
    format='%(asctime)s %(message)s'
)


def play_inaudible_audio():
    data, fs = soundfile.read('inaudible.wav', dtype='float32')
    sounddevice.play(data, fs)
    status = sounddevice.wait()
    if status:
        logging.error('Error during playback: ' + str(status))
    else:
        logging.warning('Played successfuly')


if __name__ == '__main__':
    while True:
        play_inaudible_audio()
        time.sleep(500)  # 8 minutes and 20 seconds
