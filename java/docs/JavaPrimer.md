# A Java Primer

## 1 Hello world program:

This is the hello world program written in Java

```java
public class Hello {

	public static void main(String args[]) {

		System.out.println("Hello World");

	}

}
```

## 2 Base type:

```java
boolean flag = true;
char grade = 'A';
byte b = 12;
short s = 24;
int i, j, k = 256;
long l = 890L;
float pi = 3.1416F;
double e = 2.3423, a = 124324e3;
```

## 3 Classes and Objects:

Members of a class in Java: 

* Instance variables
* Methods 
 * **Accessor** method: does not update the instance variables
 * **Update** method: update the instance variables

A demo class:

```java
public class Counter {
	
	public class Counter() {  }

	public void increase(int n) {  }

	public void decrease(int n ) {  }

}
```

### 3.1 Creating a class:

```java
Counter c = new Counter();
```

Classes are known as **reference types** in Java, and a variable of that type (such as c in the example) is known as a **reference variable**  
A reference variable is capable of storing the location (i.e., **memory address**) of an object from the declared class  

> Three events occur as part of the creation of a new instance of a class:  

> * A new object is dynamically allocated in memory, and all instance variables are initialized to standard default values. The default values are **null** for reference variables and 0 for all base types except **boolean** variables (which are **false** by default).

> * The constructor for the new object is called with the parameters specified. The constructor may assign more meaningful values to any of the instance variables, and perform any additional computations that must be done due to the creation of this object.

> * After the constructor returns, the **new** operator returns a reference (that is, a memory address) to the newly created object. If the expression is in the form of an assignment statement, then this address is stored in the object variable, so the object variable **refers** to this newly created object.

### 3.2 The Dot Operator:

To access the members of the class. We call a method associated with an object by using the reference variable name, following that by the dot operator and then the method name and its parameters.

For example:
```java
c.getCount();
c.increment();
```

> Side note: a method's name combined with the number and types of its parameters is called a method's **_signature_**, for it takes all of these parts to determine the actual method to perform for a certain method call.

### 3.3 Defining a class:

#### a. Modifiers:

* Access control modifers:
 * **public**: all classes may access the defined aspect.
 * **protected**: access to the defined aspect is only granted to the following groups of other classes:   
   * **subclasses** of the given class  
	* classes that belong to the same **package** of the given class
 * **private**: access to a defined member of class be granted only to code withing that class. Neither subclasses nor any other classes have access to such members.

* **static** modifier:

> Static variables are used to store "global" information about a class. (For example, a static variable could be used to maintain the total number of instances of that class that have been created.) Static variables exist even if no instance of their class exists.
