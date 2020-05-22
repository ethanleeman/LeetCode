class ZeroEvenOdd {
    private int n;
    private int curr;
    private boolean printedzero;

    public ZeroEvenOdd(int n) {
        this.n = n;
        this.curr = 1;
        this.printedzero = false;
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public synchronized void zero(IntConsumer printNumber) throws InterruptedException {
        while (this.curr <= this.n) {
            while (this.printedzero == true) {
                wait();
                if (this.curr > this.n) return;
            }
            printNumber.accept(0);
            this.printedzero = true;
            notifyAll();
        }
    }

    public synchronized void even(IntConsumer printNumber) throws InterruptedException {
        while (this.curr <= this.n) {
            while (this.printedzero == false || this.curr % 2 == 1) {
                wait();
                if (this.curr > this.n) return;
            }
            printNumber.accept(this.curr);
            this.curr++;
            this.printedzero = false;
            notifyAll();
        }
    }

    public synchronized void odd(IntConsumer printNumber) throws InterruptedException {
        while (this.curr <= this.n) {
            while (this.printedzero == false || this.curr % 2 == 0) {
                wait();
                if (this.curr > this.n) return;
            }
            printNumber.accept(this.curr);
            this.curr++;
            this.printedzero = false;
            notifyAll();
        }
    }
}
