import java.util.ArrayList;

public class LargestPalindromeProduct{
  ArrayList<Integer> palindrome = new ArrayList<Integer>();
  public static void main(String[]args){
    LargestPalindromeProduct o = new LargestPalindromeProduct();
    System.out.println(o.go());
  }

  public int go(){
    int result = 0;
    boolean check = false;
    for (int i = 99; i>0; i--){
      for (int j = 99; j>0; j--){
        StringBuilder sb = new StringBuilder(Integer.toString(i*j)).reverse();
        System.out.println(sb);
        if ((Integer.toString(i*j)).equals(sb.toString())){
          check = true;
          result = i*j;
          break;
        }
        if (check){
          break;
        }
      }
    }
    return result;
  }
}
