N = input()
dictionary = {}
word_idx = {}
for i in range(N):
    line = raw_input()
    sp = line.split(": ")
    word = sp[0]
    defn = sp[1].split(" ")
    dictionary[word] = defn
    word_idx[word] = i
#print dictionary

graph = {} #adj-list graph of word dependencies
for i in range(N):
    graph[i] = []
for word in dictionary:
    idx = word_idx[word]
    for dword in dictionary[word]:
        toidx = word_idx[dword]
        graph[idx].append(toidx)

#print graph


index = 0

components = []
S = []
v_index = {}
v_lowlink = {}
v_onStack = {}
def strongConnect(v):
    global index
    global components
    global S
    global v_index
    global v_lowlink
    global v_onStack

    v_index[v] = index
    v_lowlink[v] = index
    index += 1
    S.append(v)
    v_onStack[v] = True

    # for edges of V
    for w in graph[v]:
        if w not in v_index:
            strongConnect(w)
            v_lowlink[v] = min(v_lowlink[v], v_lowlink[w])
        elif v_onStack[w]:
            v_lowlink[v] = min(v_lowlink[v], v_lowlink[w])

    if v_lowlink[v] == v_index[v]:
        component = []
        while True:
            w = S.pop()
            v_onStack[w] = False
            component.append(w)
            if w==v:
                break
        components.append(component)
def SCC(graph):
    global index
    global components
    global S
    global v_index
    global v_lowlink
    global v_onStack

    index = 0
    components = []
    S = []
    v_index = {}
    v_lowlink = {}
    v_onStack = {}
    for v in graph:
        if v not in v_index:
            strongConnect(v)
    return components


comps = SCC(graph)
#print comps
newnodemap = {}
for idx in range(len(comps)):
    comp = comps[idx]
    for node in comp:
        newnodemap[node] = idx

newgraph = {}

for idx in range(len(comps)):
    comp = comps[idx]
    outgoing = set([])
    for node in comp:
        nodeout = graph[node]
        newnodeout = set([])
        for no in nodeout:
            newnodeout.add(newnodemap[no])
        outgoing = outgoing.union(newnodeout)
    outgoing.discard(idx)
    newgraph[idx] = list(outgoing)
#print newgraph
# count number of nodes with no incoming edges

ans = 0
for node in newgraph:
    if len(newgraph[node])==0:
        ans += 1

print ans
