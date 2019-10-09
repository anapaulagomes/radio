# Radio

An old radio with a new "spirit".

![picture of my vintage radio with a rasperry pi inside](https://pbs.twimg.com/media/DinjdllWsAAJBx0.jpg)

It can be used via audio cable, Bluetooth or Spotify.

## Hardware:

* An old radio with capacity to host a Raspberry PI and a speaker
* Raspberry PI 3b
* Speaker (I've been using JBL GO due to its size and sound quality)
* Audio Jack cable

## Requirements:

* Python 3
* numpy
* python-sounddevice
* python-soundfile

Optional:

* [Raspotify](https://github.com/dtcooper/raspotify)
(in order to make your radio as a Spotify Connect option)

## Running

JBL Go will turn off after 10 min of inactivity.
The script [awakening.py](awakening.py) will 
play an inaudible sound to keep it on.

    python awakening.py

You may need a few extra configuration to make the audio
system work with Raspotify.

Volume:

    amixer set Master -- 100%

Force output to Jack:

    sudo raspi-config  # advanced options

## Credits

* [Idea of playing an inaudible audio](https://forums.tomsguide.com/threads/prevent-speakers-standby-mode.375550/)
* [Command to create an inaudible audio](https://ubuntuforums.org/showthread.php?t=1911430)
* Bass Drum sample from [freewavesamples](https://freewavesamples.com/bass-drum-1)
(for testing purposes)
* [Ignore HDMI audio](https://github.com/dtcooper/raspotify/issues/82#issuecomment-383881443)
