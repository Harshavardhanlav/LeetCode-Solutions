class Main {
    public static void main(String[] args) {
        int n =4;
        int k = n;
        int s = n+1;
        for(int i = 0; i < n; i++) {
            for(int j = n; j > k; j--) {
                System.out.print(j);
            }
            for(int j =0; j <k; j++ ) {
                System.out.print(k);
            }
            for(int j =0; j <k-1; j++ ) {
                System.out.print(k);
            }
            int x = s;
            for(int j =0; j< i; j++) {
                System.out.print(x);
                x+=1;
            }
            s-=1;
            System.out.println();

            k-=1;
        }
        for(int i = 0; i < n; i++) {
            for(int j = n; j > k; j--) {
                System.out.print(j);
            }
            for(int j =0; j <k; j++ ) {
                System.out.print(k);
            }
            System.out.println();

            k-=1;
        }
    }
}