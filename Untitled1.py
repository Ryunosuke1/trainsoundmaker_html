
import numpy as np
##import time
import scipy
from scipy.io.wavfile import write
import math
from pydub import AudioSegment
##import nazo
from flask import Flask, render_template, url_for, request, redirect

site = Flask(__name__)




@site.route('/')
def index():
    return render_template("sound.html", message="type number")



@site.route("/trainsoundpost", methods=["POST"])
def trainsoundsound():
    print("complated")
    global trainsound

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
end92 = nazo.ccli.end2
acceleration = nazo.cli.accelation
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
for end92 in range(end7):
    end92 = + 1
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
    phase = np.cumsum(2 * np.pi * f / rate * np.ones(int(rate * 1800)))
    
    
    # 波形を生成
    wave = np.sin(phase)  # -1.0 〜 1.0 の値のサイン波
    # import scipy.signal して、
# wave = scipy.signal.sawtooth(phases) とすると鋸歯状波、
# wave = scipy.signal.square(phases) とすると矩形波になる
    # 16bit の wav ファイルに書き出す
    
    wave = (wave * float(2 ** 15 - 1)).astype(np.int16)  # 値域を 16bit にする
    g = scipy.io.wavfile.write('sinesinesinesine' + str[end2] + 'a.wav', rate, wave)
    end4 = end2
    for nanashi2 in range(len(u)):
        nanashi7 = end2[u]
        exec(g.format(nanashi7))

    
nanashisound = AudioSegment.empty
if end2 == end7:
    l = range(3980000)
    h = AudioSegment.empty()

    for nanashi in range(end7):
        v = h.append(AudioSegment.from_file(file="sinesinesinesine" + str(nanashi) + 'a.wav'))
        exec(v)
    #sound1 = AudioSegment.from_file('imput' + str(nanashi) +"a.mp3"))
if nanashi >= end7:
    for nanashi11 in h:
        nanashisound += nananshi11
        thend = 1
if theendsoon == 1:
    sound = nanashisound.speedup(playback_speed = 44100)
    sound.export("sound.wav", format = "wav")

        
    







