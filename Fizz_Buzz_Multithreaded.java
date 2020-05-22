class FizzBuzz {
    private int n;
    private int curr;
    private Lock lock;

    public FizzBuzz(int n) {
        this.n = n;
        this.curr = 1;
        this.lock = new ReentrantLock();
    }

    // printFizz.run() outputs "fizz".
    public synchronized void fizz(Runnable printFizz) throws InterruptedException {
        while (this.curr <= this.n) {
            while ((this.curr % 5 == 0) || (this.curr % 3 != 0)) {
                wait();
                if (this.curr > this.n) return;
            }
            printFizz.run();
            //System.out.println("p1");
            //System.out.println(this.curr);
            this.curr++;
            notifyAll();
        }
    }

    // printBuzz.run() outputs "buzz".
    public synchronized void buzz(Runnable printBuzz) throws InterruptedException {
        while (this.curr <= this.n) {
            while ((this.curr % 5 != 0) || (this.curr % 3 == 0)) {
                wait();
                if (this.curr > this.n) return;
            }
            printBuzz.run();
            //System.out.println("p2");
            //System.out.println(this.curr);
            this.curr++;
            notifyAll();
        }
    }

    // printFizzBuzz.run() outputs "fizzbuzz".
    public synchronized void fizzbuzz(Runnable printFizzBuzz) throws InterruptedException {
        while (this.curr <= this.n) {
            while ((this.curr % 5 != 0) || (this.curr % 3 != 0)) {
                wait();
                if (this.curr > this.n) return;
            }
            printFizzBuzz.run();
            //System.out.println("p3");
            //System.out.println(this.curr);
            this.curr++;
            notifyAll();
        }
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public synchronized void number(IntConsumer printNumber) throws InterruptedException {
        while (this.curr <= this.n) {
            while ((this.curr % 5 == 0) || (this.curr % 3 == 0)) {
                wait();
                if (this.curr > this.n) return;
            }
            printNumber.accept(this.curr);
            //System.out.println("p4");
            //System.out.println(this.curr);
            this.curr++;
            notifyAll();
        }
    }
}
