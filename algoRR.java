import java.util.Scanner;

public class algoRR {
    public static void main(String[] args) {
        //qt - quantum time, bt - burst time, wt - waiting time, tat - turnaround time, rem_bt - Remaining burst time.
        int n, i, qt, count = 0, temp, sq = 0, bt[], wt[], tat[], rem_bt[];
        float awt = 0, atat = 0;
        bt = new int[10];
        wt = new int[10];
        tat = new int[10];
        rem_bt = new int[10];
        Scanner s = new Scanner(System.in);
        System.out.print("Enter the number of process: ");
        n = s.nextInt();
        System.out.print("Enter the burst time of the process\n");
        for (i = 0; i < n; i++) {
            System.out.print("P" + i + " = ");
            bt[i] = s.nextInt();
            rem_bt[i] = bt[i];
        }
        System.out.print("Enter the quantum time: ");
        qt = s.nextInt();
        while (true) {
            for (i = 0, count = 0; i < n; i++) {
                temp = qt;
                if (rem_bt[i] == 0) {
                    count++;
                    continue;
                }
                if (rem_bt[i] > qt)
                    rem_bt[i] = rem_bt[i] - qt;
                else if (rem_bt[i] >= 0) {
                    temp = rem_bt[i];
                    rem_bt[i] = 0;
                }
                sq = sq + temp;
                tat[i] = sq;
            }
            if (n == count)
                break;
        }
        System.out.print("------------------------------------------------------------------");
        System.out.print("\nProcess \t Burst Time\tTurnaround Time\t\tWaiting Time\n");
        System.out.print("-------------------------------------------------------------------");
        for (i = 0; i < n; i++) {
            wt[i] = tat[i] - bt[i];
            awt = awt + wt[i];
            atat = atat + tat[i];
            System.out.print("\n P" + (i + 1) + "\t\t\t" + bt[i] + "\t\t\t\t" + tat[i] + "\t\t\t\t" + wt[i] + "\n");
        }
        System.out.println("-------------------------------------------------------------------");
        awt = awt / n;
        atat = atat / n;
        System.out.println("\nAverage waiting Time = " + awt);
        System.out.println("Average turnaround time = " + atat);

        
    }
}
