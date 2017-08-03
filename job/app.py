import random, time
from socket import gethostname

max_iter = 10
for i in range(0, max_iter):
    rdm = random.random() * 5
    msg = "Iteration %s/%s on %s. Waiting %s before continuing" % (i+1, max_iter, gethostname(), rdm)
    print(msg)
    time.sleep(rdm)
