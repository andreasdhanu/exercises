

public class SelfPowers{
  public static void main(String[] args){
    SelfPowers o = new SelfPowers();
    o.go();
  }

  void go(){
    double sum=0,result=0;
    for(double i=1;i<1001;i++){
      result=Math.pow(i,i);
      sum+=result;
    }
    System.out.println(sum);
  }
}
