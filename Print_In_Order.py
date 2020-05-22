class Foo {
    private boolean first;
    private boolean second;


    public Foo() {
        first = false;
        second = false;
    }

    public synchronized  void first(Runnable printFirst) throws InterruptedException {
        first = true;
        // printFirst.run() outputs "first". Do not change or remove this line.
        printFirst.run();
        notifyAll();
    }

    public synchronized  void second(Runnable printSecond) throws InterruptedException {

        // printSecond.run() outputs "second". Do not change or remove this line.
        while (first == false) wait();
        second = true;
        printSecond.run();
        notifyAll();
    }

    public synchronized  void third(Runnable printThird) throws InterruptedException {

        // printThird.run() outputs "third". Do not change or remove this line.
        while (second == false || first == false) wait();
        printThird.run();
    }
}
