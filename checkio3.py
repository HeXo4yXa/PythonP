FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] 
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    #FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] 
    #SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    #OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    #HUNDRED = ["hundred"]
    def fso(number):
        if number < 10:
            return FIRST_TEN[number]
        if 10<= number <20:
            return SECOND_TEN[number-10]
        if 20<= number <=99:
            if number%10==0:
                return OTHER_TENS[number/10-2]
            else:
                return OTHER_TENS[number/10-2] +' '+ FIRST_TEN[number%10]
    if 0<= number <=99:
        return fso(number)

    if 100<= number <= 999:
        if number%100==0:
            return fso(number/100) + " hundred"
        else:
            return fso(number/100) + " hundred " + fso(number%100)

if __name__ == '__main__':
    for i in range(1000):
        print checkio(i)

