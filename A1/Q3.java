import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Q3 {
    public static void main(String[] args) {

        try {
            File obj = new File("content.txt");
            Scanner reader = new Scanner(obj);

            StringBuilder sb = new StringBuilder();

            while (reader.hasNextLine()) {
                String data = reader.nextLine();

                for (int i = 0; i < data.length(); i++) {
                    char ch = data.charAt(i);

                    // Caesar cipher (+3)
                    if (ch >= 'A' && ch <= 'Z') {
                    ch = (char) ((ch - 'A' + 3) % 26 + 'A');
                   } else if (ch >= 'a' && ch <= 'z') {
                   ch = (char) ((ch - 'a' + 3) % 26 + 'a');
}

                    sb.append(ch);
                }
                sb.append("\n");
            }

            reader.close();

if (obj.exists()) {
    System.out.println("File already exists.");
} else {
    System.out.println("File created.");
}

FileWriter writer = new FileWriter(obj);
writer.write(sb.toString());
writer.close();

            System.out.println("File encrypted successfully.");

        } catch (IOException e) {
            System.out.println("An error has occurred.");
            e.printStackTrace();
        }
    }
}