import java.awt.*;
import java.util.Arrays;
import java.util.Date;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Date now = new Date();
        System.out.println(now);
        final float pi = 3.14f;
        //int x = 10 + 3 * 2; //16
        //int x = (10 + 3) * 2; //26

        String x = "1.1";
        double y = Double.parseDouble(x) + 2;
        System.out.println(y);

        Point point1 = new Point(1, 2);
        Point point2 = point1;
        point1.x = 3;
        System.out.println(point2);

        int age = 20, temperature = 22;
        int max = Math.max(age, temperature);
        System.out.println("The max is " + max);
        int myAge = 30;
        int herAge = myAge + 1;
        System.out.println("Her age is " + herAge);
        System.out.println("My age is " + myAge);
        System.out.println("Temp is " + temperature);

        String[] textblocks = {"Hei", "på", "deg"};
        System.out.println(Arrays.toString(textblocks));

        int num = 1;
        for (String textblock : textblocks) {
            System.out.print(num + ": ");
            System.out.println(textblock);
            num++;
        }

        String[] textblocks2 = {"Hei", "på", "deg"};
        for (int i = 0; i < textblocks2.length; i++) {
            System.out.println((i + 1) + ": " + textblocks2[i]);
        }
        String[][][] textblocks3 = {{{"Hei", "jeg", "prøver", "å"}}, {{"lære", "meg"}}, {{"java"}}};
        System.out.println(Arrays.deepToString(textblocks3));

        for (String[][] strings : textblocks3) {
            for (String[] string : strings) {
                for (String s : string) System.out.print(s + " ");
            }
        }
        System.out.println();

        String text = "hei på deg \"chris\"";
        String path = "C:\\windows\\...";
        System.out.println(path);
        System.out.println(text.endsWith("deg"));
        System.out.println(text.indexOf("p"));
        System.out.println(text.replace("h", "H"));
        System.out.println(text.substring(0, 1).toUpperCase() + text.substring(1));
        System.out.println(Character.toUpperCase(text.charAt(0)) + text.substring(1));

        Scanner scanner = new Scanner(System.in);
        System.out.print("Navn: ");
        String input = scanner.nextLine();
        System.out.println("Du heter " + input.trim().substring(0,1).toUpperCase() + input.trim().substring(1));
    }
}