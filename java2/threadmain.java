class thread1 implements Runnable
{
    public void run()
    {
        System.out.println("hello");

    }
}
class thread2 implements Runnable
{
    public void run()
    {
        System.out.println("world");
    }
}
class threadmain
{
    public static void main(String ar[])
    {
        thread1 t1=new thread1();
        thread2 t2=new thread2();
        Thread T1=new Thread(t1);
        Thread T2=new Thread(t2);
        T1.start();
        T2.start();
    }
}