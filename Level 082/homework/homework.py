# 2
i = 1
sum = 0
while i <= 10:
    sum += i
    i += 1
print(sum)

i = 10
while i >= 1:
    print(i)
    i -= 1


i = -1
sum = 0
while i >= -10:
    sum += i
    i -= 1
print(sum)

i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

i = 1
while i <= 100:
    print(i)
    i += 1

sum = 0
for i in range(1, 11):
    sum += i
print(sum)

for i in range(10, 0, -1):
    print(i)

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

sum = 0
for i in range(1, 101):
    sum += i
print(sum)

values = [2, 4, 6, 8, 10]
for value in values:
    print(value)

num = 5
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

age = 20
if age >= 18:
    print("Adult")
else:
    print("Minor")

score = 85
if score >= 90:
    print("Excellent")
elif score >= 75:
    print("Good")
else:
    print("Needs Improvement")

a = 10
b = 20
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")

name = "Alice"
if name == "Alice":
    print("Welcome Alice!")
else:
    print("You are not Alice.")



# 3) 
def getNumbers(start, end):
    numbers = []
    for i in range(start, end + 1):
        numbers.append(i)
    return numbers

# 4) 
def calculateAverage(numbers):
    return sum(numbers) / len(numbers)

# 5) 

'''
<form id="myForm">
  <input type="text" id="name" placeholder="Name">
  <input type="email" id="email" placeholder="Email">
  <input type="password" id="password" placeholder="Password">
  <button type="submit">Submit</button>
</form>

<script>
  const dataBase = [];

  document.getElementById('myForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    for (let i = 0; i < dataBase.length; i++) {
      if (dataBase[i].email === email) {
        alert('Account already exists');
        return;
      }
    }

    dataBase.push({ name: name, email: email, password: password });
    alert('Account created successfully');
  });
</script>
'''
