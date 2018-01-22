import java.io.*;
import java.util.*;

public class NamesScores{
  String text;
  public static void main(String[] args){
    NamesScores o = new NamesScores();
    o.go();
  }

  public void go(){
    try{
      // File textFile= new File("p022_names.txt");
      // FileReader fileReader= new FileReader(textFile);
      BufferedReader reader= new BufferedReader(new FileReader("p022_names.txt"));
      String line = null;
      while((line=reader.readLine())!=null){
        text=line;
      }
    }catch (Exception e) {
      e.printStackTrace();
    }
    text=text.replace("\"","");
    String [] arrayText=text.split(",");
    Arrays.sort(arrayText);
    Map <Character, Integer> dic = charValueDict();
    dic.forEach((k,v)->System.out.println("Key : " + k + " Value : " + v));

    int total = 0;
    int rank = 1;
    for(String name : arrayText){
      int tmp=0;
      for(char c : name.toCharArray()){
        tmp += dic.get(c);
      }
      total += tmp * rank;
      rank+=1;
    }
    System.out.println(total);
  }

  public Map <Character, Integer> charValueDict(){
    Map <Character, Integer> dic = new Hashtable<Character, Integer>();
    int i = 1;
    for(char c : "ABCDEFGHIJKLMNOPQRSTUVWXYZ".toCharArray()){
      dic.put(c,i);
      i+=1;
    }
    return dic;
  }
}
