import java.util.*;

public class DistinctPower{
  ArrayList<Double> order = new ArrayList<Double>();

  public static void main(String[] args){
    DistinctPower o = new DistinctPower();
    o.go();
  }

  void go(){
    for(int a=2;a<101;a++){
      for(int b=2;b<101 ;b++ ) {
        if(order.contains(Math.pow(a,b))){
          continue;
        }
        order.add(Math.pow(a,b));
      }
    }
    order.forEach(v->System.out.println(v));
    System.out.println(order.size());
  }
}
