rectangle1Length = float(input('Please enter the length of rectangle 1: '))
rectangle1Width = float (input('Please enter the width of rectangle 1: '))
rectangle2Length = float ( input('Please enter the length of rectangle 2: '))
rectangle2Width = float ( input('Please enter the width of rectangle 2: '))
rectangle1Area = rectangle1Length * rectangle1Width
rectangle2Area = rectangle2Length * rectangle2Width
if rectangle1Area > rectangle2Area:
	print( 'Rectangle 1 is bigger than Rectangle 2' )
elif rectangle2Area > rectangle1Area:
	print( 'Rectangle 2 is bigger than Rectangle 1' )
else: 
        print( 'Both rectangles are equal')
