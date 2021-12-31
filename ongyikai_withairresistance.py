from vpython import *
#GlowScript 3.0 VPython
#axis
xaxis=cylinder(axis=vec(10,0,0),pos=vec(-5,0,0), radius=0.01,color=color.gray(0.5))
yaxis=cylinder(axis=vec(0,10,0),pos=vec(0,-5,0), radius=0.01,color=color.gray(0.5))
zaxis=cylinder(axis=vec(0,0,10),pos=vec(0,0,-5), radius=0.01,color=color.gray(0.5))

xaxisArrow=cone(axis=vec(0.5,0,0), pos=vec(5,0,0),radius=0.05,color=color.gray(0.5))
yaxisArrow=cone(axis=vec(0,0.5,0), pos=vec(0,5,0),radius=0.05,color=color.gray(0.5))
zaxisArrow=cone(axis=vec(0,0,0.5), pos=vec(0,0,5),radius=0.05,color=color.gray(0.5))

xaxislabel=text(text='x',pos=vec(5.5,0,0))
yaxislabel=text(text='y',pos=vec(0,5.5,0))
zaxislabel=text(text='z',pos=vec(0,0,5.5))

#specifications for the ball
ballmass=0.8
ballradius=0.5
ballsize=(4/3)*pi*(ballradius)**2
ball=sphere(radius=ballradius, pos=vec(0,0.01,0),make_trail=True, trail_type='curve', trial_radius=0.01)

#initial velocity
ball.v=vec(10,9,0)
#acceleration
g=vec(0,-9.81,0)

#air resistance
k=0.1*ballmass*ballsize
FairMagnitude=k*(mag(ball.v))**2
Fair=-FairMagnitude* norm(ball.v)

#net acceleration
ball.a=g+(Fair/ballmass)

#camera
scene.camera.follow(ball)

#arrow
attach_arrow(ball,'v',shaftwidth=0.1,scale=0.5,color=color.green)

#graph
motiongraph=graph(title='velocity-time graph', xtitle='time[s]', ytitle='velocity',fast=False)
Vx=gcurve(color=color.blue)
Vy=gcurve(color=color.red)

    
#motion
def launch():
    t=0
    dt=0.001
     #use euler method, v'=v+a dt
    while ball.pos.y>0:
        rate(50)
        ball.v+=ball.a*dt
        ball.pos+=ball.v*dt
        Vx.plot(t,dot(ball.v,vec(1,0,0)))
        Vy.plot(t,dot(ball.v,vec(0,1,0)))
        t+=dt

    print('ball lands at t=',t,"seconds, with position",ball.pos)

button(text="launch",bind=launch)