using System;
using System.Collections.Generic;

namespace CsharpSolutions
{
    public class Class1337 : IAbstractSolution
    {
        public Class1337()
        {
        }

        public int[] KWeakestRows(int[][] mat, int k)
        {
            int[] kWeakestRows = new int[k];
            var binaryHeap = new SortedDictionary<int, List<int>>();
            var strength = 0;
            for (int i = 0; i < mat.Length; i++)
            {
                strength = 0;
                for (int j = 0; j < mat[i].Length; j++)
                {
                    if (mat[i][j] == 0)
                        break;
                    strength++;
                }
                if (binaryHeap.ContainsKey(strength))
                {
                    binaryHeap[strength].Add(i);
                }
                else
                    binaryHeap.Add(strength, new List<int>() { i });

            }
            int c = 0;
            bool exit = false;
            foreach (var element in binaryHeap)
            {
                foreach (var item in element.Value)
                {
                    if (c == k)
                    {
                        exit = true;
                        break;
                    }
                    kWeakestRows[c++] = item;
                }
                if (exit)
                    break;
            }

            return kWeakestRows;
        }
        public void Main()
        {

            int[][] array ={ new int []{ 1,1,0,0,0}, new int []{ 1,1,1,1,0},new int [] { 1,0,0,0,0},
                new int []{ 1,1,0,0,0},new int []{ 1,1,1,1,1} };

            var output = KWeakestRows(array,3);

            foreach (var item in output)
                Console.WriteLine(item);

        }
    }
}
