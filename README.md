# Email Validation in Python

## Project Overview

This project implements email validation in Python using two different approaches:

1. Validation using built-in string functions
2. Validation using regular expressions (regex)

**The purpose of this project is to understand:**

- How email validation can be implemented step by step using basic logic
- How the same validation rules can be expressed compactly using regex
- The strengths and limitations of both approaches
- This project is learning-focused and avoids external libraries beyond Python’s standard modules.
---


## Approach 1: Email Validation Using String Functions

This approach validates an email address by applying multiple checks sequentially using Python string methods.

### Validation Rules (String-Based)

The email is considered valid only if all the following conditions are satisfied:

1. Minimum Length
    - Email must contain at least 6 characters.

2. First Character Rule
    - The first character must be an alphabet (a–z or A–Z).

3. @ Symbol Rule
    - Email must contain exactly one @ symbol.

4. Domain Dot (.) Rule
    - A dot (.) must appear either at the 3rd or 4th position from the end (e.g., .com, .in).
    - XOR logic is used to ensure only one valid dot position exists.

5. Character Validation
    - Spaces are not allowed.
    - Uppercase letters are not allowed.
        - This restriction is enforced using isupper() logic.
    - Special characters like #, $, %, &, etc. are not allowed.
    - Allowed characters:
        - Lowercase alphabets (a–z)
        - Digits (0–9)
        - `_`, `.`, `@`

### How the String-Based Program Works

1. Takes email input from the user.
2. Applies validation checks step by step.
3. Uses internal flags to track invalid cases.
4. Displays specific error messages indicating where validation failed.
5. Confirms validity only if all checks pass.

### Sample Outputs (String-Based)

```
Enter an email : 42login@gmail.com
Wrong email 2

Enter an email : login42@gmail.com
Email is valid

Enter an email : login##42@gmail.com
Wrong email 5
```


## Approach 2: Email Validation Using Regular Expressions (Regex)

This approach performs email validation using Python’s built-in `re` module and a single regex pattern that encodes all validation rules.

### Regex Pattern Used

```
^[a-z][a-z0-9]*([._]?[a-z0-9]+)*@[a-z]+\.[a-z]{2,3}$
```

### Explanation of the Regex Logic

1. `^` - Ensures matching starts from the beginning of the string.

2. `[a-z]` - Forces the email to start with a lowercase alphabet.

3. `[a-z0-9]*` - Allows lowercase letters and digits after the first character.

4. `([._]?[a-z0-9]+)*` - Allows at most one . or _ at a time, which must be followed by alphanumeric characters.

5. `@` - Ensures exactly one @ symbol.

6. `[a-z]+` - Matches the domain name using lowercase letters only.

7. `\.` - Matches a literal dot before the domain extension.

8. `[a-z]{2,3}` - Restricts the domain extension to 2 or 3 lowercase letters (e.g., .in, .co, .com).

9. `$` - Ensures matching ends at the end of the string.

### Why re.search() Is Used

- The regex includes both start (^) and end ($) anchors, which already enforce full-string matching.
- Therefore, using re.search() works correctly and behaves equivalently to re.fullmatch() in this case.

### Example Valid Emails

 - pranav01@gmail.com
 - pranav_panjabi01@gmail.com
 - pranav@gmail.co
 - pranav@gmail.in

### Example Invalid Emails

 - 1pranav@gmail.com (starts with digit)
 - Pranav@gmail.com (uppercase letter)
 - pranav_@gmail.com (special character not followed by alphanumeric)
 - pranav@gmail.comm (invalid domain length)

## Limitations

- This project is intended for learning purposes.
- It is not a fully RFC-compliant email validator.
- Some valid real-world email formats may be rejected intentionally.

## Technologies Used

1. Python 3
2. Built-in string methods (isalpha(), isdigit(), isspace(), etc.)
3. `re` module (regular expressions)

## Learning Outcomes

- Understanding character-based validation using string functions
- Writing and debugging regular expressions
- Comparing procedural validation vs pattern-based validation
- Structuring a Python project for GitHub

## References

- Python String Methods (Official Docs):
  https://docs.python.org/3/library/stdtypes.html#string-methods

- Python `re` Module (Official Docs):
  https://docs.python.org/3/library/re.html
