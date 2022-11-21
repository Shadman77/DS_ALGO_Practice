import java.util.LinkedList;

public class LinkedListImplementation {
    public static void main(String[] args) {
        LinkedList<String> ll = new LinkedList<String>();

        ll.add("hi");
        System.out.println(ll); //[hi]

        ll.add(0, "hello");
        System.out.println(ll); //[hello, hi]

        ll.addLast("last element");

        ll.add("uchchwas");

        System.out.println(ll.peek()); //hello
        System.out.println(ll.peekLast()); //uchchwas
        System.out.println(ll); //[hello, hi, last element, uchchwas]

        System.out.println(ll.poll()); // hello// retrive and remove the first element
        System.out.println(ll); //[hi, last element, uchchwas]

        System.out.println(ll.pop()); //delete the first element as stack do// hi

        ll.push("hi2");
        System.out.println(ll); //push onto stack //[hi2, last element, uchchwas]

        ll.remove("hi2");

        System.out.println(ll); //[last element, uchchwas]

        System.out.println(); //This method returns a shallow copy of this LinkedList.

        System.out.println("final linked list : "+ll); //final linked list : [last element, uchchwas]
        ll.clear();//remove all the element from the linkedlist

        System.out.println(ll); //[]



    }
}
