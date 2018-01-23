import java.io.*;
import java.util.*;
public class CodedTriangleNumber{
  String[] text;
  Map<Character,Integer> dic= new HashMap<Character,Integer>();
  ArrayList<Double> wordValue = new ArrayList<Double>();
  ArrayList<Double> triangleNumbers = new ArrayList<Double>();
  public static void main(String[] args){
    CodedTriangleNumber o = new CodedTriangleNumber();
    o.go();
  }

  void go(){
    collectDic();
    try{
      BufferedReader reader =new BufferedReader(new FileReader("C:\\Users\\asus\\Desktop\\Euler\\CodedTriangleNumber\\p042_words.txt"));
      String line=null;
      while((line=reader.readLine())!=null){
        text=line.replaceAll("\"","").split(",");
      }
    }catch (Exception e) {
      e.printStackTrace();
    }
    for(String word : text){
      double value=0;
      for(Character c : word.toCharArray()){
        value+=dic.get(c);
      }
      // System.out.println(word+" "+value);
      wordValue.add(value);
    }
    collectTriangleNumber(Collections.max(wordValue));
    int sum=0;
    for(double i : wordValue){
      if(triangleNumbers.contains(i)){
        sum+=1;
      }
    }
    System.out.println(sum);
  }

  void collectDic(){
    int i=1;
    for(Character s : "abcdefghijklmnopqrstuvwxyz".toUpperCase().toCharArray()){
      dic.put(s,i);
      i+=1;
    }
    // dic.forEach((k,v)->System.out.println(k+" "+v));
  }

  void collectTriangleNumber(double limit){
    double triangleNumber=0;
    double n=1;
    while(triangleNumber<limit){
      triangleNumber=(n/2)*(n+1);
      triangleNumbers.add(triangleNumber);
      n+=1;
    }
    // triangleNumbers.forEach((v)->System.out.println(v));
  }


}
// import string
//
// with open('p042_words.txt') as text_file:
//     words=text_file.readline()
//
// words=words.strip('"').split('","')
//
//
// word_dic={}
// for i,c in enumerate(string.ascii_uppercase, start=1):
//     word_dic[c]=i
//
// words_values=[]
// for word in words:
//     value=0
//     for char in word:
//         value+=word_dic[char]
//     words_values.append(value)
//
// triangle_numbers=[]
// triangle_number=0
// n=1
//
// while triangle_number<max(words_values):
//     triangle_number=n/2*(n+1)
//     triangle_numbers.append(triangle_number)
//     n+=1
//
// print(triangle_numbers)
//
// print(len(words_values))
//
// sum_triangle=0
// for word_value in words_values:
//     if word_value in triangle_numbers:
//         sum_triangle+=1
//         print(word_value)
// print(sum_triangle)
