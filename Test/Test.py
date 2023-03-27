import random
color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
color = str(color)
color = color.replace("['",'')
color = color.replace("']",'')
print(type(color),color)