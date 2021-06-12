using System;
namespace CsharpSolutions
{
    public class Class795 : IAbstractSolution
    {
        public Class795()
        {
        }


        public int NumSubarrayBoundedMax(int[] nums, int left, int right)
        {
            int noOfSubarrays = 0;
            int counter = 0;
            int maxNo = -1;
            int[] factorials = new int[nums.Length + 1];
            int factorialTillNow = 1;
            for (int i = 0; i < nums.Length; i++)
            {
                factorialTillNow *= (i + 1);
                factorials[i + 1] = factorialTillNow;
                if (nums[i] > maxNo)
                    maxNo = nums[i];

                if (maxNo >= 0 && (maxNo < left || maxNo > right))
                {
                    noOfSubarrays += factorials[counter];
                    counter = 0;
                    maxNo = -1;
                }
                else
                {
                    counter++;
                }
            }
            noOfSubarrays += factorials[counter];


            return noOfSubarrays;
        }


        public void Main()
        {
            // Console.WriteLine(NumSubarrayBoundedMax(new int[] { 2, 9, 2, 5, 6 }, 2,8));
            Console.WriteLine(NumSubarrayBoundedMax(new int[] { 73, 55, 36, 5, 55, 14, 9, 7, 72, 52 }, 32, 69));

        }
    }
}
