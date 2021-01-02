using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

class Solution {

    /*
     * Complete the pageCount function below.
     */
    static int pageCount(int n, int p) {
      double last_page_num = Math.Floor(Convert.ToDouble(n) / 2.0);
      double goal_page_num = Math.Floor(Convert.ToDouble(p) / 2.0);
      return Math.Min(Convert.ToInt32(goal_page_num), Convert.ToInt32(last_page_num-goal_page_num));

    } 

     
           

       
    static void Main(string[] args) {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int n = Convert.ToInt32(Console.ReadLine());

        int p = Convert.ToInt32(Console.ReadLine());

        int result = pageCount(n, p);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}
