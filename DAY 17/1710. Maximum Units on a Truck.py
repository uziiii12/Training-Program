class Solution:
    def maximumUnits(self, boxTypes, truckSize):
    # boxTypes[i] = [number of boxes, units per box]

        ans = 0

        while truckSize > 0 and len(boxTypes) > 0:

            max_unit = 0
            index = 0

            i = 0

            while i < len(boxTypes):
                if boxTypes[i][1] > max_unit:
                    max_unit = boxTypes[i][1]
                    index = i

                i += 1

            boxes = boxTypes[index][0]

            take = min(boxes, truckSize)

            ans += take * max_unit

            truckSize -= take

            boxTypes.pop(index)

        return ans