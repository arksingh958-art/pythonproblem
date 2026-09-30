# prime in range 

start = int (input (" enter a start number "))
end = int ( input ( " enter a end number "))

for i in range ( start , end +1):
  if start > 1 :
    count = 0
    for i in range ( 1 , start+ 1):
      if start % i==0:
        count +=1
        if count ==2:
          print(start)
    