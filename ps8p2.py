def fib(n):
  fib(20)
n = 20
fn = 1
sn = 1
print(fn)
print(sn)
for tn in range (2, n):
  tn = fn + sn
  fn = sn
  sn = tn
  print(tn)
  