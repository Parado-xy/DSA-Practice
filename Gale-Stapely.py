#!/usr/bin/python3

def stable_marriage(men_preferences, women_preferences):
    # Initialize all men and women as free
    free_men = list(men_preferences.keys())
    engaged = {}  # woman -> man
    proposals = {man: [] for man in men_preferences}

    # Invert women's preferences for faster lookup
    women_rankings = {
        w: {m: rank for rank, m in enumerate(prefs)}
        for w, prefs in women_preferences.items()
    }

    while free_men:
        m = free_men[0]  # pick the first free man
        m_prefs = men_preferences[m]

        # Propose to the highest-ranked woman not yet proposed to
        for w in m_prefs:
            # Propose to women that the man `m`  hasn't proposed to. 
            if w not in proposals[m]:
                proposals[m].append(w)
                # If w is free
                if w not in engaged:
                    engaged[w] = m
                    free_men.pop(0)  # m is no longer free
                else:
                    m_prime = engaged[w]
                    # If w prefers m over m'
                    if women_rankings[w][m] < women_rankings[w][m_prime]:
                        engaged[w] = m
                        free_men.pop(0)  # m is no longer free
                        free_men.append(m_prime)  # m' is now free
                    # Else w prefers her current engagement
                    # m remains free, so do nothing
                break  # move to next iteration (next man or proposal)

    # Return the set of engaged pairs
    return {(m, w) for w, m in engaged.items()}

# As we can see. For the woman, as the proposals come by, the man she get's 
# married to will keep increasing in rank. 
# For the man however, the women he proposes to keep getting lower and lower on his prefrence list. 

men_preferences = {
    'B': ['Y', 'X', 'Z'],    
    'A': ['X', 'Y', 'Z'],
    'C': ['X', 'Z', 'Y']
}

women_preferences = {
    'X': ['B', 'A', 'C'],
    'Y': ['A', 'B', 'C'],
    'Z': ['A', 'B', 'C']
}

matches = stable_marriage(men_preferences, women_preferences)
print(matches)
