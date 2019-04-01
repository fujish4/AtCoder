c11, c12, c13 = map(int, input().split())
c21, c22, c23 = map(int, input().split())
c31, c32, c33 = map(int, input().split())
 
def isCorrect():
    if not (c11 - c21 == c12 - c22 == c13 - c23):
        return "No"
    if not (c11 - c31 == c12 - c32 == c13 - c33):
        return "No"
    if not (c11 - c12 == c21 - c22 == c31 - c32):
        return "No"
    if not (c11 - c13 == c21 - c23 == c31 - c33):
        return "No"
    return "Yes"
 
print(isCorrect())