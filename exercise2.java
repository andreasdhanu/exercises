import java.util.ArrayList;

public class SummationOfPrimes{

  private int max = 0;
  ArrayList<Integer> primes = new ArrayList<Integer>();

  public static void main(String[] args){
    SummationOfPrimes o = new SummationOfPrimes();
    try {
      System.out.println(args[0]);
    }
    catch (Exception e) {
      System.out.println(e);
      System.out.println("Program will exit...");
      System.exit(0);
    }
    o.go(Integer.parseInt(args[0]));
  }

  public void go(int numMax){
    int sum = 0;
    for (int i =2; i < numMax; i++){
      boolean prime = true;
      for (int j = 2; j < i; j++){
        if (i % j == 0){
          prime = false;
          break;
        }
      }
      if (prime == true){
        primes.add(i);
        sum += i;
      }
    }
    System.out.println(primes);
    System.out.println(sum);
  }
}
