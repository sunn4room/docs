# 并发编程

## 线程

```java
// case 1
Thread t = new Thread(() -> {
    // ...
});
t.start();

// case 2
FutureTask<String> task = new FutureTask<>(() -> {
    // ...
    return "done";
});
new Thread(task).start();
// 阻塞至得到"done"
String result = task.get();

// case 3
// 定义线程类
class MyThread extends Thread {
    @Override
    public void run() {
        // ...
    }
}
// 实例化线程类
Thread t = new MyThread();
t.start();
```

> 另见 [Thread API](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Thread.html)、[Runnable API](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Runnable.html)、[FutureTask API](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/concurrent/FutureTask.html)

### 线程状态

| State         | Description                  |
| ------------- | ---------------------------- |
| NEW           | 未启动                       |
| RUNNABLE      | 可执行，具体取决于系统调度   |
| BLOCKED       | 因不能独占监视器而阻塞       |
| WAITING       | 无限休眠，等待唤醒           |
| TIMED_WAITING | 限时休眠，等待倒计时或者唤醒 |
| TERMINATED    | 终止运行                     |

> 另见 [Thread.State API](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Thread.State.html)

### 线程中断

强行结束线程的方法不安全，推荐使用中断来优雅地结束线程，如何中断将由线程自己决定。

```java
Thread t = new Thread(() -> {
    while (true) {
        if (Thread.interrupted()) {
            // post handle
            break;
        }
        // normal handle
    }
});
t.start();
// ...
t.interrupt();
```

> 另见 [interrupt API](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Thread.html#interrupt())

### 执行器



## volatile

| Time | Thread A           | Thread B          |
| ---- | ------------------ | ----------------- |
| 1    | actions before set | ...               |
| 2    | set volatile       | ...               |
| 3    | ...                | get volatile      |
| 4    | ...                | actions after get |

## synchronized

在 Java 中，每个对象都可以是一个监视器 moniter ，synchronized 通过独占监视器来实现同步代码的目的。

### synchronized 块

```java
Object lock = new Object();
synchronized (lock) {
    // ... moniter lock
}
```

### synchronized 方法

```java
class A {
    public static synchronized void staticmethod() {
        // ... moniter A.class
    }

    public synchronized void instancemethod() {
        // ... moniter this
    }
}
```

> **等待与唤醒**
>
> 在同步代码中，可以调用监视器对象的相关方法，主动释放监视器并休眠当前线程，也可以主动唤醒监视器的其他休眠线程。另见 [Object API](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html)

### 私有锁

```java
// lock 不能被外部访问，有效防止外部滥用而导致的死锁
class A {
    private static final Object lock1 = new Object();
    public static void staticmethod() {
        synchronized (lock1) {
            // ...
        }
    }

    private final Object lock2 = new Object();
    public void instancemethod() {
        synchronized (lock2) {
            // ...
        }
    }
}
```

## Lock

监视器的对象化，相比于 synchronized 更加灵活。另见 [Lock API](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/concurrent/locks/Lock.html)

### ReentrantLock

Lock 接口的标准实现

```java
Lock lock = new ReentrantLock();

// case 1
lock.lock();
try {
    // ...
} finally {
    lock.unlock();
}

// case 2
if (lock.tryLock()) {
    try {
        // ...
    } finally {
        lock.unlock();
    }
}
```

> **Lock 的等待与唤醒**
>
> 监视器同时承担了锁和线程通信两个功能，而同步锁只负责锁功能，线程通信则交给 Condition 对象来负责，这样，一个同步锁可以产生多个 Condition 对象，且多个 Condition 对象只负责自己的等待线程，不会相互影响。另见 [Condition API](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/concurrent/locks/Condition.html)

> **ReadWriteLock**
>
> 读写锁，可有效提高并发性能。另见 [ReadWriteLock API](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/concurrent/locks/ReentrantReadWriteLock.html)、[ReentrantReadWriteLock API](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/concurrent/locks/ReentrantReadWriteLock.html)

### LockSupport

线程阻塞原语，Lock 的相关实现都需要调用 LockSupport 的相关方法。另见 [LockSupport API](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/concurrent/locks/LockSupport.html)

