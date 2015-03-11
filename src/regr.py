# regression example in python
# take data from stdin data points separted by space
import numpy as np
from sklearn.linear_model import LinearRegression 

line = raw_input()
F, N = map(int, line.split())

trnData = []
tstData = []
for _ in range(N):
  line = raw_input()
  line = map(float, line.split())
  trnData.append(line)

tstN = int(raw_input())
for _ in range(tstN):
  line = raw_input()
  line = map(float, line.split())
  tstData.append(line)

#Data checks

trnData = np.array(trnData)
tstData = np.array(tstData)
trnX = trnData[:,0:F]
trnY = trnData[:,F]

model = LinearRegression()
model.fit(trnX, trnY)

print model.predict(tstData)
