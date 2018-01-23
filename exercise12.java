import java.util.*;
public class CoinSums{

  ArrayList<String> coins = new ArrayList<String>();

  public static void main(String[] args){
    CoinSums objectCoinSums = new CoinSums();
    objectCoinSums.go();
  }

  void go(){
    for(int i=0;i<2;i++){
      for(int j=0;j<3;j++){
        for(int k=0;k<5;k++){
          for(int l=0;l<11;l++){
            for(int m=0;m<21;m++){
              for(int n=0;n<41;n++){
                for(int o=0;o<101;o++){
                  for(int p=0;p<201;p++){
                    int sum=k*50+j*100+i*200+l*20+m*10+n*5+o*2+p*1;
                    String tmp=i+" "+j+" "+k+" "+l+" "+m+" "+n+" "+o+" "+p;
                    System.out.println(tmp);
                    if(sum==200){
                      coins.add(tmp);
                      break;
                    }
                    else if (sum>200) {
                      break;
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
    System.out.println(coins.size());
  }
}
