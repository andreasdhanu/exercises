// import math
//
// def combinatoric(n, r):
//     return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
//
// counter=0
// for i in range(1,101):
//     for j in range(1,i):
//         combinatoric_value=combinatoric(i,j)
//         if combinatoric_value<=1000000:
//             continue
//
//         print(i,j,combinatoric_value)
//         counter+=1
//
// print(counter)
import java.math.BigInteger;
import java.math.BigDecimal;
public class CombinatoricSelection{
  public static void main(String[] args){
    CombinatoricSelection obj = new CombinatoricSelection();
    obj.play();
  }

  private BigDecimal doFactorial(int input){
    if(input==0){
      return BigDecimal.valueOf(1);
    }
    BigInteger output= BigDecimal.valueOf(1);
    for(int i =1;i<=input;i++){
      output.multiply(BigDecimal.valueOf(i));
    }
    return output;
  }

  private BigDecimal doCombinatoric(int n, int r){
    return doFactorial(n).divide((doFactorial(r).multiply(doFactorial(n-r))));
  }

  private void play(){
    for (int i = 1;i<=101;i++){
      for (int j = 1;j<i;j++){
        // double combinatoricResult=doCombinatoric(i,j);
        // if(combinatoricResult<=1000000){
        //   continue;
        // }
        // System.out.println(i+" "+j+" "+combinatoricResult);
        // System.out.println(i+" "+j);

      }
      System.out.println(i+" "+doFactorial(i));
    }
  }
}
