import fibo

fibo.fib(1000)

value = input('What shall I write to file? : ')
f = open('output.txt', 'w')
f.write(value + '\n')