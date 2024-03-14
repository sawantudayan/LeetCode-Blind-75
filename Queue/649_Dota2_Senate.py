def predictPartyVictory(self, senate: str) -> str:
    """
    This function predicts the victory of either the Radiant or Dire party in a game based on the current state of the senate.

    :param senate: A string representing the current state of the senate. The characters 'R' and 'D' represent a member of the Radiant and Dire party respectively.
    :return: A string 'Radiant' if the Radiant party will win, and 'Dire' if the Dire party will win.
    
    Time Complexity : O(n), where n is the length os the string 'senate'
    Space Complexity : O(n), since the function creates 2 lists that can grow upto a length of n
    """
    n = len(senate)
    r_arr = [i for i in range(len(senate)) if senate[i] == 'R']
    d_arr = [j for j in range(len(senate)) if senate[j] == 'D']
    
    while r_arr and d_arr:
        r = r_arr.pop()
        d = d_arr.pop()
        if r<d:
            r_arr.append(n+r)
        else:
            d_arr.append(n+d)
    return 'Radiant' if r_arr else 'Dire'