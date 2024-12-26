import math
def calculate(base,height):
    hyp=math.sqrt(base**2+height**2)
    return hyp
base,height=map(float,input().split())
result=calculate(base,height)
print(f" hypotenus:{result:.2f}")
