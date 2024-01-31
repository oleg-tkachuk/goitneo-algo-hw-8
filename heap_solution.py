import heapq


def min_cost_to_connect_cables_with_details(cable_lengths):
    heapq.heapify(cable_lengths)

    total_cost = 0
    steps = []  # Store details of each merge step

    while len(cable_lengths) > 1:
        # Take the two smallest cables
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)

        # Cable combining and costing
        cost = first + second
        total_cost += cost

        # Add merge details to the list of steps
        steps.append(f"Combined cables of length {first} and {second} meters, costs: {cost}")

        # Adding a new cable to the heap
        heapq.heappush(cable_lengths, cost)

    return total_cost, steps


def main():
    print(f"Homework 8 | Find the order of cables combining that minimizes the total cost")

    cable_lengths = [5, 25, 4, 42, 2, 8, 7, 10, 37]
    print(f"Homework 8 | Length of existing cables: {cable_lengths}")

    # Calculations
    total_cost, steps = min_cost_to_connect_cables_with_details(cable_lengths)
    print(f"Homework 8 | Steps to connect the cables: ")
    for i, item in enumerate(steps, start=1):
        print(11 * " " + f"{i}. {item}")
    print(f"Homework 8 | The minimum total costs for connecting cables are: {total_cost}")


if __name__ == "__main__":
    main()
