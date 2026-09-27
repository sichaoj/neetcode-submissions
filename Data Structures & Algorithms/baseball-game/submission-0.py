class Solution:
    def calPoints(self, operations: List[str]) -> int:
        array = []
        for i in range(len(operations)): 
            if operations[i] not in ("+","C","D"):
                operations[i] = int(operations[i])
                array.append(operations[i])
            elif operations[i] == "+":
                if len(array) < 2:
                    array = array 
                else:
                    j = len(array)
                    array.append( array[j-1] + array[j-2] )
            elif operations[i] == "C":
                if len(array) == 0:
                    array = array
                else: 
                    array.pop()
            elif operations[i] == "D": 
                if len(array) == 0:
                    array = array
                else: 
                    array.append(2 * array[-1])

        final = sum(array)

        return final 
