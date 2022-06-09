from datetime import datetime
startTime = datetime.now()

nine = len('onetwothreefourfivesixseveneightnine')
nineteen = nine + len('teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen')
ninety9 = nineteen + 10 * len('twentythirtyfortyfiftysixtyseventyeightyninety') + 8 * nine
thousand = (10 * ninety9) + (9 * 99 * len('and')) + 100 * (nine + 9 * len('hundred')) + len('onethousand')

#thousand = ninety9 + 100 * len('onehundredtwohundredthreehundred...ninehundred')
#100 * (nine + 9*len('hundred')) + 9 * 99 * len('and') + 9*ninety9 +1

print(thousand)

print(datetime.now() - startTime)
