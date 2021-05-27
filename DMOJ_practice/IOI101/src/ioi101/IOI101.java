package ioi101;

import java.util.Scanner;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 *
 * @author Sasung
 */
public class IOI101 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String s = sc.next();
        char[] toChar = s.toCharArray();

        for (int i = 0; i < s.length(); i++) {
            switch (toChar[i]) {
                case '0':
                    toChar[i] = 'O';
                    break;
                case '1':
                    toChar[i] = 'l';
                    break;
                case '3':
                    toChar[i] = 'E';
                    break;
                case '4':
                    toChar[i] = 'A';
                    break;
                case '5':
                    toChar[i] = 'S';
                    break;
                case '6':
                    toChar[i] = 'G';
                    break;
                case '8':
                    toChar[i] = 'B';
                    break;
                case '9':
                    toChar[i] = 'g';
                    break;
            }
        }
        System.out.println(String.valueOf(toChar));
    }
}