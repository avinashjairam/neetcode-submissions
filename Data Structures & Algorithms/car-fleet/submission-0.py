class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # step 1 : combine each car's position and speed into pairs. So we treat
        # each car as (position, speed)

        pair = [(p, s) for p,s in zip(position,speed)]

        # step 2: sort the cars by position in descending order (closests to target first)
        # Because only cars behind can catch up to cars in front 
        pair.sort(reverse = True)

        # step 3: start with the frontmost car - it always forms at least one fleet
        fleets = 1

        # calculate how long this frontmost car will take to reach the target 
        prevTime = (target - pair[0][0]) / pair[0][1]

        # step 4 - move through each of the remaining cars (from the next closests to the farthest)
        for i in range(1, len(pair)):
            currCar = pair[i]

            # Compute how long the current (behind) car would take to reach the target
            currTime = (target - currCar[0]) / currCar[1]

            # if the current car takes *longer* to reach than the one ahead (prevTime)
            # that means it will not catchup before the destination -> new fleet
            if currTime > prevTime:
                fleets += 1

                # update prevTime to represent the new fleet's time to reach the target
                prevTime = currTime 

            # otherwise, if currTime <= prevTime
            # The current car will catch up before reaching the target 
            # So it merges into the fleet (formed)

        # Step 5: return the number of fleets formed
        return fleets        