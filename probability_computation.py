'''
Get solution from the output of getState function
For 'What is the probability that the tourist is ever east of East 1st Avenue but ends up west of West 1st Avenue in 10 moves?'
Compute the number of states that never been east of East 1st but ends up west of West 1st, and 
the number of states that ends west of West 1st. 
The difference between this two divided by totoal states of of the 10th moves is the solution.
'''
entry = (0, 0)
walks = 1
distParameter = 0
def ManhattanDist(point):
	return abs(point[0] - entry[0]) + abs(point[1] - entry[1])

def distWithin(point):
	return abs(point[0] - entry[0]) + abs(point[1] - entry[1]) < distParameter

def eastOne(point):
	return point[0] < 2

def blockAway(point):
	return ManhattanDist(point) < distParameter

# To save computating cost, merge the stated of each walk by giving stateCount as weights of stateS
def getState(entryPoint, stepSize):
	stateSpace = {0: {entryPoint: 1}}
	for i in range(0, stepSize):
		stateSpace[i + 1] = {}
		for state, stateCount in stateSpace[i].iteritems():
			newState = (state[0] - 1, state[1])
			if newState in stateSpace[i + 1]:
				stateSpace[i + 1][newState] += stateCount
			else:
				stateSpace[i + 1][newState] = stateCount

			newState = (state[0] + 1, state[1])
			if newState in stateSpace[i + 1]:
				stateSpace[i + 1][newState] += stateCount
			else:
				stateSpace[i + 1][newState] = stateCount

			newState = (state[0], state[1] - 1)
			if newState in stateSpace[i + 1]:
				stateSpace[i + 1][newState] += stateCount
			else:
				stateSpace[i + 1][newState] = stateCount

			newState = (state[0], state[1] + 1)
			if newState in stateSpace[i + 1]:
				stateSpace[i + 1][newState] += stateCount
			else:
				stateSpace[i + 1][newState] = stateCount
	return stateSpace

def getStateConditioned(entryPoint, stepSize, conditionFunction):
	stateSpace = {0: {entryPoint: 1}}
	for i in range(0, stepSize):
		stateSpace[i + 1] = {}
		for state, stateCount in stateSpace[i].iteritems():
			newState = (state[0] - 1, state[1])
			if newState in stateSpace[i + 1] and conditionFunction(newState):
				stateSpace[i + 1][newState] += stateCount
			elif conditionFunction(newState):
				stateSpace[i + 1][newState] = stateCount

			newState = (state[0] + 1, state[1])
			if newState in stateSpace[i + 1] and conditionFunction(newState):
				stateSpace[i + 1][newState] += stateCount
			elif conditionFunction(newState):
				stateSpace[i + 1][newState] = stateCount

			newState = (state[0], state[1] - 1)
			if newState in stateSpace[i + 1] and conditionFunction(newState):
				stateSpace[i + 1][newState] += stateCount
			elif conditionFunction(newState):
				stateSpace[i + 1][newState] = stateCount

			newState = (state[0], state[1] + 1)
			if newState in stateSpace[i + 1] and conditionFunction(newState):
				stateSpace[i + 1][newState] += stateCount
			elif conditionFunction(newState):
				stateSpace[i + 1][newState] = stateCount
	return stateSpace

def countState(stateSpace, index):
	stateSubSpace = stateSpace[index]
	count = 0
	for stateCount in stateSubSpace.itervalues():
		count += stateCount
	return count

def getAverage(rate, conditionFunction):
	stateSpace = {0: {entry: 1}}
	passCounter = 0
	StepCounter = 0
	for i in range(0, 400):
		stateSpace[i + 1] = {}
		for state, stateCount in stateSpace[i].iteritems():
			newState = (state[0] - 1, state[1])
			if newState in stateSpace[i + 1] and conditionFunction(newState):
				stateSpace[i + 1][newState] += stateCount
			elif conditionFunction(newState):
				stateSpace[i + 1][newState] = stateCount

			newState = (state[0] + 1, state[1])
			if newState in stateSpace[i + 1] and conditionFunction(newState):
				stateSpace[i + 1][newState] += stateCount
			elif conditionFunction(newState):
				stateSpace[i + 1][newState] = stateCount

			newState = (state[0], state[1] - 1)
			if newState in stateSpace[i + 1] and conditionFunction(newState):
				stateSpace[i + 1][newState] += stateCount
			elif conditionFunction(newState):
				stateSpace[i + 1][newState] = stateCount

			newState = (state[0], state[1] + 1)
			if newState in stateSpace[i + 1] and conditionFunction(newState):
				stateSpace[i + 1][newState] += stateCount
			elif conditionFunction(newState):
				stateSpace[i + 1][newState] = stateCount
		passNum = countState(stateSpace, i) * 4 - countState(stateSpace, i + 1)
		StepCounter += passNum
		passCounter += (i + 1) * passNum
	return passCounter / float(StepCounter)	

# Compute probability by counting states, question1
walks = 10
state_10 = getState(entry, walks)
totalState_10 = countState(state_10, walks)
count_3 = 0
#print totalState_10
for state, stateCount in state_10[walks].iteritems():
	if ManhattanDist(state) >= 3:
		count_3 += stateCount
#print count_3
print '1. The probability that the tourist is at least 3 city blocks away after 10 moves is'
print count_3 / float(totalState_10)

# Compute probability by counting states, question2
walks = 60
state_60 = getState(entry, walks)
totalState_60 = countState(state_60, walks)
count_10 = 0
for state, stateCount in state_60[walks].iteritems():
	if ManhattanDist(state) >= 10:
		count_10 += stateCount
print '2. The probability that the tourist is at least 10 city blocks away after 60 moves is'
print count_10 / float(totalState_60)

# Use conditioned state counting function, question 3
walks = 10
distParameter = 5
state_10_5 = getStateConditioned(entry, walks, distWithin)
count_5 = 0
for state, stateCount in state_10_5[walks].iteritems():
	count_5 += stateCount
print '3. The probability that the tourist is ever at least 5 city blocks away within 10 moves is'
print 1 - count_5 / float(totalState_10)

# Use conditioned state counting function, question 4
walks = 60
distParameter = 10
state_60_10 = getStateConditioned(entry, walks, distWithin)
count_60_10 = 0
for state, stateCount in state_60_10[walks].iteritems():
	count_60_10 += stateCount
print '4. The probability that the tourist is ever at least 10 city blocks away within 60 moves is'
print 1 - count_60_10 / float(totalState_60)

# Use conditioned state counting function, question 5
walks = 10
state_10_e = getStateConditioned(entry, walks, eastOne)
count_10_e = 0
for state, stateCount in state_10_e[walks].iteritems():
	if state[0] < -1:
		count_10_e += stateCount
print count_10_e
count_10_w = 0
for state, stateCount in state_10[walks].iteritems():
	if state[0] < -1:
		count_10_w += stateCount
print '5. The probability that the tourist is ever east of East 1st but ends up west of West 1st in 10 moves is'
print (count_10_w - count_10_e) / float(totalState_10)

# Use conditioned state counting function, question 6
walks = 30
state_30_e = getStateConditioned(entry, walks, eastOne)
state_30 = getState(entry, walks)
totalState_30 = countState(state_30, walks)
count_30_e = 0
for state, stateCount in state_30_e[walks].iteritems():
	if state[0] < -1:
		count_30_e += stateCount
count_30_w = 0
for state, stateCount in state_30[walks].iteritems():
	if state[0] < -1:
		count_30_w += stateCount
print '6. The probability that the tourist is ever east of East 1st but ends up west of West 1st in 30 moves is'
print (count_30_w - count_30_e) / float(totalState_30)