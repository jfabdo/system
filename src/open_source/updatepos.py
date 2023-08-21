def updatepos(pos,velocity,maxSpeed,FRICTION,state,dt):
    speed = velocity.length()
    if speed > maxSpeed:
        velocity.normalize()
        velocity *= maxSpeed
        speed = maxSpeed

    if state == 'Walking':
        frictionVal = FRICTION*dt
        if frictionVal > speed:
            velocity.set(0, 0, 0)
        else:
            frictionVec = -velocity
            frictionVec.normalize()
            frictionVec *= frictionVal

            velocity += frictionVec

    pos.setPos(pos.getPos() + velocity*dt)