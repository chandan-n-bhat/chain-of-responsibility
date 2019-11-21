# Consider a sweet nuclear family with Father, Mother, Son and a Daughter
# Lets say on the occasion of Deepavali the childrens' grandmother sent out gifts for each one in the family.
# She forgot to mention which gift is for whom instead asks everyone which they need.
# This can be modelled using the Chain of responsibilty design pattern
# Lets say the gifts were Watch for the father,Saree for the Mother, Laptop for the Son and Smartphone for the Daughter.

# Author : Chandan N Bhat
# Design Patter : Chain of Responsibilty

from __future__ import annotations
from abc import ABC, abstractmethod


class Handler(ABC):

    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass


class AbstractHandler(Handler):

    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)

        return None

# Concrete Handlers either handle a request or pass it to the next handler in the chain.

class FatherHandler(AbstractHandler):
    def handle(self, request):
        if request == "Watch":
            return f"Father: I'll keep the {request}.Thank you Mother-in-law!"
        else:
            return super().handle(request)


class MotherHandler(AbstractHandler):
    def handle(self, request: Any):
        if request == "Saree":
            return f"Mother: I Love Sarees.Thank you mom for the {request}."
        else:
            return super().handle(request)


class SonHandler(AbstractHandler):
    def handle(self, request):
        if request == "Laptop":
            return f"Son: Love you Grandma for the {request} :)"
        else:
            return super().handle(request)

class DaughterHandler(AbstractHandler):
    def handle(self, request):
        if request == "Smartphone":
            return f"Daughter: Love you Grandma for the {request} :)"
        else:
            return super().handle(request)


def grandma(handler):
    
    for gift in ["Saree", "Watch", "Laptop","Smartphone","Book"]:
        print(f"\nGrandma: Who wants a {gift}?")
        result = handler.handle(gift)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {gift} was left untouched.", end="")


if __name__ == "__main__":

    father = FatherHandler()
    mother = MotherHandler()
    son = SonHandler()
    daughter = DaughterHandler()

    father.set_next(mother).set_next(son).set_next(daughter)

    print("The Gifts sent by Grandma are : {}".format(["Saree", "Watch", "Laptop","Smartphone","Book"]))

    print("Case 1:")
    print("\tChain: Father -> Mother -> Son -> Daughter")
    grandma(father)
    print("\n")

    print("Case 2:")
    print("\tSubchain: Son -> Daughter")
    grandma(son)
    print("\n")

    print("Unfortunately,In both cases the Book wasn't taken by anyone :(.\n")
    print("Everyone are happy for Grandma for sending them gifts for Deepavali!")