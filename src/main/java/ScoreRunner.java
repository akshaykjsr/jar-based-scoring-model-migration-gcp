import java.io.*;

public class ScoreRunner {
    public static void main(String[] args) {
        if (args.length != 2) {
            System.err.println("Usage: java -jar score-model.jar input.csv output.csv");
            System.exit(1);
        }

        String inputCsv = args[0];
        String outputCsv = args[1];

        try {
            ProcessBuilder pb = new ProcessBuilder("python3", "model/score.py", inputCsv, outputCsv);
            pb.redirectErrorStream(true);  // Merge stderr into stdout
            Process process = pb.start();

            // Print output from the Python script
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }

            int exitCode = process.waitFor();
            if (exitCode == 0) {
                System.out.println("✅ Python inference complete.");
            } else {
                System.err.println("❌ Python script failed with exit code: " + exitCode);
            }

        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
