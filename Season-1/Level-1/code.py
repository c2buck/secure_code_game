'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import Decimal


Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    net = Decimal("0")
    total_payable = Decimal("0")
    limit = Decimal("9999")
    for item in order.items:
        amount = Decimal(str(item.amount))
        if item.type == 'payment':
            net += amount
        elif item.type == 'product':
            if amount <= 0:
                return "invalid item amount"
            if item.quantity <= 0:
                return "invalid quantity amount"
            if item.quantity != int(item.quantity):
                return "invalid quantity amount whole number"
            total_payable = amount * item.quantity
            if total_payable >= limit:
                return "Total amount payable for an order exceeded"
            net -= amount * item.quantity
        else:
            return "Invalid item type: %s" % item.type

    if net != Decimal("0"):
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
    else:
        return "Order ID: %s - Full payment received!" % order.id