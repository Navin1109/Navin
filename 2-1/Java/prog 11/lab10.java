import java.util.Scanner;
import java.util.InputMismatchException;
public class Exception{
    public static void main(String args[]){
        try{
            Scanner s=new Scanner(System.in);
            int l=s.nextInt();
            int a=45;
            int c;
            c=a/l;
        }
        catch(ArithmeticException e){
            System.out.println("Exception raised:"+e);
        }
        catch(InputMismatchException e){
            System.out.println("Exception raised :"+e);
        }
    }
}