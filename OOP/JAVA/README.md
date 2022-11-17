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

10. Difference between equals and '=='
    '==' compare the references. Reference address same or not.

    equals compare the object values

    obj1 = new Obj("Hello");
    obj2 = new Obj("Hello");
    
    if(obj1 == obj2) // return false. because of different references

    if(obj1.equals(obj2)) // return true;

11. Polymorphism: Reference variable belong to the parent. And, object belogs to the child
     Parent ref = new Child(); //run time polymorphim..

12. For an abstract class you can't create object for it. Not have defination, only have name. If parent class has N nubmer of abstract class. N number of abstruct class you have to redefine with defination in child class.
  <code>
   //Object to Object inheritance
    abstract class Shape{
        Shape(){
            //constructor
        }
        abstruct void draw(); //no def
    }

    class Circle extends Shape{
        void draw(){
            //code
        }
    }
  </code>

13. Interface 100% abstruction. All method  will be abstuct and public.Variable are not instance variable it will be static variable. Neither you nor run time create the object. 
    //not Object to Object inheritance
    <code>
      interface Shape{
        // no constructor
        void draw(); //public and abstruct 
      }

    class Circle implements Shape{
        public void draw(){
            //code
        }
      }
    </code>

14. What is polymorphism or dynamic method dispatch?
    -> It is a process in which a call to an override method is resolved at runtime rather than at complile-time.
    -> In this process, an overridden method is called through the reference variable of a superclass.
    -> The determination of the method to be called is based on the object being referred to by the reference variable.

15. Overloading vs Overriden method.


16. Can you override private and static method in java?   
 ->No, private method cann't override.
 -> If you create a similar method with same return type and same method arguments in child class then it will hide the super class method. This is known as method hiding. If child class method have to be static.

17. Multiple inheritance or daimond shape problem?
No, not suppoted.

18. A block is exectued when obj is created of a class. and a static block is executed when the class is loaded to the memory.

19. What is a servlet?

->java servlet is serve side technologies to extend the capbility of web servers by providing support for dynamic response and data persistence.
->The javax.servlet and javax.servlet.http packages provide interfaces and classes fro writing our own servlets.
->All servlets must impplement the javax.servlet.Servlet interface, which defines servlet lifecycle methods.
->As most web applications are accessed useing HTTP protocol, we mostly extend HttpServlet class. Servlet API hierarchy.

20. GET VS POST

GET:
->Data send through URL. So, limited amount of data can be sent.
->Not secured
->More efficient

POST:
->Large amount of data can be sent. Because data sent in body.
->Secured
->It is less efficient.










