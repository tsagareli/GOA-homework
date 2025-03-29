# (True or (True and True)) and (False or False)
# (True and True) -> True, (False or False) -> False
# (True or True) -> True, True and False -> False
print((True or (True and True)) and (False or False))  # False

# (True and False) or (False and True)
# True and False -> False, False and True -> False
# False or False -> False
print((True and False) or (False and True))  # False

# (False and True) or (False and False)
# False and True -> False, False and False -> False
# False or False -> False
print((False and True) or (False and False))  # False

# (True or False) and (False or True)
# True or False -> True, False or True -> True
# True and True -> True
print((True or False) and (False or True))  # True

# (False and True) or (True and False)
# False and True -> False, True and False -> False
# False or False -> False
print((False and True) or (True and False))  # False

# (True or False) and (True and True)
# True or False -> True, True and True -> True
# True and True -> True
print((True or False) and (True and True))  # True