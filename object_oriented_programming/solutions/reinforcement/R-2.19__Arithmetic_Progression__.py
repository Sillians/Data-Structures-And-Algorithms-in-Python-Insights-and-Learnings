# from object_oriented_programming.code_fragments.arithmetic_progression import ArithmeticProgression
#
# ap = ArithmeticProgression(128, 0)
# ap.make_progression(10)

stop = 2**63
start=0
step=128
num = max(0, ((stop-start+step-1)//step))
print(num)