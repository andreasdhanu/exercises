class Function{
  int multiple(int input){
    int data = 0;
    for (int i=0; i<input; i++) {
      if ((i%3==0)||(i%5==0)) {
        data += i;
      }
    }
    return data;
  }
}

public class MultiplesOf3and5{
  public static void main(String[] args) {
    Function o = new Function();
    System.out.println(o.multiple(1000));
  }
}
