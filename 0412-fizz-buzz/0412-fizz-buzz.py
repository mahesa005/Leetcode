class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        List_int = list(range(1, n+1))
        for i in range(n):
            if List_int[i] % 3 == 0 and List_int[i] % 5 == 0:
                List_int[i] = "FizzBuzz"
            elif List_int[i] % 3 == 0:
                List_int[i] = "Fizz"
            elif List_int[i] % 5 == 0:
                List_int[i] = "Buzz"
        List_str = list(map(str, List_int))
        return List_str
            
        