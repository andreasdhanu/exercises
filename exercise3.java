import java.util.*;
public class PermutedMultiples{
  int startingNumber=125874;
  public static void main(String[] args){
    PermutedMultiples obj = new PermutedMultiples();
    obj.play();
  }

  private void play(){
    while (true){
      ArrayList<String> a = new ArrayList<String>(Arrays.asList(String.valueOf(startingNumber).split("")));
      ArrayList<String> b = new ArrayList<String>(Arrays.asList(String.valueOf(startingNumber*2).split("")));
      ArrayList<String> c = new ArrayList<String>(Arrays.asList(String.valueOf(startingNumber*3).split("")));
      ArrayList<String> d = new ArrayList<String>(Arrays.asList(String.valueOf(startingNumber*4).split("")));
      ArrayList<String> e = new ArrayList<String>(Arrays.asList(String.valueOf(startingNumber*5).split("")));
      ArrayList<String> f = new ArrayList<String>(Arrays.asList(String.valueOf(startingNumber*6).split("")));
      Collections.sort(a);
      Collections.sort(b);
      Collections.sort(c);
      Collections.sort(d);
      Collections.sort(e);
      Collections.sort(f);
      if(a.equals(b) && a.equals(c) && a.equals(d) && a.equals(e) && a.equals(f)){
        System.out.println(startingNumber);
        break;
      }
      startingNumber+=1;
    }
  }
}
