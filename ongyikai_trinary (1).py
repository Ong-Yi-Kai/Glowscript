from vpython import *
#GlowScript 3.0 VPython
#scene.userspin=False
#scene.fov=0.01

#Axis
xaxis=cylinder(axis=vec(10,0,0),pos=vec(-5,0,0), radius=0.05,color=color.gray(0.5))
yaxis=cylinder(axis=vec(0,10,0),pos=vec(0,-5,0), radius=0.05,color=color.gray(0.5))
#zaxis=cylinder(axis=vec(0,0,10),pos=vec(0,0,-5), radius=0.05,color=color.gray(0.5))

xaxisArrow=cone(axis=vec(0.5,0,0), pos=vec(5,0,0),radius=0.15,color=color.gray(0.5))
yaxisArrow=cone(axis=vec(0,0.5,0), pos=vec(0,5,0),radius=0.15,color=color.gray(0.5))
#zaxisArrow=cone(axis=vec(0,0,0.5), pos=vec(0,0,5),radius=0.15,color=color.gray(0.5))

xaxislabel=text(text='x',pos=vec(5.5,0,0))
yaxislabel=text(text='y',pos=vec(0,5.5,0))
#zaxislabel=text(text='z',pos=vec(0,0,5.5))

# celestial bodies 
m=1          #mass of body in solar masses
r=0.684        #distance between bodies in Au
Body1=sphere( pos=vec(0,r/sqrt(3),0),radius=0.1,color=color.red, make_trail=True)
Body2=sphere(pos=vec(-0.5*r,-r/sqrt(12),0), radius=0.1, make_trail=True,color=color.green)
Body3=sphere(pos=vec(0.5*r,-r/sqrt(12),0), radius=0.1, make_trail=True, color=color.white)

#initial velocity and acceleration
v=10    #speed of planet 
Body1.v=vec(-v,0,0)
Body1.vmid=vec(-v,0,0)

Body2.v=vec(v*sin(pi/6),-v*cos(pi/6),0)
Body2.vmid=vec(v*sin(pi/6),-v*cos(pi/6),0)

Body3.v=vec(v*sin(pi/6),v*cos(pi/6),0)
Body3.vmid=vec(v*sin(pi/6),v*cos(pi/6),0)

#motion
t=0
dt=0.0001

while t<2.8:
    rate(2000)
    Body1.a=39.5*m*(1/mag(Body2.pos-Body1.pos)**2)*norm(Body2.pos-Body1.pos)+39.5*m*(1/mag(Body3.pos-Body1.pos)**2)*norm(Body3.pos-Body1.pos)
    #Body1.vmid+=Body1.a*0.5*dt
    Body1.v+=Body1.a*dt
    Body1.pos+= Body1.v*dt
    
    Body2.a=39.5*m*(1/mag(Body1.pos-Body2.pos)**2)*norm(Body1.pos-Body2.pos)+ 39.5*m*(1/mag(Body3.pos-Body2.pos)**2)*norm(Body3.pos-Body2.pos)
    #Body2.vmid+=Body2.a*0.5*dt
    Body2.v+=Body2.a*dt
    Body2.pos+=Body2.v*dt
    
    
    Body3.a=39.5*m*(1/mag(Body1.pos-Body3.pos)**2)*norm(vec(Body1.pos-Body3.pos))+ 39.5*m*(1/mag(Body2.pos-Body3.pos)**2)*norm(Body2.pos-Body3.pos)
    #Body3.vmid+=Body3.a*0.5*dt
    Body3.v+=Body3.a*dt
    Body3.pos+=Body3.v*dt
    
    
    t+=dt