#> realtime:get
tag @s add own
function realtime:next
tellraw @s [{"text": "現在時刻は"},{"nbt":"now.hour","storage": "realtime:"},{"text": "時"},{"nbt":"now.minute","storage": "realtime:"},{"text": "分"},{"nbt":"now.second","storage": "realtime:"},{"text": "秒"},{"text": "です。"}]

