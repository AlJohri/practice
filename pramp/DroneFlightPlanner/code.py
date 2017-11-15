"""
Drone Flight Planner

Question:

You are planning a drone flight.
The drone has 2 engines: a gliding engine that generates movement to the sides
and an elevation engine that generates movement up or down.
The gliding engine takes no energy, but the elevation engine uses both fuel
and self charging. To climb up, the elevation engine uses 1 energy unit per
foot. When flying down, the engine is charged 1 energy unit per foot.
Before the flight, you fill the fuel tank of the drone. Each bottle of fuel
produces 1 energy unit for the operation of the elevation engine.

Given such a drone and a route represented by an array of 3 dimensional
coordinate, what is the most efficient way calculate the minimal amount of
fuel needed to complete the route?
Explain and code the most efficient solution in terms of runtime complexity
and number of operations per coordinate

Tips:
If you don't get the simple solution, try running the basic solution on paper
and get the sense of it

To get 5 stars for Problem Solving, your peer must complete the simple
solution and explain it well. The basic solution can get your peer up to 5
stars

If your peer is having a hard time, help your peer focus by getting the
gliding engine and the x & y coordinates out of the way

Another hint: give your peer the example route array on the solution and ask
your peer to focus on solving this route first and then generalize a solution

A common solution for this question is calculating the difference between the
max & min heights on the routes. That is, of course, a wrong answer. Try to
think why

"""

zroute = [10, 0, 2, 15, 8]

def calcFuelBasic(zroute):
   energy_balance = 0
   initial_bottles = 0
   for i in range(1, len(zroute)):
      energy_balance += zroute[i-1] - zroute[i]
      if energy_balance < 0:
         initial_bottles += abs(energy_balance)
   return initial_bottles

def calcFuelSimple(zRoute):
   return max(zRoute) - zRoute[0]

print(zroute)
print(calcFuelBasic(zroute))
print(calcFuelSimple(zroute))

"""
Solution:
Since we only relate to moving up and down, we can ignore the x and y coordinates an
focus on the z coordinate.
We should come up with the amount of initial energy required to enable the flight.
Therefore, we have to make sure we can climb the biggest elevation difference.

Example route: [10, 0, 2, 15, 8]

Basic & Easy Solution
Imagine you start the flight with an empty engine, but are able to fuel the drone
while it's in the air.
Iterating over all coordinates, count how many bottles of fuel you need to add along
the route to never be on a negative balance.
This amount is the minimal amount of fuel you need to make it through the flight.

Using this on the example route, we get to a negative balance only when climbing
from 2 to 15. The negative balance on that point is -5 and we add 5 bottles to
cover for it.

function calcFuelBasic(zRoute):
   bottlesAdded = 0
   energyBalance = 0
   for i from 1 to length(zRoute)-1:
      energyBalance = energyBalance + (zRoute[i] - zRoute[i-1])
      if (energyBalance < 0):
         bottlesAdded = bottlesAdded - energyBalance
         energyBalance = 0
   return bottles

Runtime Complexity: linear O(n). Constant number of operations for each
coordinates + a constant number of operations.
# of operations: 2-4 for each coordinates + 3 general

The Elegant & Efficient Solution

This solution is based on one observation: The initial fuel amount is what
it takes the drone to climb from the start point to the highest (max)
point on the route.
Getting to any height below the start height produces energy, and going
above take at most the difference between max height and start height.
Even if we go below before climbing to the max height, by getting to the
same height as the start, our balance is zero and we then need the energy
to climb from start to max.

function calcFuelSimple(zRoute):
   maxHeight = zRoute[0]
   for i from 1 to length(zRoute)-1:
      if (zRoute[i] > maxHeight):
         maxHeight = zRoute[i]
   return maxHeight - zRoute[0]

Runtime Complexity: linear O(n). We iterate of the array once with
constant number of actions per iteration.
# of actions: 1 or 2 per iteration + 2 general

"""