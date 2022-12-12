
import numpy as np
import matplotlib.pyplot as plt
from os.path import dirname, join as pjoin
##import time
import scipy
from scipy.io.wavfile import write
import wave
import math
##from pydub import AudioSegment
##import nazo
from flask import Flask, render_template, request
from numpy import frombuffer

site = Flask(__name__)




@site.route('/')
def index():
    return render_template("sound.html", message="type number")



@site.route("/trainsoundpost", methods=["POST"])
def trainsoundsound():
    print("complated")
    global end2
    global maxspee
    global acceleration
    global deceleration
    
    


    global g1
    global g2

    end2 = request.form.get("runningtime")
    maxspee = request.form.get("maxiumspeed")
    acceleration = request.form.get("acceleration")

    deceleration = request.form.get("deceleration")
    g1 = request.form.get("biggearratio")
    g2 = request.form.get("smallgearratio")


    


        
end1 = 0
#時間（秒）
##timestart = 0
##0 <= timestart <= end1
##timestart = time.time()
##end2 = 0
end92 = end2 * 44100
##acceleration = nazo.cli.accelation
acceleration2 = acceleration * 1000 / 3600
brake = -3.5
bnake = brake * 1000 / 3600
spee = 0
spee2=0
j = 0
u = 0
nanashi2 = 0
end4 = 0
end7 = 0
end9 = 0
diameter = 860
diameter2 = diameter / 1000
x = diameter2 * math.pi
#人は死ぬ　いつか死ぬ
g1 = 82
g2 = 17
y = g1 / g2
nanashi = 0
theendsoon = 0
for end111 in range(end7):
    end111 = + 1



    global end137
    end137 = end111 - 1



    
    
    
    exec(end137 = [{}.wav].format(end111))
    ##end111 = (end92 - 1) /44100 + 1
    time3 =  end92 - (maxspee / (brake * 1000 /3600)) * 44100
    time4 = end92 - time3
    time2 = (maxspee / (acceleration * 1000 / 3600)) * 44100
    if end2 >= 79380000:
        break
    print ('最高速度(km/h)',maxspee, '\n直径',diameter, '\n時速(km/h)',spee, '\n加速度(km/h/s)', acceleration, '経過時間',end111)
    if 0 <= end111 <= time2:
        spee = 0 + acceleration2 * end2 /44100
    if time2 < end111 < time3:
        spee = spee2
    if time3<= end111 < end1:
        spee = spee2 + (time4 * bnake)
    
    frequency = spee / x
    f = frequency * y * g2
    rate = 44410
    ##phase = np.cumsum(2 * np.pi * f / rate * np.ones(int(rate * end2)))
    sec = 1.0
    hurehaba = 1.0
    
    # 波形を生成
    wave = np.arrange(0, sec, 1 / rate)  # -1.0 〜 1.0 の値のサイン波
    # import scipy.signal して、
# wave = scipy.signal.sawtooth(phases) とすると鋸歯状波、
# wave = scipy.signal.square(phases) とすると矩形波になる
    # 16bit の wav ファイルに書き出す



    wave2 = hurehaba * np.sin(2*np.pi*f*wave)
    plt.plot(wave, wave2)
    
    ##wave = (wave * float(2 ** 15 - 1)).astype(np.int16)  # 値域を 16bit にする
    ##g = scipy.io.wavfile.write('sinesinesinesine' + str[end2] + 'a.wav', rate, wave)
    ##p = {}.setparams(nchannels = 1, sampwidth = 2, framerate = rate, nframes = rate, comptype = None, compname = "not compressed")
    end4 = end2
    nanashi13 = range(end7)
    exec('{} = None'.format(nanashi13))



    exec(scipy.io.wavfile.write(end137, samplerate, 44100, wave2(np.int16)))





def join_waves(inputs, output):
    '''
    inputs : list of filenames
    output : output filename
    '''
    try:
        fps = [wave.open(f, 'r') for f in inputs]
        fpw = wave.open(output, 'w')

        fpw.setnchannels(fps[0].getnchannels())
        fpw.setsampwidth(fps[0].getsampwidth())
        fpw.setframerate(fps[0].getframerate())
        
        for fp in fps:
            fpw.writeframes(fp.readframes(fp.getnframes()))
            fp.close()
        fpw.close()

    except wave.Error:
        print("waveerror")

    except Exception:
        print("error")
end = 0

if __name__ == '__main__':
    inputs = [str(n) + '.wav' for n in range(end2)]
    output = 'sine.wav'
    end = "compleated!?"







@app.route("/")
def site2():
    return render_template("sound.html", result = end)

    ##join_waves(inputs, output)    
##if end2 == end7:
    ##l = range(3980000)
    ##h = AudioSegment.empty()

    ##for nanashi in range(end7):
        ##v = h.append(AudioSegment.from_file(file=end137[nanashi]))
        ##exec(v)
    #sound1 = AudioSegment.from_file('imput' + str(nanashi) +"a.mp3"))
##if nanashi >= end7:
    ##for nanashi11 in h:
        ##nanashisound += nanashi11
        ##thend = 1
##if theendsoon == 1:
    ##sound = nanashisound.speedup(playback_speed = 44100)
##    sound.export("sound.wav", format = "wav")

        
    







