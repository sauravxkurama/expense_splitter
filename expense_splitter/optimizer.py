# optimizer.py

import heapq

def minimize_transactions(balances):
    max_heap = []
    min_heap = []

    for person, balance in balances.items():
        if abs(balance) < 0.01:
            continue
        if balance > 0:
            heapq.heappush(max_heap, (-balance, person))  # max heap using -ve
        else:
            heapq.heappush(min_heap, (balance, person))   # min heap

    transactions = []

    while max_heap and min_heap:
        credit = heapq.heappop(max_heap)
        debit = heapq.heappop(min_heap)

        settled_amount = min(-credit[0], -debit[0])
        transactions.append((debit[1], credit[1], settled_amount))

        remaining_credit = -credit[0] - settled_amount
        remaining_debit = -debit[0] - settled_amount

        if remaining_credit > 0:
            heapq.heappush(max_heap, (-remaining_credit, credit[1]))
        if remaining_debit > 0:
            heapq.heappush(min_heap, (-remaining_debit, debit[1]))

    return transactions
