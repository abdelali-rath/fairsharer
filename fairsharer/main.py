def fair_sharer(values, num_iterations, share=0.1):

    """Runs num_iterations.
    In each iteration the highest value in values gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neightbor of the rightmost field.

    Examples:
    fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
    fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]
    
    Args
    values:
        1D array of values (list or numpy array)
    num_iteration:
        Integer to set the number of iterations
    """

    values = list(values)
    n = len(values)

    for _ in range(num_iterations):

        if len(set(values)) == 1:
            break

        # highest values position
        max_index = values.index(max(values))
        max_value = values[max_index]
        
        # share amount
        share_amount = int(max_value * share)

        # checking neighbours
        left_index = max_index - 1 if max_index > 0 else n - 1
        right_index = max_index + 1 if max_index < n - 1 else 0

        values[max_index] -= 2 * share_amount
        values[left_index] += share_amount
        values[right_index] += share_amount

    return values


print("fair share [0, 1000, 800, 0], 1 :")
print(fair_sharer([0, 1000, 800, 0], 1)) # --> [100, 800, 900, 0]
print("\n")
print("fair share [0, 1000, 800, 0], 2 :")
print(fair_sharer([0, 1000, 800, 0], 2)) # --> [100, 890, 720, 90]
print("\n")

# random
print("fair share [230, 85, 39, 105], 1 :")
print(fair_sharer([230, 85, 39, 105], 1)) # --> [184, 108, 39, 128]