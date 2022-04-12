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

    public static synchronized void instancemethod() {
        // ... moniter this
    }
}
```

### 等待和唤醒

> 必须在同步代码中调用监视器对象 moniter 的相关 wait notify 方法

```java
moniter.wait() // 阻塞线程并释放moniter，直到被唤醒且重新获取moniter，或者线程被中断并抛出异常
moniter.wait(1000) // 阻塞线程并释放moniter，直到被唤醒且重新获取moniter，或者线程被中断并抛出异常，或者一秒后自动唤醒且重新获取moniter
moniter.notify() // 随机唤醒一个阻塞在当前moniter的线程，但不立刻释放moniter
moniter.notifyAll() // 唤醒所有阻塞在当前moniter的线程，但不立刻释放moniter
```

### 私有锁

```java
class A {
    // lock 不能被外部访问，有效防止死锁
    private final Object lock = new Object();
    public void instancemethod() {
        synchronized (lock) {
            // ...
        }
    }
}
```


