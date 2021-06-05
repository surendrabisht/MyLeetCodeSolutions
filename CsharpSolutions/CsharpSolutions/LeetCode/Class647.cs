using System;
namespace CsharpSolutions.LeetCode
{
    public class Class647 : IAbstractSolution
    {
        public void Main()
        {
            //test-Cases
            Console.WriteLine(CountSubstrings("aaaaa"));
        }

        public int CountSubstrings(string s)
        {
            int length = s.Length;
            int[,] palindromes = new int[length, length];

            int countOfPalindromes = s.Length;
            for (int i = 0; i < s.Length; i++)
            {
                palindromes[i, i] = 1;
            }
            for (int i = length - 2; i >= 0; i--)
            {
                for (int j = i + 1; j < s.Length; j++)
                {
                    if (s[i] == s[j])
                    {
                        if (j - i == 1)
                        {
                            palindromes[i, j] = 1;
                            countOfPalindromes++;

                        }
                        else if (palindromes[i + 1, j - 1] == 1)
                        {
                            palindromes[i, j] = 1;
                            countOfPalindromes++;
                        }
                    }

                }
            }
            return countOfPalindromes;
        }
    }
}
