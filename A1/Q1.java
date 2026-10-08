import java.util.*;
class Q1{
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        String txt=sc.nextLine();
        StringBuilder newstr1=new StringBuilder();
        StringBuilder newstr2=new StringBuilder();
        
        for(int i=0;i<txt.length();i++)
        {
            char ch=txt.charAt(i);
            char chxor=(char) (ch^0);
            newstr1.append(chxor);
        }

        System.out.println("Plain text:"+txt);
        System.out.println("XOR with 0:"+newstr1);

        
        for(int i=0;i<txt.length();i++)
        {
            char ch=txt.charAt(i);
            char chxor=(char) (ch^1);
            newstr2.append(chxor);
        }

        System.out.println("Plain text:"+txt);
        System.out.println("XOR with 1:"+newstr2);
        sc.close();
    } 
}