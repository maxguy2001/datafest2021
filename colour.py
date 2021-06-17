def plotPointColour(proportion):
    #localProportion = float(proportion.to_string(index = False))
    localProportion = proportion

    Colour = "Blue"

    # Green - Top 25% : in range max to (min + (max - min) * 0.75)
    # Yellow - 75% to 50%: (min + (max - min) * 0.75) to (min + (max - min) * 0.5)
    # Orange - 50% to 25%: (min + (max - min) * 0.5) to (min + (max - min) * 0.25)
    # Red - Bottom 25%: (min + (max - min) * 0.25) to min
    #max_v = round(post_grouped_uk_data["DAST_CAT"].max(), 6)
    #min_v = round(post_grouped_uk_data["DAST_CAT"].min(), 6)
    max_v = 2.4
    min_v = 1.2
    per75 = (min_v + ((max_v - min_v) * 0.75))
    per50 = (min_v + (max_v - min_v) * 0.5)
    per25 = (min_v + (max_v - min_v) * 0.25)
    

    if ((localProportion <= max_v) and (localProportion >= per75)):
        Colour = "Green"
    elif ((localProportion <= per75) and (localProportion >= per50)):
        Colour = "Yellow"
    elif ((localProportion <= per50) and (localProportion >= per25)):
        Colour = "Orange"
    elif ((localProportion <= per25) and (localProportion >= min_v)):
        Colour = "Red"
    else:
        print(max_v)
        print(min_v)
        print(per75)
        print(per50)
        print(per25)
        print(proportion)
        print(localProportion)
        print(type(localProportion))
        raise ValueError
    
    return Colour

print(plotPointColour(1.5))