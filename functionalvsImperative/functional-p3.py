#  q_func.py
#
SIZE=8


def checkPlacement (partial, col, spread=1) :
  if not partial : return True
  else :
    if int(partial[-1]) in (col,col-spread,col+spread):
      return False
    else :
      return checkPlacement(partial[:-1], col, spread+1)

def printBoard(partial) :
  if partial :
    col = int(partial[0])     ### taking a digit
    lin = ". "*(col-1) + "Q " + \
          ". "*(SIZE-col)          #### Print ## a line 
    print(lin)
    printBoard(partial[1:])  ### recursive call


def expandSolution(partial) :
  if len(partial) >= SIZE :
    print(partial) # a solution
    return []
  else :
    pairs = tuple(zip([partial]*SIZE, range(1,SIZE+1)))
    pairs = list(filter(lambda p: checkPlacement(p[0],p[1]), pairs))
    pairs = map(lambda p: "%s%d"%p, pairs)
    return list(pairs)


def findSolutions(partials=[""]) :
  if partials :
    partials = map(expandSolution, partials)
    partials = functools.reduce(lambda x,y: x+y, partials)
    findSolutions(partials)
  return

  
if __name__ == "__main__" :
  import time
  import functools
  start = time.time()
  findSolutions()
  finish = time.time()
  print("Done. Took %.4f" % (finish-start))
