public class ChampernownesConstant{
  String strNum="";
  public static void main(String[] args){
    ChampernownesConstant o = new ChampernownesConstant();
    o.go();
  }

  void go(){
    int i = 0;
    while(strNum.length()<=1000000){
      strNum+=i;
      i+=1;
    }
    System.out.println(strNum);
    System.out.println(Character.getNumericValue(strNum.charAt(1))*Character.getNumericValue(strNum.charAt(10))*Character.getNumericValue(strNum.charAt(100))*Character.getNumericValue(strNum.charAt(1000))*Character.getNumericValue(strNum.charAt(10000))*Character.getNumericValue(strNum.charAt(100000))*Character.getNumericValue(strNum.charAt(1000000)));
  }
}


//
//
// str_num=''
// i=0
// while len(str_num)<=1000000:
//     str_num+=str(i)
//     i+=1
//
// print(str_num)
// print(int(str_num[1])*int(str_num[10])*int(str_num[100])*int(str_num[1000])*int(str_num[10000])*int(str_num[100000])*int(str_num[1000000]))
