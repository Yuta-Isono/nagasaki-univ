#!/usr/bin/env python2.7
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create("localhost")
pos = mc.player.getPos()

# write to original position here
x = -1881
y = 4
z = -638

pos.x = x
pos.y = y
pos.z = z

pos.x += 1931 
pos.y += -4
pos.z += 899


# Kounai no Yuka
for i in range(0, 32):
    for j in range(-1, 0):
        for k in range(-30, 2):
            mc.setBlock(pos.x+i, pos.y + j, pos.z+k, block.Block(1,6))


# Douro gawa no Yuka
for i in range(0, 32):
    for j in range(-1, 0):
        for k in range(0, 16):
            mc.setBlock(pos.x+i, pos.y + j, pos.z+k, block.Block(43,4))

#Hidari Gawa no Tuuro
for i in range(0, 9):
    for j in range(-1, 0):
        for k in range(0, 16):
            mc.setBlock(pos.x+i, pos.y + j, pos.z+k, block.Block(82,1))

#Migi Gawa no Tuuro
for i in range(23, 32):
    for j in range(-1, 0):
        for k in range(0, 16):
            mc.setBlock(pos.x+i, pos.y + j, pos.z+k, block.Block(82,1))



# Syuei san no Koya
for i in range(14, 19):
    for j in range(0, 6):
        for k in range(-16, -11):
            mc.setBlock(pos.x+i, pos.y + j, pos.z+k, block.Block(35,1))



# Itiban Hidari no Hashira

for i in range(0, 3):
    for j in range(0, 5):
        for k in range(0, 3):
            mc.setBlock(pos.x+i, pos.y + j, pos.z+k, block.Block(80,1))

pos.x = x + 6
pos.y = y
pos.z = z

pos.x += 1931
pos.y += -4
pos.z += 899

# Hidari kara Nibanme no Hashira
for i in range(0, 3):
    for j in range(0, 5):
        for k in range(0, 3):
        	mc.setBlock(pos.x+i, pos.y + j, pos.z+k, block.Block(80,1))


pos.x = x + 23
pos.y = y
pos.z = z

pos.x += 1931
pos.y += -4
pos.z += 899

# Migi kara Nibanme no Hashira
for i in range(0, 3):
    for j in range(0, 5):
        for k in range(0, 3):
            mc.setBlock(pos.x+i, pos.y + j, pos.z+k, block.Block(80,1))



pos.x = x + 29
pos.y = y
pos.z = z

pos.x += 1931
pos.y += -4
pos.z += 899

# Itiban Migi no Hashira
for i in range(0, 3):
    for j in range(0, 5):
        for k in range(0, 3):
            mc.setBlock(pos.x+i, pos.y + j, pos.z+k, block.Block(80,1))

