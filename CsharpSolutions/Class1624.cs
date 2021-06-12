using System;
using System.Collections.Generic;

namespace CsharpSolutions
{
    public class Class1624:IAbstractSolution
    {
        public Class1624()
        {
        }

        public int MaxLengthBetweenEqualCharacters(string s)
        {
            int maxLength = 0;
            var hashKey = new Dictionary<int, int[]>();
            for (int i = 0; i < s.Length; i++)
            {
                char c = s[i];
                if (hashKey.ContainsKey(c))
                {
                    int[] newArray = hashKey[c];
                    newArray[1] = i;
                    if (maxLength < newArray[1] - newArray[0])
                        maxLength = newArray[1] - newArray[0];
                }
                else
                    hashKey.Add(c, (new int[] { i, i }));
            }
            return maxLength-1;
        }



        public void Main()
        {
            Console.WriteLine( MaxLengthBetweenEqualCharacters("cabbac"));
        }
    }
}
