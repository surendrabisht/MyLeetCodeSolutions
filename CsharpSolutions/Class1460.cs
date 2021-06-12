using System;
using System.Collections.Generic;
namespace CsharpSolutions
{
    public class Class1460: IAbstractSolution
    {
        public Class1460()
        {
        }

        public bool CanBeEqual(int[] target, int[] arr)
        {
            bool isSame = false;

            var hashKey = new Dictionary<int, int>();
            foreach (char c in arr)
            {
                if (hashKey.ContainsKey(c))
                {
                    hashKey[c]++;
                }
                else
                    hashKey.Add(c, 1);


            }

            var countOfMatchedChars = 0;
            foreach (char c in target)
            {
                if (hashKey.ContainsKey(c) && hashKey[c] > 0)
                {
                    hashKey[c]--;
                    countOfMatchedChars++;
                }
                else
                {
                    break;
                }
            }
            if (countOfMatchedChars == arr.Length)
                isSame = true;
            return isSame;
        }


        public void Main()
        {
            throw new NotImplementedException();
        }
    }
}
