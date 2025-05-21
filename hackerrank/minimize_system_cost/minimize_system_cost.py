"""
2. Code Question 2

Amazon Web Services provides scalable cloud computing services. An AWS user has designed architecture that uses
vertical scaling where computers are serially connected with one another.

The strength of the machines is represented by an array machines, where the iᵗʰ element of the array represents the
strength of the iᵗʰ machine. The cost of connecting a machine at index i to a machine at index i + 1 is defined as
|machines[i+1] - machines[i]|. In order to reduce some costs, the user has decided to remove some machines
from the system. To avoid a lot of reconnections, the user decides to remove any k consecutive machines from the
system such that the total cost of the remaining system is minimized.

Given a positive integer array machines, and an integer k, remove exactly k consecutive machines from the system
such that the total sum of differences of the consecutive machine strengths is minimized.

Example:
machines = [3, 9, 4, 2, 16]
k = 3

Current cost: |9-3| + |4-9| + |2-4| + |16-2| = 6 + 5 + 2 + 14 = 27

Options:
- Remove [3, 9, 4] ⇒ [2, 16] → cost = |16-2| = 14
- Remove [9, 4, 2] ⇒ [3, 16] → cost = |3-16| = 13
- Remove [4, 2, 16] ⇒ [3, 9] → cost = |3-9| = 6

Return: 6

Constraints:
1 ≤ k < n ≤ 2*10⁵
1 ≤ machines[i] ≤ 10⁹
"""


def minimizeSystemCost(k, machines):
    print(f"Machines: {machines}, k: {k}")

    # Build pairwise costs between adjacent machines
    machine_costs = []
    for i in range(len(machines) - 1):
        print(f"i: {i}")
        machine_costs.append(abs(machines[i] - machines[i + 1]))
    # originally this line was incorrectly adding a dummy cost that shouldn't exist
    # machine_costs.append(0)  ← no need for this, would cause indexing mismatches

    print("machines")
    print(machines)
    print("Machine costs")
    print(machine_costs)

    min_cost = None
    for i in range(len(machines) - k + 1):
        # remove k consecutive machines starting at index i
        non_removed_machines = machines[:i] + machines[i + k :]

        # here's the main logic issue:
        # machine_costs is built from pairwise diffs between consecutive items.
        # If we remove k items starting at i, we must also remove costs:
        #  - from (i-1) if i > 0  (the edge before the cut)
        #  - through (i + k - 2) (the last edge inside the cut)
        # what should remain is cost[:i-1] + [|A-B|] + cost[i+k:]

        # current (incorrect) version:
        # non_removed_costs = machine_costs[:max(i-1,0)] + machine_costs[i + k - 1:]

        # correct version:
        non_removed_costs = []
        if i > 0:
            non_removed_costs.append(
                abs(machines[i - 1] - machines[i + k])
            )  # bridge over the gap
        for j in range(i - 1):
            non_removed_costs.append(abs(machines[j] - machines[j + 1]))
        for j in range(i + k, len(machines) - 1):
            non_removed_costs.append(abs(machines[j] - machines[j + 1]))

        print(f"i: {i}, non_removed_machines: {non_removed_machines}")
        print(f"non_removed_costs: {non_removed_costs}")

        if min_cost is None:
            min_cost = sum(non_removed_costs)
        else:
            min_cost = min(min_cost, sum(non_removed_costs))

    return min_cost
