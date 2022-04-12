# 并发编程

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
