'''
Operators
Operators are the constructs, which can manipulate the value of operands. Consider the expression 4 + 5 = 9.
# Here, 4 and 5 are called operands and + is called the operator.

Types of Operator

1.  Arithmetic operators
2.  Assignment operators
3.  Comparison (Relational) Operators
4.  logical operator
5.  identity operator
6.  Membership operator
7.  bitwise operator

Python Arithmetic Operators
Assume variable a holds the value 10 and variable b holds the value 21, then-

Operators and their description:-

+ Addition
Adds values on either side of the operator.

example:-

a + b = 31

- Subtraction
Subtracts right hand operand from left hand operand.

example:-

a - b = -11

* Multiplication
Multiplies values on either side of the operator

example:-

a * b = 210

/ Division
Divides left hand operand by right hand operand

example:-

b / a = 2.1

% Modulus
Divides left hand operand by right hand operand and returns remainder

example:-

b%a=1

** Exponent
Performs exponential (power) calculation on operators

example:-

a**b =10 to the power 20

//
Floor Division - The division of operands where the result is the quotient in which the digits after the decimal point are removed.

example:-

9//2 = 4 and 9.0//2.0 = 4.0

Python Comparison Operators
These operators compare the values on either side of them and decide the relation among them. They are also called Relational operators.

Assume variable a holds the value 10 and variable b holds the value 20, then-

==
If the values of two operands are equal, then the condition becomes true.

example:-

(a == b) is not true.

!=
If values of two operands are not equal, then condition becomes true.

example:-

(a!= b) is true.

>
If the value of left operand is greater than the value of right operand, then condition becomes true.

example:-

(a > b) is not true.

<
If the value of left operand is less than the value of right operand, then condition becomes true.

example:-

(a < b) is true.

>=
If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.

example:-

(a >= b) is not true.

<=
If the value of left operand is less than or equal to the value of right operand, then condition becomes true.

example:-

(a <= b) is true.

Python Assignment Operators
Assume variable a holds 10 and variable b holds 20, then-

=
Assigns values from right side operands to left side operand

example:-

c = a + b assigns value of a + b into c

+= Add AND
It adds right operand to the left operand and assign the result to left operand

example:-

c += a is equivalent to c = c + a

-= Subtract AND
It subtracts right operand from the left operand and assign the result to left operand

example:-

c -= a is equivalent to c = c - a

*= Multiply AND
It multiplies right operand with the left operand and assign the result to left operand

example:-

c *= a is equivalent to c = c * a

/= Divide AND
It divides left operand with the right operand and assign the result to left operand

example:-

c /= a is equivalent to c = c / ac /= a is equivalent to c = c / a

%= Modulus AND
It takes modulus using two operands and assign the result to left operand

example:-

c %= a is equivalent to c = c % a

**= Exponent AND
Performs exponential (power) calculation on operators and assign value to the left operand

example:-

c **= a is equivalent to c = c ** a

//= Floor Division
It performs floor division on operators and assign value to the left operand

example:-

c //= a is equivalent to c = c // a

Python Bitwise Operators
Bitwise operator works on bits and performs bit-by-bit operation. Assume if a = 60; and b = 13; Now in binary format they will be as follows-

a = 0011 1100

b = 0000 1101

-----------------

a&b = 0000 1100

a|b = 0011 1101

a^b = 0011 0001

~a = 1100 0011

Pyhton's built-in function bin() can be used to obtain binary representation of an integer number.

The following Bitwise operators are supported by Python language-

& Binary AND
Operator copies a bit to the result, if it exists in both operands

example:-

(a & b) (means 0000 1100)

| Binary OR
It copies a bit, if it exists in either operand.

example:-

^ Binary XOR
It copies the bit, if it is set in one operand but not both.

example:-

(a ^ b) = 49 (means 0011 0001)

~ Binary Ones Complement
It is unary and has the effect of 'flipping' bits.

example:-

(~a ) = -61 (means 1100 0011 in 2's complement form due to a signed binary number.

<< Binary Left Shift
The left operand???s value is moved left by the number of bits specified by the right operand.

example:-

a << = 240 (means 1111 0000)

>> Binary Right Shift
The left operand???s value is moved right by the number of bits specified by the right operand.

example:-

a >> = 15 (means 0000 1111)

Python Logical Operators
The following logical operators are supported by Python language. Assume variable a holds True and variable b holds False then-

and Logical AND
If both the operands are true then condition becomes true.

example:-

(a and b) is False.

or Logical OR
If any of the two operands are non-zero then condition becomes true.

example:-

(a or b) is True.

not Logical NOT
Used to reverse the logical state of its operand.

example:-

Not(a and b) is True.

Python Membership Operators
Python???s membership operators test for membership in a sequence, such as strings, lists, or tuples. There are two membership operators as explained below-

in
Evaluates to true, if it finds a variable in the specified sequence and false otherwise.

example:-

x in y, here in results in a 1 if x is a member of sequence y.

not in
Evaluates to true, if it does not find a variable in the specified sequence and false otherwise.

example:-

x not in y, here not in results in a 1 if x is not a member of sequence Y

Python Identity Operators
Identity operators compare the memory locations of two objects. There are two Identity operators as explained below:

is
Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.

example:-

x is y, here is results in 1 if id(x) equals id(y).

is not
Evaluates to false if the variables on either side of the operator point to the same object and true otherwise.

example:-

x is not y, here is not results in 1 if id(x) is not equal to id(y)

Python Operators Precedence
The following table lists all the operators from highest precedence to the lowest.

**
Exponentiation (raise to the power)

~ +-
Ccomplement, unary plus and minus (method names for the last two are +@ and -@)

* / % //
Multiply, divide, modulo and floor division

+-
Addition and subtraction

>> <<
Right and left bitwise shift

&
Bitwise 'AND'

^|
Bitwise exclusive `OR' and regular `OR'

<= < > >=
Comparison operators

<> == !=
Equality operators

= %= /= //= -= += *= **=
Assignment operators

is is not
Identity operators

in not in
Membership operators

not or and
Logical operators
'''
x = 20.21
y = str(x)
print(y)