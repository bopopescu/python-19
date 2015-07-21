#---------------------------------------------------------
# April Dawn Kester
# akester@ischool.berkeley.edu
# Homework #11 WOOT!!!
# November 24, 2014
# Functional programming
# Script 3
#---------------------------------------------------------

answerString = None

def maxPath(triangle):
    myList = triangle[-1]
    global answerString
    answerString = str(max(myList))
    
    while len(triangle) > 1:
        x = triangle.pop()
        y = triangle.pop()
        triangle.append([max(x[i], x[i+1]) + t for i,t in enumerate(y)])

        answerString += " + "
        answerString += str(t)

    return triangle[0][0]

def main():
    filename = "maxtriangle2.txt"
    try:
        with open(filename, mode="U") as file:
            data = file.read()
        file.close()
    except IOError:
        print "Can not open", filename
        print "Goodbye!"
        sys.exit()

    total = str(maxPath([map(int, row.split()) for row in data.splitlines()]))
    global answerString
    answerString += " = "
    answerString += total
    print answerString

if __name__ == "__main__":
    main()