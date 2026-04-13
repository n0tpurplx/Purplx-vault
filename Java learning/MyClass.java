// why am i even doing this?
// well basically this is all my progress of my java learning fully commented for future me
// i hope your proud future me!

// this makes a class
public class MyClass {
  public static void main(String[] args) { // this makes stuff work in the class
    String name = "John"; // this defines name as a String
    Byte x = 20, y = 1; // makes x and y integers
    Double yearTime = 0.4; // defines yearTime as a float
    Double age = x + y + yearTime; // calculates the age
    System.out.println(age); // this prints the age
    System.out.println(name); // this prints the name
    System.out.println(name + " is " + age + " years old!"); // this prints name and age
    String lengthTxt = "im not sure how long i am"; // create string for doing something
    System.out.println("the length of the string " + lengthTxt + " is " + lengthTxt.length()); // prints length of the string
    String txt = "hello im in all uppercase";
    System.out.println(txt.toUpperCase());
}
}
