using System;
namespace CsharpSolutions
{
    public class Class1051:IAbstractSolution
    {
        public Class1051()
        {
        }
        public int HeightChecker(int[] heights)
        {
            int[] sortedHeights = (int []) heights.Clone();
            Array.Sort(sortedHeights);
            int totalIndices = 0;
            for (int i = 0; i < heights.Length; i++)
            {
                if (heights[i] != sortedHeights[i])
                    totalIndices++;
            }
            return totalIndices;
        }

        public void Main()
        {
            Console.WriteLine(HeightChecker(new int []{ 1, 1, 4, 2, 1, 3 }));
        }
    }
}
