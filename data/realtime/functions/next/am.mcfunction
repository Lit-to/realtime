#> realtime:next/am
summon armor_stand ~ ~ ~ {Tags:["r_time"]}
item replace entity @e[type=armor_stand,tag=r_time] weapon.mainhand with magma_cream
data modify entity @e[type=armor_stand,tag=r_time,limit=1] HandItems[0].tag.Time set from block 0 -64 0 LastOutput 
execute as @e[type=minecraft:armor_stand,sort=nearest,limit=1] run function realtime:next/get



kill @e[type=armor_stand,tag=r_time]

