def pipe_fix(pipe):
   
    a = 0
    
    for valor in range(pipe[0], pipe[-1]):
        
        if pipe[a+1] != pipe[a]+1:
            pipe.insert((a+1), pipe[a]+1) 
        
        a = a + 1

    return pipe
