using System;
using System.Collections.Generic;
namespace CsharpSolutions
{
    public class Class1451 : IAbstractSolution
    {
        public Class1451()
        {
        }

        public string ArrangeWords(string text)
        {
            string arrangedWords = "";
            text = text + " ";
            SortedDictionary<int, List<String>> sortedwords = new SortedDictionary<int, List<string>>();

            string word = "";
            int length;
            for (int i = 0; i < text.Length; i++)
            {

                if (text[i].Equals(' '))
                {
                    length = word.Length;
                    if (sortedwords.ContainsKey(length))
                        sortedwords[length].Add(word);
                    else
                        sortedwords.Add(length, new List<string>() { word });
                    word = "";
                }
                else
                {
                    if (i == 0)
                    {
                        word = "" + char.ToLower(text[i]);
                    }
                    else { word = word + text[i]; }
                }

            }

            bool isFirstWord = true;
            foreach (var item in sortedwords)
            {
                foreach (var sortedWord in item.Value)
                {
                    var word1 = sortedWord;
                    if (isFirstWord)
                    {
                        word1 = "" + char.ToUpper(sortedWord[0]);
                        if (sortedWord.Length > 1)
                            word1 += sortedWord.Substring(1);
                    }
                    arrangedWords += word1 + " ";
                    isFirstWord = false;
                }
            }
            arrangedWords = arrangedWords.Substring(0, arrangedWords.Length - 1);
            
            return arrangedWords;
        }

        public void Main()
        {
            Console.WriteLine(ArrangeWords("Keep calm and code on"));
        }
    }
}
