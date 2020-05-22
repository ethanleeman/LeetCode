class H2O {
    public int ox;
    public int hyg;
    public Lock lock;

    public H2O() {
        this.ox = 0;
        this.hyg = 0;
        this.lock = new ReentrantLock();
    }

    public synchronized void hydrogen(Runnable releaseHydrogen) throws InterruptedException {

        // releaseHydrogen.run() outputs "H". Do not change or remove this line.
        while (this.hyg == 2) {
            wait();
        }
        this.lock.lock();
        try {
            releaseHydrogen.run();
            this.hyg++;
            if (this.hyg == 2 && this.ox == 1) {
                this.hyg = 0;
                this.ox = 0;
            }
            notifyAll();
        }
        finally {
        this.lock.unlock();
        }
    }

    public synchronized void oxygen(Runnable releaseOxygen) throws InterruptedException {

        // releaseOxygen.run() outputs "O". Do not change or remove this line.
        while (this.ox == 1) { wait();}
        this.lock.lock();
        try {
		    releaseOxygen.run();
            this.ox++;
            if (this.hyg == 2 && this.ox == 1) {
                this.hyg = 0;
                this.ox = 0;
            }
            notifyAll();
        } finally {
            this.lock.unlock();
        }

    }
}
