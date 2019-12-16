# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

import numpy as np
# Install Pillow and uncomment this line to access image processing.
from PIL import Image, ImageDraw, ImageChops


class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an int representing its
    # answer to the question: 1, 2, 3, 4, 5, or 6. Strings of these ints
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName(). Return a negative number to skip a problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.
    def Solve(self, problem):
        if problem.problemType == '2x2':
            return self.solveProb2x2(problem)
            # return self.solveProb2x2(problem)
        elif problem.problemType == '3x3':
            return self.solveProb3x3(problem)
        return -1

    def solveProb3x3(self, problem):
        figA = Image.open(problem.figures["A"].visualFilename).convert('L').point(lambda x: 0 if x < 128 else 255, '1')
        figB = Image.open(problem.figures["B"].visualFilename).convert('L').point(lambda x: 0 if x < 128 else 255, '1')
        figC = Image.open(problem.figures["C"].visualFilename).convert('L').point(lambda x: 0 if x < 128 else 255, '1')
        figD = Image.open(problem.figures["D"].visualFilename).convert('L').point(lambda x: 0 if x < 128 else 255, '1')
        figE = Image.open(problem.figures["E"].visualFilename).convert('L').point(lambda x: 0 if x < 128 else 255, '1')
        figF = Image.open(problem.figures["F"].visualFilename).convert('L').point(lambda x: 0 if x < 128 else 255, '1')
        figG = Image.open(problem.figures["G"].visualFilename).convert('L').point(lambda x: 0 if x < 128 else 255, '1')
        figH = Image.open(problem.figures["H"].visualFilename).convert('L').point(lambda x: 0 if x < 128 else 255, '1')
        op1 = Image.open(problem.figures["1"].visualFilename).convert('L').point(lambda x: 0 if x < 128 else 255, '1')
        op2 = Image.open(problem.figures["2"].visualFilename).convert('L').point(lambda x: 0 if x < 128 else 255, '1')
        op3 = Image.open(problem.figures["3"].visualFilename).convert('L').point(lambda x: 0 if x < 128 else 255, '1')
        op4 = Image.open(problem.figures["4"].visualFilename).convert('L').point(lambda x: 0 if x < 128 else 255, '1')
        op5 = Image.open(problem.figures["5"].visualFilename).convert('L').point(lambda x: 0 if x < 128 else 255, '1')
        op6 = Image.open(problem.figures["6"].visualFilename).convert('L').point(lambda x: 0 if x < 128 else 255, '1')
        op7 = Image.open(problem.figures["7"].visualFilename).convert('L').point(lambda x: 0 if x < 128 else 255, '1')
        op8 = Image.open(problem.figures["8"].visualFilename).convert('L').point(lambda x: 0 if x < 128 else 255, '1')

        # if problem.figures["A"].visualFilename == "Problems/Basic Problems C/Basic Problem C-09/A.png":
        #     print("Yoyo")
        #     print(self.splitAndCompare(figA, figC))

        print(problem.figures["A"].visualFilename)
        figList = [figA, figB, figC, figD, figE, figF, figG, figH]
        opList = [op1, op2, op3, op4, op5, op6, op7, op8]
        # print(self.darkPixelRatio(figA, figB))
        # print(self.intersectionPixelRatio(figA, figB))
        # for fig in figList:
        #     print(self.darkPixelDensity(fig))
        # for op in opList:
        #     print(self.darkPixelDensity(op))
        # sys.exit()
        finalScoresList = self.listFinalScore3x3(figA, figB, figC, figD, figE, figF, figG, figH, opList)
        print(finalScoresList)
        max_score = max(finalScoresList)
        # print(finalScoresList)
        indexMaxScore = finalScoresList.index(max_score)
        return indexMaxScore + 1

    def listFinalScore3x3(self, figA, figB, figC, figD, figE, figF, figG, figH, opList):
        figADark = self.darkPixelDensity(figA)
        figBDark = self.darkPixelDensity(figB)
        figCDark = self.darkPixelDensity(figC)
        figDDark = self.darkPixelDensity(figD)
        figEDark = self.darkPixelDensity(figE)
        figFDark = self.darkPixelDensity(figF)
        figGDark = self.darkPixelDensity(figG)
        figHDark = self.darkPixelDensity(figH)
        pixelRatioMatrix = [[figADark, figBDark, figCDark], [figDDark, figEDark, figFDark], [figGDark, figHDark, 0]]
        opListDark = []
        for op in opList:
            opListDark.append(self.darkPixelDensity(op))
        print(pixelRatioMatrix)
        print(opListDark)
        ct = 0.1
        cit = 0.6

        score = np.array([0, 0, 0, 0, 0, 0, 0, 0])

        horizontalRelationConstant = False
        horizontalRelationIncreasing = False
        horizontalRelationDecreasing = False

        verticalRelationConstant = False
        verticalRelationIncreasing = False
        verticalRelationDecreasing = False

        print(score)
        if (figBDark - figADark > cit and figCDark - figBDark > cit and figEDark - figDDark > cit and figFDark - figEDark > cit and figHDark - figGDark > cit):
            horizontalRelationIncreasing = True
            tempscore = []
            for opDark in opListDark:
                if opDark - figHDark > cit:
                    tempscore.append(1)
                else:
                    tempscore.append(0)
            print("horizontalRelationIncreasing" + str(tempscore))
            score = score + np.array(tempscore)

        elif (cit < figADark - figBDark and cit < figBDark - figCDark and cit < figDDark - figEDark and cit < figEDark - figFDark and cit < figGDark - figHDark):
            horizontalRelationDecreasing = True
            tempscore = []
            for opDark in opListDark:
                if figHDark - opDark > cit:
                    tempscore.append(1)
                else:
                    tempscore.append(0)
            print("horizontalRelationDecreasing" + str(tempscore))
            score = score + np.array(tempscore)

        elif (abs(figADark - figBDark) < ct and abs(figBDark - figCDark) < ct and abs(figDDark - figEDark) < ct and abs(
                figEDark - figFDark) < ct and abs(figGDark - figHDark) < ct):
            horizontalRelationConstant = True
            tempscore = []
            for opDark in opListDark:
                if abs(figHDark - opDark) < ct:
                    tempscore.append(1)
                else:
                    tempscore.append(0)
            print("horizontalRelationConstant" + str(tempscore))
            score = score + np.array(tempscore)

        if (figDDark - figADark > cit and figGDark - figDDark > cit and figEDark - figBDark > cit and figHDark - figEDark > cit and figFDark - figCDark > cit):
            verticalRelationIncreasing = True
            tempscore = []
            for opDark in opListDark:
                if opDark - figFDark > cit:
                    tempscore.append(1)
                else:
                    tempscore.append(0)
            print("verticalRelationIncreasing" + str(tempscore))
            score = score + np.array(tempscore)
        elif (cit < figADark - figDDark and cit < figDDark - figGDark and cit < figBDark - figEDark and cit < figEDark - figHDark and cit < figCDark - figFDark):
            verticalRelationDecreasing = True
            tempscore = []
            for opDark in opListDark:
                if figFDark - opDark > cit:
                    tempscore.append(1)
                else:
                    tempscore.append(0)
            print("verticalRelationDecreasing" + str(tempscore))
            score = score + np.array(tempscore)
        elif (abs(figADark - figDDark) < ct and abs(figGDark - figDDark) < ct and abs(figEDark - figBDark) < ct and abs(
                figHDark - figEDark) < ct and abs(figFDark - figCDark) < ct):
            verticalRelationConstant = True
            tempscore = []
            for opDark in opListDark:
                if abs(figFDark - opDark) < ct:
                    tempscore.append(1)
                else:
                    tempscore.append(0)
            print("verticalRelationConstant" + str(tempscore))
            score = score + np.array(tempscore)

        print("horizontalRelationConstant:" + str(horizontalRelationConstant))
        print("horizontalRelationIncreasing:" + str(horizontalRelationIncreasing))
        print("horizontalRelationDecreasing:" + str(horizontalRelationDecreasing))
        print("verticalRelationConstant:" + str(verticalRelationConstant))
        print("verticalRelationIncreasing:" + str(verticalRelationIncreasing))
        print("verticalRelationDecreasing:" + str(verticalRelationDecreasing))

        diffImageScore = self.diffImageScorer3x3(figA, figB, figC, figD, figE, figF, figG, figH, opList,
                                                 horizontalRelationIncreasing or horizontalRelationDecreasing, verticalRelationIncreasing or verticalRelationDecreasing)

        darkPixelIncrementScore = self.darkPixelIncrementScorer3x3(figADark,figBDark,figCDark,figDDark,figEDark,figFDark,figGDark,figHDark, opListDark, horizontalRelationIncreasing or horizontalRelationDecreasing, verticalRelationIncreasing or verticalRelationDecreasing)

        if (horizontalRelationConstant == False and horizontalRelationIncreasing == False and horizontalRelationDecreasing == False and verticalRelationConstant == False and verticalRelationIncreasing == False and verticalRelationDecreasing == False):
            return list(np.array(self.checkReflectionPropertyAndScore3x3(figA, figB, figC, figD, figE, figF, figG, figH, opList)) + np.array(self.splitAndCompareScorer(figA, figB, figC, figD, figE, figF, figG, figH, opList)))

        return list(5*score + 5*np.array(diffImageScore) + np.array(darkPixelIncrementScore))

    def darkPixelIncrementScorer3x3(self, figADark,figBDark,figCDark,figDDark,figEDark,figFDark,figGDark,figHDark, opListDark, horizontalRelationIncreasingOrDecreasing, verticalRelationIncreaingOrDecreasing):
        ct = 0.2
        score = np.array([0, 0, 0, 0, 0, 0, 0, 0])
        if (horizontalRelationIncreasingOrDecreasing):
            diffGHDark = abs(figGDark - figHDark)
            tempScore = []
            for opDark in opListDark:
                diffOpHDark = abs(figHDark - opDark)
                if(abs(diffOpHDark-diffGHDark)<ct):
                    tempScore.append(1)
                else:
                    tempScore.append(0)
            score = score + np.array(tempScore)

        if (verticalRelationIncreaingOrDecreasing):
            diffCFDark = abs(figCDark - figFDark)
            tempScore = []
            for opDark in opListDark:
                diffOpFDark = abs(figFDark - opDark)
                if(abs(diffOpFDark-diffCFDark)<ct):
                    tempScore.append(1)
                else:
                    tempScore.append(0)
            score = score + np.array(tempScore)

        print("darkPixelIncrementScorer3x3:" + str(score))

        return list(score)

    def splitAndCompareScorer(self, figA, figB, figC, figD, figE, figF, figG, figH, opList):
        score = []
        if (self.splitAndCompare(figA, figC) and self.splitAndCompare(figD, figF)):
            for op in opList:
                if(self.splitAndCompare(figG, op)):
                    score.append(1)
                else:
                    score.append(0)
            return score

        return [0,0,0,0,0,0,0,0]


    def splitAndCompare(self, image1, image2):
        ct = 0.1
        widthImage1, heightImage1 = image1.size
        leftImage1 = image1.crop((0, 0, widthImage1/2, heightImage1))
        rightImage1 = image1.crop((widthImage1/2, 0, widthImage1, heightImage1))

        widthImage2, heightImage2 = image2.size
        leftImage2 = image2.crop((0, 0, widthImage2/2, heightImage2))
        rightImage2 = image2.crop((widthImage2/2, 0, widthImage2, heightImage2))

        return self.isEqualImages(leftImage1, rightImage2, ct) and self.isEqualImages(leftImage2, rightImage1, ct)

    def diffImageScorer3x3(self, figA, figB, figC, figD, figE, figF, figG, figH, opList, horizontalRelationIncreasingOrDecreasing, verticalRelationIncreaingOrDecreasing):
        score = np.array([0,0,0,0,0,0,0,0])
        ct = 1
        print("Entered diffImageScorer3x3")
        if (horizontalRelationIncreasingOrDecreasing):
            diffAB = ImageChops.difference(figA, figB)
            diffBC = ImageChops.difference(figB, figC)
            diffDE = ImageChops.difference(figD, figE)
            diffEF = ImageChops.difference(figE, figF)
            diffGH = ImageChops.difference(figG, figH)

            diffABDark = self.darkPixelDensity(diffAB)
            diffBCDark = self.darkPixelDensity(diffBC)
            diffDEDark = self.darkPixelDensity(diffDE)
            diffEFDark = self.darkPixelDensity(diffEF)
            diffGHDark = self.darkPixelDensity(diffGH)

            print("diffABDark" + str(diffABDark))
            print("diffBCDark" + str(diffBCDark))
            print("diffDEDark" + str(diffDEDark))
            print("diffEFDark" + str(diffEFDark))
            print("diffGHDark" + str(diffGHDark))

            tempScore = []

            if (abs(diffABDark-diffBCDark)<ct and abs(diffDEDark-diffEFDark)<ct):
                for op in opList:
                    diffOpH = ImageChops.difference(figH, op)
                    diffOpHDark = self.darkPixelDensity(diffOpH)
                    if (abs(diffGHDark-diffOpHDark)<ct):
                        tempScore.append(1)
                    else:
                        tempScore.append(0)

                score = score + np.array(tempScore)

        if (verticalRelationIncreaingOrDecreasing):
            diffAD = ImageChops.difference(figA, figD)
            diffBE = ImageChops.difference(figB, figE)
            diffCF = ImageChops.difference(figC, figF)
            diffDG = ImageChops.difference(figD, figG)
            diffEH = ImageChops.difference(figE, figH)

            diffADDark = self.darkPixelDensity(diffAD)
            diffBEDark = self.darkPixelDensity(diffBE)
            diffCFDark = self.darkPixelDensity(diffCF)
            diffDGDark = self.darkPixelDensity(diffDG)
            diffEHDark = self.darkPixelDensity(diffEH)

            print("diffABDark" + str(diffADDark))
            print("diffBCDark" + str(diffBEDark))
            print("diffDEDark" + str(diffCFDark))
            print("diffEFDark" + str(diffDGDark))
            print("diffGHDark" + str(diffEHDark))

            tempScore = []

            if (abs(diffADDark-diffDGDark)<ct and abs(diffBEDark-diffEHDark)<ct):
                for op in opList:
                    diffOpF = ImageChops.difference(figF, op)
                    diffOpFDark = self.darkPixelDensity(diffOpF)
                    if (abs(diffCFDark-diffOpFDark)<ct):
                        tempScore.append(1)
                    else:
                        tempScore.append(0)

                score = score + np.array(tempScore)

        print("diffImageScorer3x3:"+str(score))
        return list(score)

    def checkReflectionPropertyAndScore3x3(self, figA, figB, figC, figD, figE, figF, figG, figH, opList):
        mirrorFigALeftRight = figA.transpose(Image.FLIP_LEFT_RIGHT)
        mirrorFigDLeftRight = figD.transpose(Image.FLIP_LEFT_RIGHT)
        mirrorFigGLeftRight = figG.transpose(Image.FLIP_LEFT_RIGHT)
        mirrorFigATopDown = figA.transpose(Image.FLIP_TOP_BOTTOM)
        mirrorFigBTopDown = figB.transpose(Image.FLIP_TOP_BOTTOM)
        mirrorFigCTopDown = figC.transpose(Image.FLIP_TOP_BOTTOM)
        ct = 0.07

        isReflectionRelationAC = self.isEqualImages(mirrorFigALeftRight, figC, ct)
        isReflectionRelationDF = self.isEqualImages(mirrorFigDLeftRight, figF, ct)
        isReflectionRelationAG = self.isEqualImages(mirrorFigATopDown, figG, ct)
        isReflectionRelationBH = self.isEqualImages(mirrorFigBTopDown, figH, ct)

        reflectionScoreList = []
        if (isReflectionRelationAC and isReflectionRelationDF and isReflectionRelationAG and isReflectionRelationBH):
            for op in opList:
                if self.isEqualImages(op, mirrorFigGLeftRight, ct) and self.isEqualImages(op, mirrorFigCTopDown, ct):
                    reflectionScoreList.append(1)
                else:
                    reflectionScoreList.append(0)
            return reflectionScoreList
        return [0,0,0,0,0,0,0,0]

    def darkPixelDensity(self, image):
        countBlackPixelImage = 1
        for pixel in image.getdata():
            if pixel == (0):
                countBlackPixelImage += 1
        return countBlackPixelImage * 100.00 / len(list(image.getdata()))

    def intersectionPixelRatio(self, image1, image2):
        lenList = len(list(image1.getdata()))
        listImage1 = list(image1.getdata())
        listImage2 = list(image2.getdata())

        countIntersectionDarkPixel = 1
        for i in range(lenList):
            if listImage1[i] == 0 and listImage2[i] == 0:
                countIntersectionDarkPixel += 1
        return countIntersectionDarkPixel * 100.00 / (lenList)

    def solveProb2x2(self, problem):
        # print(problem.figures["A"].visualFilename)
        figA = Image.open(problem.figures["A"].visualFilename).convert('L').point(lambda x: 0 if x < 128 else 255, '1')
        figB = Image.open(problem.figures["B"].visualFilename).convert('L').point(lambda x: 0 if x < 128 else 255, '1')
        figC = Image.open(problem.figures["C"].visualFilename).convert('L').point(lambda x: 0 if x < 128 else 255, '1')
        op1 = Image.open(problem.figures["1"].visualFilename).convert('L').point(lambda x: 0 if x < 128 else 255, '1')
        op2 = Image.open(problem.figures["2"].visualFilename).convert('L').point(lambda x: 0 if x < 128 else 255, '1')
        op3 = Image.open(problem.figures["3"].visualFilename).convert('L').point(lambda x: 0 if x < 128 else 255, '1')
        op4 = Image.open(problem.figures["4"].visualFilename).convert('L').point(lambda x: 0 if x < 128 else 255, '1')
        op5 = Image.open(problem.figures["5"].visualFilename).convert('L').point(lambda x: 0 if x < 128 else 255, '1')
        op6 = Image.open(problem.figures["6"].visualFilename).convert('L').point(lambda x: 0 if x < 128 else 255, '1')

        opList = [op1, op2, op3, op4, op5, op6]

        finalScoresList = self.listFinalScore(figA, figB, figC, opList)
        # print(finalScoresList)
        max_score = max(finalScoresList)
        indexMaxScore = finalScoresList.index(max_score)
        # print("option chosen: " + str(indexMaxScore + 1))
        return indexMaxScore + 1

    def listFinalScore(self, figA, figB, figC, opList):
        mode = self.decideComparisonMode(figA, figB, figC)
        # print("mode = " + str(mode))
        rotationScore = [0, 0, 0, 0]
        reflectionScore = [0, 0, 0, 0]
        pixelRatioScore = [0, 0, 0, 0]
        if mode == 0:
            rotationScore = np.array(self.scoreRotation(figA, figB, figC, opList)) + np.array(
                self.scoreRotation(figA, figC, figB, opList) + np.array(self.scoreRotation(figB, figC, figA, opList)))
            reflectionScore = np.array(self.scoreReflection(figA, figB, figC, opList)) + np.array(
                self.scoreReflection(figA, figC, figB, opList) + np.array(
                    self.scoreReflection(figB, figC, figA, opList)))
            pixelRatioScore = np.array(self.scorerPixelColor(figB, opList)) + np.array(
                self.scorerPixelColor(figC, opList) + np.array(self.scorerPixelColor(figA, opList)))

        elif mode == 1:
            rotationScore = np.array(self.scoreRotation(figA, figB, figC, opList)) + np.array(
                self.scoreRotation(figB, figC, figA, opList))
            reflectionScore = np.array(self.scoreReflection(figA, figB, figC, opList)) + np.array(
                self.scoreReflection(figB, figC, figA, opList))
            pixelRatioScore = np.array(self.scorerPixelColor(figC, opList)) + np.array(
                self.scorerPixelColor(figA, opList))

        elif mode == 2:
            rotationScore = np.array(self.scoreRotation(figA, figC, figB, opList)) + np.array(
                self.scoreRotation(figB, figC, figA, opList))
            reflectionScore = np.array(self.scoreReflection(figA, figC, figB, opList)) + np.array(
                self.scoreReflection(figB, figC, figA, opList))
            pixelRatioScore = np.array(self.scorerPixelColor(figB, opList)) + np.array(
                self.scorerPixelColor(figA, opList))

        elif mode == 3:
            rotationScore = np.array(self.scoreRotation(figA, figB, figC, opList)) + np.array(
                self.scoreRotation(figA, figC, figB, opList))
            reflectionScore = np.array(self.scoreReflection(figA, figB, figC, opList)) + np.array(
                self.scoreReflection(figA, figC, figB, opList))
            pixelRatioScore = np.array(self.scorerPixelColor(figB, opList)) + np.array(
                self.scorerPixelColor(figC, opList))
        elif mode == 4:
            rotationScore = np.array(self.scoreRotation(figA, figB, figC, opList))
            reflectionScore = np.array(self.scoreReflection(figA, figB, figC, opList))
            pixelRatioScore = np.array(self.scorerPixelColor(figC, opList))
        elif mode == 5:
            rotationScore = np.array(self.scoreRotation(figA, figC, figB, opList))
            reflectionScore = np.array(self.scoreReflection(figA, figC, figB, opList))
            pixelRatioScore = np.array(self.scorerPixelColor(figB, opList))
        elif mode == -1:
            return list(
                np.array(self.hitAndTry(figA, figB, figC, opList)) + np.array(self.hitAndTry(figA, figC, figB, opList)))

        # print("rotationScore:" + str(rotationScore))
        # print("reflectionScore: " + str(reflectionScore))
        return list(rotationScore + 16 * reflectionScore + 64 * pixelRatioScore)

    def decideComparisonMode(self, figA, figB, figC):
        compareAB = self.equalPixelDensity(figA, figB)
        compareAC = self.equalPixelDensity(figA, figC)
        compareBC = self.equalPixelDensity(figB, figC)
        if compareAB and compareAC and compareBC:
            return 0
        if compareAB and compareBC:
            return 1
        if compareAC and compareBC:
            return 2
        if compareAB and compareAC:
            return 3
        if compareAB:
            return 4
        if compareAC:
            return 5
        return -1

    def scorerPixelColor(self, fig, opList):
        scoresPixelList = []
        for op in opList:
            if self.equalPixelDensity(fig, op):
                scoresPixelList.append(1)
            else:
                scoresPixelList.append(0)
        return scoresPixelList

    def equalPixelDensity(self, image1, image2):
        image1Density = self.ratioOfWhiteToDarkPixel(image1)
        image2Density = self.ratioOfWhiteToDarkPixel(image2)
        return abs(image1Density - image2Density) < 1

    def scoreRotation(self, figA, figB, figC, opList):
        rots = []
        for x in range(0, 360, 90):
            if self.isEqualImages(figA.rotate(x), figB, 0.07):
                rots.append(x)

        # print ("rotation: " + str(rots))
        if not rots:
            return [0, 0, 0, 0, 0, 0]

        rotationScoreList = [0, 0, 0, 0, 0, 0]
        for rot in rots:
            differenceMetric = []
            eachRotationScoreList = []
            for op in opList:
                differenceMetric.append(self.differenceImagesMetric(figC.rotate(rot), op))

            minValue = min(differenceMetric)
            minIndex = differenceMetric.index(minValue)

            i = 0
            for op in opList:
                if (i == minIndex):
                    eachRotationScoreList.append(1)
                else:
                    eachRotationScoreList.append(0)
                i = i + 1
            rotationScoreList = list(np.array(rotationScoreList) + np.array(eachRotationScoreList))

        return rotationScoreList

    def scoreReflection(self, figA, figB, figC, opList):
        scoreLeftRight = np.array(self.scoreLeftRightTopDownReflection(figA, figB, figC, opList, Image.FLIP_LEFT_RIGHT))
        # print("scoreLeftRight: " + str(scoreLeftRight))
        scoreTopDown = np.array(self.scoreLeftRightTopDownReflection(figA, figB, figC, opList, Image.FLIP_TOP_BOTTOM))
        # print("scoreTopDown: " + str(scoreTopDown))
        return list(scoreLeftRight + scoreTopDown)

    def scoreLeftRightTopDownReflection(self, figA, figB, figC, opList, transpose):
        mirrorFigA = figA.transpose(transpose)

        if not self.isEqualImages(mirrorFigA, figB, 0.05):
            return [0, 0, 0, 0, 0, 0]

        mirrorLeftRightFigC = figC.transpose(transpose)

        leftRightReflectionScoreList = []
        differenceMetric = []
        for op in opList:
            differenceMetric.append(self.differenceImagesMetric(mirrorLeftRightFigC, op))

        # print("differenceMetricReflection: " + str(transpose) + " " + str(differenceMetric))
        minValue = min(differenceMetric)
        minIndex = differenceMetric.index(minValue)

        i = 0
        for op in opList:
            if (i == minIndex):
                leftRightReflectionScoreList.append(1)
            else:
                leftRightReflectionScoreList.append(0)
            i = i + 1

        # print(leftRightReflectionScoreList)
        return leftRightReflectionScoreList

    def isEqualImages(self, image1, image2, threshold):
        return self.differenceImagesMetric(image1, image2) < threshold

    def differenceImagesMetric(self, image1, image2):
        diff = ImageChops.difference(image1, image2)
        return self.ratioOfWhiteToDarkPixel(diff)

    def ratioOfWhiteToDarkPixel(self, image):
        blackPixel = 1
        whitePixel = 1
        for pixel in image.getdata():
            if pixel == (0):
                blackPixel += 1
            else:
                whitePixel += 1
        # print(whitePixel/float(blackPixel))
        return whitePixel / float(blackPixel)

    def hitAndTry(self, figA, figB, figC, opList):
        # return self.diffOfDiffImages(figA, figB, figC, opList)
        # print("fill and score: " + str(self.fillImageAndScore(figA, figB, figC, opList)))
        return list(np.array(self.diffOfDiffImages(figA, figB, figC, opList))
                    + np.array(self.fillImageAndScore(figA, figB, figC, opList)))

    def diffOfDiffImages(self, figA, figB, figC, opList):
        diffAB = ImageChops.difference(figA, figB)
        diffOfDiffList = []
        for op in opList:
            diffCOp = ImageChops.difference(figC, op)
            if self.isEqualImages(diffAB, diffCOp, 0.037):
                diffOfDiffList.append(1)
            else:
                diffOfDiffList.append(0)
        return diffOfDiffList

    # def imageAddAndCompare(self, figA, figB):
    #     result = Image.alpha_composite(figA, figB)
    #     result.show()
    #     sys.exit()

    def fillImageAndScore(self, figA, figB, figC, opList):
        figACopy = figA.copy()
        figBCopy = figB.copy()
        figCCopy = figC.copy()
        opListCopy = []
        for op in opList:
            opListCopy.append(op.copy())

        if self.ratioOfWhiteToDarkPixel(figACopy) > self.ratioOfWhiteToDarkPixel(figBCopy):
            figACopy = self.imageFill(figACopy)
            figCCopy = self.imageFill(figCCopy)
        else:
            figBCopy = self.imageFill(figBCopy)
            for op in opListCopy:
                op = self.imageFill(op)

        if not self.isEqualImages(figACopy, figBCopy, 0.037):
            return [0, 0, 0, 0, 0, 0]

        differenceMetric = []
        for op in opListCopy:
            differenceMetric.append(self.differenceImagesMetric(figCCopy, op))

        minValue = min(differenceMetric)
        minIndex = differenceMetric.index(minValue)

        fillScoreList = []
        i = 0
        for op in opListCopy:
            if (i == minIndex):
                fillScoreList.append(1)
            else:
                fillScoreList.append(0)
            i = i + 1

        return fillScoreList

    def imageFill(self, image):
        width, height = image.size
        center = (int(0.5 * width), int(0.5 * height))
        black = (0)
        ImageDraw.floodfill(image, xy=center, value=black)
        return image

    def checkReflectionPropertyAndScore3x3(self, figA, figB, figC, figD, figE, figF, figG, figH, opList):
        mirrorFigALeftRight = figA.transpose(Image.FLIP_LEFT_RIGHT)
        mirrorFigDLeftRight = figD.transpose(Image.FLIP_LEFT_RIGHT)
        mirrorFigGLeftRight = figG.transpose(Image.FLIP_LEFT_RIGHT)
        mirrorFigATopDown = figA.transpose(Image.FLIP_TOP_BOTTOM)
        mirrorFigBTopDown = figB.transpose(Image.FLIP_TOP_BOTTOM)
        mirrorFigCTopDown = figC.transpose(Image.FLIP_TOP_BOTTOM)
        ct = 0.07

        isReflectionRelationAC = self.isEqualImages(mirrorFigALeftRight, figC, ct)
        isReflectionRelationDF = self.isEqualImages(mirrorFigDLeftRight, figF, ct)
        isReflectionRelationAG = self.isEqualImages(mirrorFigATopDown, figG, ct)
        isReflectionRelationBH = self.isEqualImages(mirrorFigBTopDown, figH, ct)

        reflectionScoreList = []
        if (isReflectionRelationAC and isReflectionRelationDF and isReflectionRelationAG and isReflectionRelationBH):
            for op in opList:
                if self.isEqualImages(op, mirrorFigGLeftRight, ct) and self.isEqualImages(op, mirrorFigCTopDown, ct):
                    reflectionScoreList.append(1)
                else:
                    reflectionScoreList.append(0)
            return reflectionScoreList
        return [0,0,0,0,0,0,0,0]

    def darkPixelDensity(self, image):
        countBlackPixelImage = 1
        for pixel in image.getdata():
            if pixel == (0):
                countBlackPixelImage += 1
        return countBlackPixelImage * 100.00 / len(list(image.getdata()))

    def intersectionPixelRatio(self, image1, image2):
        lenList = len(list(image1.getdata()))
        listImage1 = list(image1.getdata())
        listImage2 = list(image2.getdata())

        countIntersectionDarkPixel = 1
        for i in range(lenList):
            if listImage1[i] == 0 and listImage2[i] == 0:
                countIntersectionDarkPixel += 1
        return countIntersectionDarkPixel * 100.00 / (lenList)

    def solveProb2x2(self, problem):
        # print(problem.figures["A"].visualFilename)
        figA = Image.open(problem.figures["A"].visualFilename).convert('L').point(lambda x: 0 if x < 128 else 255, '1')
        figB = Image.open(problem.figures["B"].visualFilename).convert('L').point(lambda x: 0 if x < 128 else 255, '1')
        figC = Image.open(problem.figures["C"].visualFilename).convert('L').point(lambda x: 0 if x < 128 else 255, '1')
        op1 = Image.open(problem.figures["1"].visualFilename).convert('L').point(lambda x: 0 if x < 128 else 255, '1')
        op2 = Image.open(problem.figures["2"].visualFilename).convert('L').point(lambda x: 0 if x < 128 else 255, '1')
        op3 = Image.open(problem.figures["3"].visualFilename).convert('L').point(lambda x: 0 if x < 128 else 255, '1')
        op4 = Image.open(problem.figures["4"].visualFilename).convert('L').point(lambda x: 0 if x < 128 else 255, '1')
        op5 = Image.open(problem.figures["5"].visualFilename).convert('L').point(lambda x: 0 if x < 128 else 255, '1')
        op6 = Image.open(problem.figures["6"].visualFilename).convert('L').point(lambda x: 0 if x < 128 else 255, '1')

        opList = [op1, op2, op3, op4, op5, op6]
        if problem.figures["A"].visualFilename == "Problems/Challenge Problems B/Challenge Problem B-06/A.png":
            print("Yoolo")

        finalScoresList = self.listFinalScore(figA, figB, figC, opList)
        # print(finalScoresList)
        max_score = max(finalScoresList)
        indexMaxScore = finalScoresList.index(max_score)
        # print("option chosen: " + str(indexMaxScore + 1))
        return indexMaxScore + 1

    def listFinalScore(self, figA, figB, figC, opList):
        mode = self.decideComparisonMode(figA, figB, figC)
        # print("mode = " + str(mode))
        rotationScore = [0, 0, 0, 0]
        reflectionScore = [0, 0, 0, 0]
        pixelRatioScore = [0, 0, 0, 0]
        if mode == 0:
            rotationScore = np.array(self.scoreRotation(figA, figB, figC, opList)) + np.array(
                self.scoreRotation(figA, figC, figB, opList) + np.array(self.scoreRotation(figB, figC, figA, opList)))
            reflectionScore = np.array(self.scoreReflection(figA, figB, figC, opList)) + np.array(
                self.scoreReflection(figA, figC, figB, opList) + np.array(
                    self.scoreReflection(figB, figC, figA, opList)))
            pixelRatioScore = np.array(self.scorerPixelColor(figB, opList)) + np.array(
                self.scorerPixelColor(figC, opList) + np.array(self.scorerPixelColor(figA, opList)))

        elif mode == 1:
            rotationScore = np.array(self.scoreRotation(figA, figB, figC, opList)) + np.array(
                self.scoreRotation(figB, figC, figA, opList))
            reflectionScore = np.array(self.scoreReflection(figA, figB, figC, opList)) + np.array(
                self.scoreReflection(figB, figC, figA, opList))
            pixelRatioScore = np.array(self.scorerPixelColor(figC, opList)) + np.array(
                self.scorerPixelColor(figA, opList))

        elif mode == 2:
            rotationScore = np.array(self.scoreRotation(figA, figC, figB, opList)) + np.array(
                self.scoreRotation(figB, figC, figA, opList))
            reflectionScore = np.array(self.scoreReflection(figA, figC, figB, opList)) + np.array(
                self.scoreReflection(figB, figC, figA, opList))
            pixelRatioScore = np.array(self.scorerPixelColor(figB, opList)) + np.array(
                self.scorerPixelColor(figA, opList))

        elif mode == 3:
            rotationScore = np.array(self.scoreRotation(figA, figB, figC, opList)) + np.array(
                self.scoreRotation(figA, figC, figB, opList))
            reflectionScore = np.array(self.scoreReflection(figA, figB, figC, opList)) + np.array(
                self.scoreReflection(figA, figC, figB, opList))
            pixelRatioScore = np.array(self.scorerPixelColor(figB, opList)) + np.array(
                self.scorerPixelColor(figC, opList))
        elif mode == 4:
            rotationScore = np.array(self.scoreRotation(figA, figB, figC, opList))
            reflectionScore = np.array(self.scoreReflection(figA, figB, figC, opList))
            pixelRatioScore = np.array(self.scorerPixelColor(figC, opList))
        elif mode == 5:
            rotationScore = np.array(self.scoreRotation(figA, figC, figB, opList))
            reflectionScore = np.array(self.scoreReflection(figA, figC, figB, opList))
            pixelRatioScore = np.array(self.scorerPixelColor(figB, opList))
        elif mode == -1:
            return list(
                np.array(self.hitAndTry(figA, figB, figC, opList)) + np.array(self.hitAndTry(figA, figC, figB, opList)))

        # print("rotationScore:" + str(rotationScore))
        # print("reflectionScore: " + str(reflectionScore))
        return list(rotationScore + 16 * reflectionScore + 64 * pixelRatioScore)

    def decideComparisonMode(self, figA, figB, figC):
        compareAB = self.equalPixelDensity(figA, figB)
        compareAC = self.equalPixelDensity(figA, figC)
        compareBC = self.equalPixelDensity(figB, figC)
        if compareAB and compareAC and compareBC:
            return 0
        if compareAB and compareBC:
            return 1
        if compareAC and compareBC:
            return 2
        if compareAB and compareAC:
            return 3
        if compareAB:
            return 4
        if compareAC:
            return 5
        return -1

    def scorerPixelColor(self, fig, opList):
        scoresPixelList = []
        for op in opList:
            if self.equalPixelDensity(fig, op):
                scoresPixelList.append(1)
            else:
                scoresPixelList.append(0)
        return scoresPixelList

    def equalPixelDensity(self, image1, image2):
        image1Density = self.ratioOfWhiteToDarkPixel(image1)
        image2Density = self.ratioOfWhiteToDarkPixel(image2)
        return abs(image1Density - image2Density) < 1

    def scoreRotation(self, figA, figB, figC, opList):
        rots = []
        for x in range(0, 360, 90):
            if self.isEqualImages(figA.rotate(x), figB, 0.07):
                rots.append(x)

        # print ("rotation: " + str(rots))
        if not rots:
            return [0, 0, 0, 0, 0, 0]

        rotationScoreList = [0, 0, 0, 0, 0, 0]
        for rot in rots:
            differenceMetric = []
            eachRotationScoreList = []
            for op in opList:
                differenceMetric.append(self.differenceImagesMetric(figC.rotate(rot), op))

            minValue = min(differenceMetric)
            minIndex = differenceMetric.index(minValue)

            i = 0
            for op in opList:
                if (i == minIndex):
                    eachRotationScoreList.append(1)
                else:
                    eachRotationScoreList.append(0)
                i = i + 1
            rotationScoreList = list(np.array(rotationScoreList) + np.array(eachRotationScoreList))

        return rotationScoreList

    def scoreReflection(self, figA, figB, figC, opList):
        scoreLeftRight = np.array(self.scoreLeftRightTopDownReflection(figA, figB, figC, opList, Image.FLIP_LEFT_RIGHT))
        # print("scoreLeftRight: " + str(scoreLeftRight))
        scoreTopDown = np.array(self.scoreLeftRightTopDownReflection(figA, figB, figC, opList, Image.FLIP_TOP_BOTTOM))
        # print("scoreTopDown: " + str(scoreTopDown))
        return list(scoreLeftRight + scoreTopDown)

    def scoreLeftRightTopDownReflection(self, figA, figB, figC, opList, transpose):
        mirrorFigA = figA.transpose(transpose)

        if not self.isEqualImages(mirrorFigA, figB, 0.05):
            return [0, 0, 0, 0, 0, 0]

        mirrorLeftRightFigC = figC.transpose(transpose)

        leftRightReflectionScoreList = []
        differenceMetric = []
        for op in opList:
            differenceMetric.append(self.differenceImagesMetric(mirrorLeftRightFigC, op))

        # print("differenceMetricReflection: " + str(transpose) + " " + str(differenceMetric))
        minValue = min(differenceMetric)
        minIndex = differenceMetric.index(minValue)

        i = 0
        for op in opList:
            if (i == minIndex):
                leftRightReflectionScoreList.append(1)
            else:
                leftRightReflectionScoreList.append(0)
            i = i + 1

        # print(leftRightReflectionScoreList)
        return leftRightReflectionScoreList

    def isEqualImages(self, image1, image2, threshold):
        return self.differenceImagesMetric(image1, image2) < threshold

    def differenceImagesMetric(self, image1, image2):
        diff = ImageChops.difference(image1, image2)
        return self.ratioOfWhiteToDarkPixel(diff)

    def ratioOfWhiteToDarkPixel(self, image):
        blackPixel = 1
        whitePixel = 1
        for pixel in image.getdata():
            if pixel == (0):
                blackPixel += 1
            else:
                whitePixel += 1
        # print(whitePixel/float(blackPixel))
        return whitePixel / float(blackPixel)

    def hitAndTry(self, figA, figB, figC, opList):
        # return self.diffOfDiffImages(figA, figB, figC, opList)
        # print("fill and score: " + str(self.fillImageAndScore(figA, figB, figC, opList)))
        return list(np.array(self.diffOfDiffImages(figA, figB, figC, opList))
                    + np.array(self.fillImageAndScore(figA, figB, figC, opList)))

    def diffOfDiffImages(self, figA, figB, figC, opList):
        diffAB = ImageChops.difference(figA, figB)
        diffOfDiffList = []
        for op in opList:
            diffCOp = ImageChops.difference(figC, op)
            if self.isEqualImages(diffAB, diffCOp, 0.037):
                diffOfDiffList.append(1)
            else:
                diffOfDiffList.append(0)
        return diffOfDiffList

    # def imageAddAndCompare(self, figA, figB):
    #     result = Image.alpha_composite(figA, figB)
    #     result.show()
    #     sys.exit()

    def fillImageAndScore(self, figA, figB, figC, opList):
        figACopy = figA.copy()
        figBCopy = figB.copy()
        figCCopy = figC.copy()
        opListCopy = []
        for op in opList:
            opListCopy.append(op.copy())

        if self.ratioOfWhiteToDarkPixel(figACopy) > self.ratioOfWhiteToDarkPixel(figBCopy):
            figACopy = self.imageFill(figACopy)
            figCCopy = self.imageFill(figCCopy)
        else:
            figBCopy = self.imageFill(figBCopy)
            for op in opListCopy:
                op = self.imageFill(op)

        if not self.isEqualImages(figACopy, figBCopy, 0.037):
            return [0, 0, 0, 0, 0, 0]

        differenceMetric = []
        for op in opListCopy:
            differenceMetric.append(self.differenceImagesMetric(figCCopy, op))

        minValue = min(differenceMetric)
        minIndex = differenceMetric.index(minValue)

        fillScoreList = []
        i = 0
        for op in opListCopy:
            if (i == minIndex):
                fillScoreList.append(1)
            else:
                fillScoreList.append(0)
            i = i + 1

        return fillScoreList

    def imageFill(self, image):
        width, height = image.size
        center = (int(0.5 * width), int(0.5 * height))
        black = (0)
        ImageDraw.floodfill(image, xy=center, value=black)
        return image
