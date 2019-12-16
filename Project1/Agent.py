# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

# Install Pillow and uncomment this line to access image processing.
from PIL import Image, ImageDraw, ImageChops
import numpy as np


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
        if problem.problemType != '2x2':
            return -1
        print(problem.figures["A"].visualFilename)
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
        print(finalScoresList)
        max_score = max(finalScoresList)
        indexMaxScore = finalScoresList.index(max_score)
        print("option chosen: " + str(indexMaxScore + 1))
        return indexMaxScore + 1

    def listFinalScore(self, figA, figB, figC, opList):
        mode = self.decideComparisonMode(figA, figB, figC)
        print("mode = " + str(mode))
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

        print("rotationScore:" + str(rotationScore))
        print("reflectionScore: " + str(reflectionScore))
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

        print ("rotation: " + str(rots))
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
        print("scoreLeftRight: " + str(scoreLeftRight))
        scoreTopDown = np.array(self.scoreLeftRightTopDownReflection(figA, figB, figC, opList, Image.FLIP_TOP_BOTTOM))
        print("scoreTopDown: " + str(scoreTopDown))
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

        print("differenceMetricReflection: " + str(transpose) + " " + str(differenceMetric))
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
        print("fill and score: " + str(self.fillImageAndScore(figA, figB, figC, opList)))
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
