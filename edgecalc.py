#calculates negative american odds with user calculated probabilty
def negativeodd(odds, prob):
    ip = (-1 * odds) / ((-1 * odds) + 100)
    odds = odds * -1
    edge = (((odds + 100) * prob) - odds) / odds
    return ip, edge

#calculates positive american odds with user calculated probabilty
def positiveodd(odds, prob):
    ip = 100 / (odds + 100)
    edge = (((odds + 100) * odds) - 100) / 100
    return ip, edge

#logic needs improvment
def oddcalc(odd1, odd2, prob):
    if odd1 == odd2:
        if odd1 < 0:
            ip, edge = negativeodd(odd1, prob)
        else:
            ip, edge = positiveodd(odd1, prob)
        return ((ip+ip)-1)*100, ip, edge
    else:
        if odd1 < 0:
            ip2, edge = negativeodd(odd2, prob)
            ip, edge = negativeodd(odd1, prob)
        elif odd1>0:
            ip2, edge = positiveodd(odd2, prob)
            ip, edge = positiveodd(odd1, prob)
        elif odd2<0:
            ip2, edge = negativeodd(odd2, prob)
            ip, edge = negativeodd(odd1, prob)
        return ((ip+ip2-1)*100), ip, edge

#take in american odds and return decimal odds
def decimalOdds(odd1):
    if odd1 > 0:
        decimal = (odd1 / 100) + 1
        return decimal
    else:
        decimal = (100 / (odd1*-1)) + 1
        return decimal
#take in decimal odds and return american odds
def americanOdds(odds1):
    if odds1 >= 2.00:
        american = (odds1 -1) * 100
        return american
    else:
        american = (-100) / (odds1 -1)
        return american
def main(odd1,odd2, prob):
    houseedge, ip, edge = oddcalc(odd1, odd2, prob)
    return ip, edge, houseedge
