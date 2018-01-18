import java.util.ArrayList;

public class Prime{
  int i = 2;
  ArrayList<Integer> primes = new ArrayList<Integer>();
  public static void main(String[] args){
    Prime o = new Prime();
    o.go();
  }

  public void go(){

    while (primes.size() < 10){
      boolean prime = true;
      for (int j = 2; j < this.i; j++){
        if (this.i % j == 0){
          prime = false;
          break;
        }
      }
      if (prime == true){
        primes.add(i);
      }
      this.i+=1;
    }
    System.out.println(primes);
    System.out.println(primes.get(primes.size()-1));
  }
}
