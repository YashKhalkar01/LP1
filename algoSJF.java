import java.util.Scanner;

public class algoSJF {
    public static void main(String[] args) {
        // Shortest Job First, Hence, process with shortest Burst shall be executed
        // first.
        int n;
        Scanner s = new Scanner(System.in);

        System.out.println("Shortest Job First Algorithm");
        System.out.println("Enter Number of Processes :");
        n = s.nextInt();
        int Process[] = new int[n];
        int Arrival[] = new int[n];
        int Burst[] = new int[n];
        int Waiting[] = new int[n];
        int Completion[] = new int[n];
        int TurnAround[] = new int[n];

        // input in processes array
        for (int i = 0; i < n; i++) {
            // System.out.println("Enter Process Number :");
            Process[i] = i+1;
            System.out.println("Enter Arrival Time For Process "+(i+1)+" :");
            Arrival[i] = s.nextInt();
            System.out.println("Enter Burst Time :");
            Burst[i] = s.nextInt();
        }

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (Burst[i] > Burst[j]) {
                    int tempBurst = Burst[i];
                    Burst[i] = Burst[j];
                    Burst[j] = tempBurst;
                    int tempP = Process[i];
                    Process[i] = Process[j];
                    Process[j] = tempP;
                    int tempAT = Arrival[i];
                    Arrival[i] = Arrival[j];
                    Arrival[j] = tempAT;
                }
            }
        }
        // to display
        int WT_avg = 0, TAT_avg = 0;
        System.out.println("---------------------------------------------------------------------");
        System.out.println("Process | Arrival | Burst | Completion | Turnaround | Waiting");
        System.out.println("---------------------------------------------------------------------");

        for (int i = 0; i < n; i++) {
            if (i == 0)
                Completion[0] = Burst[0] + Arrival[0]; // for 1st completion
            else
                Completion[i] = Math.max(Completion[i - 1], Arrival[i]) + Burst[i];
            TurnAround[i] = Completion[i] - Arrival[i];

            Waiting[i] = TurnAround[i] - Burst[i];

            System.out.println(Process[i] + "\t  " + Arrival[i] + "\t " + Burst[i] + "\t\t" + Completion[i] + "\t\t"
                    + TurnAround[i] + "\t" + Waiting[i]);
            
            WT_avg+= Waiting[i];
            TAT_avg+= TurnAround[i];
        }
        System.out.println("Stats :");
        System.out.println("Average Waiting Time: " + WT_avg / n);
        System.out.println("Average Turnaround time: " + TAT_avg / n);

        s.close();
    }

}
