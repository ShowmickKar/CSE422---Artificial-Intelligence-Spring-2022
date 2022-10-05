import math
import random


def search(points):
    highest_achievable_points = alpha_beta_pruning(
        points, 0, -math.inf, math.inf, 0, True)
    return highest_achievable_points


def alpha_beta_pruning(points, depth, alpha, beta, index, maximizer):
    if depth == 3:
        return points[index]
    if maximizer:
        max_value = -math.inf
        for i in range(2):
            evaluation = alpha_beta_pruning(points, depth + 1, alpha,
                                            beta, 2 * index + i, False)
            max_value = max(max_value, evaluation)
            alpha = max(alpha, max_value)
            if beta <= alpha:
                break
        return max_value
    else:
        min_value = math.inf
        for i in range(2):
            evaluation = alpha_beta_pruning(points, depth + 1, alpha,
                                            beta, 2 * index + i, True)
            min_value = min(min_value, evaluation)
            beta = min(beta, min_value)
            if beta <= alpha:
                break
        return min_value


# Driver Code
if __name__ == '__main__':
    id = input("Enter your student id: ")
    id = id.replace('0', '8')
    min_bound = int(id[4])
    shuffle = int(id[3])
    max_bound = id[len(id)-2:]
    to_win = int(max_bound[-1] + max_bound[-2])
    max_bound = math.ceil(to_win * 1.5)
    points = [random.randint(min_bound, max_bound) for _ in range(8)]

    print("--- Output for Task 1 ---")
    print("Generated 8 random points between the minimum and maximum point")
    print(f"limits: {points}")
    print(f"Total Points to win: {to_win}")
    achieved_points = search(points)
    print(
        f"Achieved point by applying alpha-beta pruning = {achieved_points}")
    winner = "Optimus Prime" if achieved_points >= to_win else "Megatron"
    print(f"The winner is {winner}")

    shuffled_numbers = []
    win_count = 0
    for i in range(shuffle):
        new_random_point = random.choice(points)
        if achieved_points >= new_random_point:
            win_count += 1
        shuffled_numbers.append(new_random_point)
    max_number_from_shuffle = max(shuffled_numbers)

    print("--- Output for Task 2 ---")
    print("After the Shuffle")
    print(f"List of all points values from each shuffle: {shuffled_numbers}")
    print(f"The maximum value of all shuffles: {max_number_from_shuffle}")
    print(f"Won {win_count} times out of {shuffle} shuffles")
