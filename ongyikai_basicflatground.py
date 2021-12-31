from vpython import *
#GlowScript 3.0 VPython

#ground=box(pos=vec(0,0,0),size=vec(1000,1000,0.1),color=color.white)
xaxis=cylinder(axis=vec(10,0,0),pos=vec(-5,0,0), radius=0.05,color=color.gray(0.5))
yaxis=cylinder(axis=vec(0,10,0),pos=vec(0,-5,0), radius=0.05,color=color.gray(0.5))
zaxis=cylinder(axis=vec(0,0,10),pos=vec(0,0,-5), radius=0.05,color=color.gray(0.5))

xaxisArrow=cone(axis=vec(0.5,0,0), pos=vec(5,0,0),radius=0.15,color=color.gray(0.5))
yaxisArrow=cone(axis=vec(0,0.5,0), pos=vec(0,5,0),radius=0.15,color=color.gray(0.5))
zaxisArrow=cone(axis=vec(0,0,0.5), pos=vec(0,0,5),radius=0.15,color=color.gray(0.5))

xaxislabel=text(text='x',pos=vec(5.5,0,0))
yaxislabel=text(text='y',pos=vec(0,5.5,0))
zaxislabel=text(text='z',pos=vec(0,0,5.5))


ball=sphere(radius=0.1, pos=vec(0,0.01,0),make_trail=True, trail_type='curve', trial_radius=0.01)
#initial velocity
ball.v=vec(3,4,0)
#acceleration
ball.a=vec(0,-9.81,0)


scene.camera.follow(ball)

#motion
t=0
dt=0.01
 #use euler method, v'=v+a dt
while ball.pos.y>0:
    rate(10)
    ball.v+=ball.a*dt
    ball.pos+=ball.v*dt
    t+=dt

print('ball lands at t=',t,"seconds, with position",ball.pos)
