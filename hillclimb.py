def hillclimb(init_function,move_operator,objective_function,max_evaluations):

    best_route=init_function
    best_score=objective_function(best_route)
    
    num_evaluations=1
    
    while num_evaluations < max_evaluations:
        # examine moves around our current position
        move_made=False
        for next in move_operator(best_route):
            if num_evaluations >= max_evaluations:
                break
            
            # see if this move is better than the current
            next_score=objective_function(next)
            num_evaluations+=1
            if next_score > best_score:
                best_route=next
                best_score=next_score
                move_made=True
                break         # depth first search
            
        if not move_made:
            break             # at a local maximum
    
    return (num_evaluations,best_score,best_route)

def hillclimb_and_restart(init_function,move_operator,objective_function,max_evaluations):

    # repeatedly hillclimb until max_evaluations is reached
    
    best=None
    best_score=0
    
    num_evaluations=0
    while num_evaluations < max_evaluations:
        remaining_evaluations=max_evaluations-num_evaluations
        
        evaluated,score,found=hillclimb(init_function,move_operator,objective_function,remaining_evaluations)
        
        num_evaluations+=evaluated
        if score > best_score or best is None:
            best_score=score
            best=found
        
    return (num_evaluations,best_score,best)
