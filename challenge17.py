def numtowordslength(num):
    units = ["","one","two","three","four","five","six","seven","eight","nine"]
    teens = ["","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    tens = ["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    thousands = ["","thousand"]

    if num == 0:
        words.append("zero")

    else:
        if len(num) == 1:
            return len(units[num])
        elif len(num) == 2:
            if num <= 19 and num >= 11:
                return len(teens(num))
        elif len(num) == 3:

        else:
