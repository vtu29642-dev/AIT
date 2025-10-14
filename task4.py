def alphabeta_pruning(depth,nodeIndex,maximizingPlayer,values,alpha,beta):
    if depth==0 or nodeIndex>=len(values):
        return values[nodeIndex]
    if maximizingPlayer:
        max_eval=float('-inf')
        for i in range(2):
            eval=alphabeta_pruning(depth-1,nodeIndex*2+i,False,values,alpha,beta)
            max_eval=max(max_eval,eval)
            alpha=max(alpha,eval)
            if beta<=alpha:
                break
        return max_eval
    else:
        min_eval=float('inf')
        for i in range(2):
            eval=alphabeta_pruning(depth-1,nodeIndex*2+i,True,values,alpha,beta)
            min_eval=min(min_eval,eval)
            beta=min(beta,eval)
            if beta<=alpha:
                break
        return min_eval
if __name__=="__main__":
    values=[3,5,6,9,1,2,0,-1]
    depth=3
    alpha=float('-inf')
    beta=float('inf')
    optimal_value=alphabeta_pruning(depth,0,True,values,alpha,beta)
    print(f"The optimal value is: {optimal_value}")
