import java.util.concurrent.Semaphore;

public class ReaderWriter {
    static Semaphore mutex = new Semaphore(1); // Mutex to control access to read_count
    static Semaphore database = new Semaphore(1); // Semaphore to control access to database
    static int readCount = 0; // To keep track of number of readers

    static void reader() throws InterruptedException {
        while (true) {
            mutex.acquire(); // Acquire mutex to modify readCount
            readCount++;
            if (readCount == 1) {
                database.acquire(); // First reader acquires the database semaphore
            }
            mutex.release(); // Release mutex after modifying readCount

            // Reading data
            System.out.println(readCount + " User Reading the Data.........");

            mutex.acquire(); // Acquire mutex to modify readCount
            readCount--;
            if (readCount == 0) {
                database.release(); // Last reader releases the database semaphore
            }
            mutex.release(); // Release mutex after modifying readCount

            System.out.println("Reading Finished!!!!!!");
            break;
        }
    }

    static void writer() throws InterruptedException {
        while (true) {
            database.acquire(); // Writer acquires database semaphore

            // Writing to the database
            System.out.println("Writing on the database......");

            database.release(); // Writer releases database semaphore

            System.out.println("Writing Finished!!!!!.");
            break;
        }
    }

    public static void main(String[] args) throws InterruptedException {
        // Creating writer and reader threads to demonstrate concurrency
        Thread writerThread = new Thread(() -> {
            try {
                writer();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });

        Thread readerThread1 = new Thread(() -> {
            try {
                reader();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });

        Thread readerThread2 = new Thread(() -> {
            try {
                reader();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });

        writerThread.start();
        readerThread1.start();
        readerThread2.start();

        // Wait for all threads to finish
        writerThread.join();
        readerThread1.join();
        readerThread2.join();
    }
}
