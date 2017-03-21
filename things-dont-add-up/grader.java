import java.util.Scanner;

public class grader {
    
    public static void main(String[] args) {
        

        Scanner s = new Scanner(System.in);
        
        int A = s.nextInt(), B = s.nextInt(), N = s.nextInt(), count = 0;
        int[] nugs = new int[N];
        for(int i = 0; i < N; i++)
            nugs[i] = s.nextInt();


        // 1 10000000 16 788069 788246 419404 186300 847360 357398 969137 457317 770314 238904 904353 340869 513632 232159 549739 279898        
        boolean[] poss = new boolean[B + 1];
        poss[0] = true;
        for(int i = 0; i < A; i++)
            if(poss[i])
                for(int n : nugs)
                    if(i + n <= B)
                        poss[i + n] = true;
        for(int i = A; i <= B; i++)
            if(poss[i]) {
                for(int n : nugs)
                    if(i + n <= B)
                        poss[i + n] = true;
            }
            else count++;
        System.out.println(count);
        
    }
    
}