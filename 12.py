"""INTEGERS TO ROMAN NUMBERS

Roman Numbers are represented by seven different symbol

I, V, X, L, C, D and M


Symbol       Value

I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example 2 is written as II in Roman numeral, Just two one's are added together. 12 is written as XII, which is simply X + II.
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead,
the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the
number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.

X can be placed before L (50) and C (100) to make 40 and 90.

C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer Convert it to a roman numeral"""


"""Solution

Edge cases notations

1  4  5 9  10 40 50 90 100 400 500 900 1000
I  IV V  IX  X  XL L  XC C  CD D  CM M

[
    (1000, "M"), 
    (900, "CM"), 
    (500, "D"), 
    (400, "CD"), 
    (100, "C"), 
    (90, "XC"), 
    (50, "L"), 
    (40, "XL"), 
    (10, "X"), 
    (9, "IX"), 
    (5, "V"), 
    (4, "IV"), 
    (1, "I")
]


Method 1: The subtraction method

Given a number say 4579  we can start with the highest annotation and subtract it until the annotation value is greater than our 
holding number thus moving to the next annotation this process should go in until our holding number is zero


4579 - 1000 = 3579

Annotation = M

3579 - 1000  = 2579

Annotation = MM

2579 - 1000 = 1579

Annotation = MMM

1579 - 1000 = 579

Annotation = MMMM

579 - 500 = 79

Annotation = MMMMD

79 - 50 = 29

Annotation = MMMMDL

29 - 10 = 19    

Annotattion = MMMMDLX

19 - 10 = 9 

Annotation = MMMMDLXX

9 - 5 = 4

Annotation = MMMMDLXXV

4 - 4 = 0

Annotation = MMMMDLXXVIV


METHOD 2: THE DIVISION METHOD

4579 // 1000 = 4

Annotation = MMMM reminder = 579

579 // 500 = 1

Annotation  = MMMMD reminder = 79

79 // 50 = 1

Annotation = MMMMDL reminder = 29

29 // 10 = 2

Annotation = MMMMDLX reminder = 9

9 // 5 = 1

Annotation = MMMMDLXV reminder = 4

4 // 4 = 1

Annotation = MMMMDLXVIV reminder = 0

"""


def solution_Method1(n:int)-> str:

    Annotations = [

        (1000, "M"), 
        (900, "CM"), 
        (500, "D"), 
        (400, "CD"), 
        (100, "C"), 
        (90, "XC"), 
        (50, "L"), 
        (40, "XL"), 
        (10, "X"), 
        (9, "IX"), 
        (5, "V"), 
        (4, "IV"), 
        (1, "I")
    ]
    
    holding = n 

    roman = ""

    current_annotation = 0

    while holding > 0 :

        if holding >= Annotations[current_annotation][0] :

            roman += Annotations[current_annotation][1]

            holding -= Annotations[current_annotation][0]

            print(roman)

        else:

            current_annotation += 1

            continue
        
        print(current_annotation)

    return  roman


def solution_Method2(n: int) -> str:

    Annotations = [

        (1000, "M"), 
        (900, "CM"), 
        (500, "D"), 
        (400, "CD"), 
        (100, "C"), 
        (90, "XC"), 
        (50, "L"), 
        (40, "XL"), 
        (10, "X"), 
        (9, "IX"), 
        (5, "V"), 
        (4, "IV"), 
        (1, "I")
    ]

    holding = n

    roman = ""

    current_annotation = 0

    while holding > 0:

        if holding >= Annotations[current_annotation][0]:

            multiplier = holding // Annotations[current_annotation][0]

            roman += Annotations[current_annotation][1] * multiplier

            holding  = holding % Annotations[current_annotation][0]

            print(roman)

        else:

            current_annotation += 1

            continue
        print(current_annotation)
    return roman

print("using the Divition Method")
print(solution_Method2(4579))
print("using the Subtraction method")
print(solution_Method1(4579))