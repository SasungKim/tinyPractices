package pretopost;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Stack;

/**
 *
 * @author Sasung
 */
public class PreToPost {
    
    public static boolean isNum(String s){
        try{
            Integer.parseInt(s);
            return true;
        }
        catch(NumberFormatException e){
            return false;
        }
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line;
        Stack<String> ans = new Stack<String>();
        
        while(!(line = br.readLine()).equals("0")){
            String[] b = line.split(" ");
            for (int i = b.length-1; i >= 0; i--){
                if(isNum(b[i]))
                    ans.push(b[i]);
                
                else
                    ans.push(ans.pop() + " " + ans.pop() + " " + b[i]);
                    
            }
            System.out.println(ans.pop());
        }
    }
}
