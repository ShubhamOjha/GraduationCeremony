class GraduationCeremony:
    def __init__(self, n, m=4):
        """
        Initialize the GraduationCeremony class.

        :param n: Number of academic days.
        :param m: Cannot miss m or more classes consecutively.
        """
        if n < m or n < 0 or m < 0:
            raise ValueError("Invalid Inputs: n and m must be non-negative and n >= m")

        self.n = n
        self.m = m

    def solve(self):
        """
        Solve the problem using dynamic programming with space optimization.
        
        :return: A string in the format "{x2}/{x1}" representing the fraction of ways to miss the last day.
        """
        n, m = self.n, self.m
        dp = [1] * (m + 1)
        dp[m] = 0

        for i in range(1, n + 1):
            temp = [0] * (m + 1)
            for j in range(m - 1, -1, -1):
                temp[j] = dp[0] + dp[j + 1]

            temp, dp = dp, temp

        x1 = dp[0]  # Total number of valid ways to attend classes
        x2 = temp[1]  # Total number of ways to miss the last day

        return f"{x2}/{x1}"

    def run(self):
        """
        Run the solve method and print the result.
        """
        result = self.solve()
        print(result)

if __name__ == "__main__":
    input_value = int(input())
    obj = GraduationCeremony(input_value)
    obj.run()
