# Week 10 - Testing

## Testing Pyramid

![A pyramid with 3 sections. The bottom is "unit", the middle is "service" and the top is "UI".](/img/testing_pyramid.png)

further reading: [The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)

## Test execution: Arrange, Act, Assert

### 1. Arrange

- create objects
- setup mocks
- what's the expected output?

### 2. Act

invoke system under test

### 3. Assert

- check expected and actual behavior
- give feedback

## Test naming strategies

### a.) 'System under test' - 'Behavior' - 'Condition'

```javascript
function authentication_rejectsUser_badCredentialsProvided()
```

### b.) 'Given' - 'When' - 'Then'

```javascript
function badCredentials_authenticate_rejectUser()
```

## Tasks

<details>

<summary>whole class</summary>

You can easily code along the following tasks at [online-python.com](https://www.online-python.com/).

<details>

<summary>test cases</summary>

```python
def is_within_range(number, lower, upper):
    return lower <= number <= upper
```

Think about unit tests for the function above. Cover different scenarios and edge cases.

</details>

<details>

<summary>bug hunt</summary>

```python
def calculate_sales_tax(products):
    tax_rates = {'low': 0.07, 'high': 0.19}
    total_tax = 0
    for product in products:
        if product['category'] == 'low':
            total_tax += product['price'] * tax_rates['low']
        else:
            total_tax = product['price'] * tax_rates['high']
    return total_tax
```

<details>

<summary>bugs</summary>

- total_tax in `else` branch newly assigned
- return value with more than 2 decimal places
- product with category `no_tax`
- product with category `Low` (upper-case `L`)
- products with missing `category` or `price`

</details>

</details>

</details>

<details>

<summary>in your group</summary>

- write 5 unit tests for your existing code

    - Test Runners:
        - Java/Kotlin: [JUnit](https://junit.org)
        - JavaScript: [Jest](https://jestjs.io/)
        - Python: [unittest](https://docs.python.org/3/library/unittest.html)

- write 1 unit test using [Test-driven development](https://en.wikipedia.org/wiki/Test-driven_development), i.e.

    1. write a new test that is failing
    2. change the code so that all existing tests succeed
    3. refactor the code as needed

</details>

## Checks for Understanding

<details>

<summary>expand</summary>

- How would you argue against the statement of "Average Engineer" below:

    ![Screenshot of a code review communication. One participants states "I'm merging it. Fuck the tests.". Another comments: "Writing testcases for your code is doubting your own coding abilities. It's a sign of weakness.](/img/f_the_tests.webp)

- In terms of testing, what is a takeaway of this statement:

    ![Screenshot of a microblogging post about a guy that likes to add unusual symbols to online forms because they know that some developer is going to see it and wonder if they have a bug.](/img/encoding_evil.webp)

</details>