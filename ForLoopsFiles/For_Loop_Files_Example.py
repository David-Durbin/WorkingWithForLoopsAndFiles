def main():
    ttl = 0.0 # total variable
    cnt = 0  # counting variable

    infile = open("numbers.txt", 'r')

    for line in infile:
        # read the next line in the file, however this is redundant as we are doing the by interating down each line
        # using the for loop.
        line = infile.readline()
        ttl += int(line)
        cnt += 1

    # close the file
    infile.close()

    # print all results
    print('There were', cnt, 'numbers in the file.')
    print('The total of those numbers is', format(ttl, ',.2f'))
    print('The average of the numbers is', format(ttl/cnt, ',.2f'))



main()
