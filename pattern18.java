// Online Java Compiler
// Use this editor to write, compile and run your Java code online

class Main {
    public static void main(String[] args) {
        int n = -1;
        for (int i = 0; i<n; i++) {
            char ch = (char) ('A' + n - i - 1);
            for(int j =n-i; j<=n; j++) {
                System.out.print(ch);
                ch++;
            }
            System.out.println();
        }
    }
}