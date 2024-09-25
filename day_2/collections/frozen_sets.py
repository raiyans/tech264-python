"""Objective

Understand the concept and usage of immutable sets (frozen sets).

The task

Create a frozen set named frozen_set containing elements "hello", "world".
Try to add "!" to frozen_set. What happens?
Create a normal set named normal_set containing elements "let's", "learn".
Try to add frozen_set to normal_set. Why does it work? Explain.
Print normal_set.
Run your script half a dozen times. What do you notice about where frozen_set is added to normal_set? Hint: Look at the order of the items.
What makes a frozen set different to a normal set? Explain. """

frozen_set = frozenset(["hello", "world"])
#cant add to frozen sett
print(frozen_set)
normal_set = {"let's", "learn"}
normal_set.add(frozen_set)
print(normal_set)
#frozenset is place randomly
#frozen set has immutability