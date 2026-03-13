# There are n people lined up to buy tickets, with person 0 at the front and person n - 1 at the back. 
# You are given a 0-indexed array tickets of length n, where tickets[i] is the number of tickets person i wants to purchase.

# Each ticket purchase takes exactly 1 second. Each person can only buy one ticket at a time. 
# If, after buying a ticket, a person still needs more tickets, they immediately move to the end of the line. 
# If a person no longer needs any tickets, they leave the line entirely.

# You need to calculate how many seconds it takes for the person who starts at position k (0-indexed) 
# to finish buying all of their tickets.

def timeRequiredToBuy(tickets, k):
    time = 0
    for i in range(len(tickets)):
        if i <= k:
            time += min(tickets[i], tickets[k])
        else:
            time += min(tickets[i], tickets[k] - 1)
    return time