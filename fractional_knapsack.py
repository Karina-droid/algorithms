class Item:
    def __int__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def fractionalKnapsack(W, arr):
    arr.sort(key=lambda x: (x.profit/x.weight), reverse=True)
    value = 0.0
    for item in arr:
        #if adding item won't overflow, add it completely
        if item.weight < W:
            W -= item.weight
            value += item.profit
        #if we can't add current item, add a fraction of it
        else:
            value += W/item.weight * item.profit
            break
    return value
