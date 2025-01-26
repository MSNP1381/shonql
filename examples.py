examples = [
    """
# Simple variable assignment
x = 42;
name = "John";
""",
    """
# Basic function calls and storing results
result = add(5, 3);
greeting = makeGreeting("John");
print(greeting);""",
    """# Using function results in other functions
num1 = getValue();
doubled = multiply(num1, 2);
result = add(doubled, 5);
print(result);""",
"""# Nested function calls without intermediate variables
result = add(
    multiply(getValue(), 2),
    subtract(10, 5)
);
print(result);

message = concat(
    makeGreeting(getName()),
    "! How are you?"
);""",
"""# Complex composition of functions and variables
firstName = getName();
lastName = getLastName();
age = getAge();

fullName = concat(firstName, concat(" ", lastName));
greeting = makeGreeting(fullName);

isAdult = greaterThan(age, 18);
message = conditionalSelect(
    isAdult,
    concat(greeting, " Welcome to the adult section!"),
    concat(greeting, " Sorry, adults only.")
);

print(message);"""
]
