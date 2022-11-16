👋 Basic JAVA OOP
    ✨ Resource 
        - https://www.youtube.com/playlist?list=PLgH5QX0i9K3oAZUB2QXR-dZac0c9HNyRa


# Questions:

1. Compare With boxing and unboxing

int i = 5 ; //single value container
Integer iRef = new Integer(i); //boxing //obj
int k = iRef.intValue();// unboxint //obj

Interger kRef = i; //AutoBoxing 
int k = kRef; //AutoUnboxing

2. 
   final vs finally vs finalize
final: final is a keyword work like const. 
      final int a = 100;
finally: Inside the finally block code is always executed. Either error(exceptions) comes or not. The codes must be executed in the finally block
      try{
            int x = 10;  
        }catch(Exception ex){System.out.println('Error Found');}
        finally{
            System.out.println('This code must be exected');
        }

finalize: Is like a destructor whenever object will be removed from the memory by the garbage collector. So, this finalize method will be executed.
        finalize example1 = new finallize();
        example1 = NULL;
        system.gc();

3. String is immutable. StringBuffer and StringBuilder is mutable;
 String obj = new String("hello");
 StringBuilder builder = new StringBuilder("bulider string"); //String builder operations are not thread safe.
                                                              //String builder is the sigle thread environment.
                                                              //faster than string buffer.

 StringBuffer buffer = new StringBuffer("StringBuffer string"); //Stringbuffer operations are thread safe and synchonized. 
                                                                //It is used when  multiple threads are working on same string.

 buffer.append("Hi..");
 String newString = obj.concat('hi'); 
 System.out.println(obj);//Output will be 'hello' because string are immutable. 

4. Difference between Stack and Heap memory.




