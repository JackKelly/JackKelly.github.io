---
title: "Where to make notes whilst learning a new programming language"
date: 2012-03-02 16:59:41 +0000
categories: ["programming"]
permalink: /where_to_make_notes_whilst_learning_a_new_programming_language
---
For the past few days I've been teaching myself JavaScript for a PhD
project. I'm using the excellent book "[JavaScript: The Good Parts" by
Douglas
Crockford](http://www.amazon.co.uk/JavaScript-Good-Parts-Douglas-Crockford/dp/0596517742).
 To begin with, I took notes in my hand-written note book.  But that was
slow and clunky.  So I started making notes in Google Docs.  But that
doesn't have syntax highlighting.  So it finally dawned on me: the best
place to make notes whilst learning a new language is in code!  This
feels so blindingly obvious now that I feel dumb mentioning it but it
took me a little while to figure out.  Of course, we all tinker with
code snippets whilst learning a new language.  But I'm now trying to get
into the habit of creating a new file for each topic, and to put lots of
comments in the code to explain each new language feature that I learn.
 The code will be my (runnable) notes.

For example, here's my file on the topic of function invocation:

<!--break-->

 

<div class="geshifilter">

``` {.javascript .geshifilter-javascript style="font-family:monospace;"}
/* 
  From Chapter 4: Functions.
  Section on "Invocation"  
  * Every function receives 2 additional parameters: 'this' and 'arguments'.
  * There are no runtime errors if a function is called with the
    wrong number of arguments.
  * The value of 'this' is determined by the invocation pattern.
  * There are 4 invocation patterns in JS: 
     *  method invocation
     *  function invocation
     *  constructor invocation 
     *  apply invocation pattern
*/
 
/****************************
 * 1: METHOD INVOCATION     
 * 
 * When a function if stored as a property of an object,
 * we call it a METHOD. When a method is invoked,
 * 'this' is bound to that object.
 */
 
// Public method; can be used in any number of objects
function incrementFunc(inc)
{
    // 'this' will be bound to the object for whom
    // this function is a method. Binding happens
    // at invocation time.
    this.value += typeof inc === 'number' ? inc : 1;
}
 
function methodInvocationTest()
{
    print("Method invocation pattern:");
 
    // Create an object literal
    var myObject = {
        value : 0,
        increment : incrementFunc // Very late binding. Bound at invocation time.
    };
 
    print("Initial value = " + myObject.value);
    myObject.increment();
    print("After incrementing by default amount = " + myObject.value);
    myObject.increment(40);
    print("After incrementing by 40 = " + myObject.value);
 
    // 'incrementFunc' can be used in any number of objects, e.g.:
    var myObject2 = {
        value : 1000,
        increment : incrementFunc
    };
 
    print("My object 2");
    print("Initial value = " + myObject2.value);
    myObject2.increment();
    print("After incrementing by default amount = " + myObject2.value);
    myObject2.increment(40);
    print("After incrementing by 40 = " + myObject2.value);
}
 
/******************************
 * 2: FUNCTION INVOCATION     *
 ******************************/
function add(a, b) { return a+b; }
 
function functionInvocationTest()
{
    print("Function invocation test...");
 
    // Compare this definition of myObject
    // to myObject in example above.
    var myObject = {
        value : 0,
        increment : function() {
            incrementFunc(); // WON'T WORK because the
            // function's 'this' will be bound to the 'global' object,
            // not to 'myObject'.
        }
    };
 
    print("Initial value = " + myObject.value);
    myObject.increment(); // WON'T WORK
    print("After incrementing by default amount = " + myObject.value);
    myObject.increment(40);
    print("After incrementing by 40 = " + myObject.value);
 
    // When a function is not the property of an object,
    // then it is invoked as a function:
    var sum = add(3,4);
    // When a function is invoked like this, 'this'
    // is bound to the 'global' object.
    // This is a design mistake. Would've been better if 'this'
    // of inner function was bound to the 'this' variable
    // of the outer function.   Hence an inner function to a method
    // does not share the method's access to the object via 'this'.
    myObject.double_broken = function() { // Broken version of the function
        var helper = function() {
            // Helper function's 'this' points to 'global' object,
            // NOT to 'myObject'
            this.value = add(this.value, this.value);
        }
        helper(); // WON'T WORK!
    };
 
    print("Setting myObject.value = 1");
    myObject.value = 1;
    myObject.double_broken();
    print("After attemping to double, using broken function = " + myObject.value);
 
    // work around.  Takes advantage of 'closure'
    // where inner function has access to out function's variables (EXCEPT 'this'):
    myObject.double_works = function() { // Broken version of the function
        var that = this; // Create a local variable
        var helper = function() {
            // 'helper()' has access to 'that'
            // because of JavaScript's 'closure'
            that.value = add(that.value, that.value);
        }
        helper();
    };
 
    myObject.double_works();
    print("After attemping to double, using working function = " + myObject.value);
 
}
 
 
/******************************
 * 3: CONSTRUCTOR INVOCATION  *
 ******************************/
 
function constructorInvocationTest()
{
    // Constructor
    var Quo = function(string) {
        this.status = string;
    }
}
 
/******************************
 *    MAIN FUNCTION           *
 ******************************/
 
window.onload = function()
{
//    methodInvocationTest();    
    functionInvocationTest();
    print("Done");
}
```

</div>

