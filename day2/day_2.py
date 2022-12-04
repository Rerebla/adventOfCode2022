import typing
from enum import Enum


class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class GameOutcome(Enum):
    WIN = 6
    DRAW = 3
    LOOSE = 0


letterShapeMappingPart1: typing.Mapping[str, Shape] = {
    "A": Shape.ROCK,
    "B": Shape.PAPER,
    "C": Shape.SCISSORS,
    "X": Shape.ROCK,
    "Y": Shape.PAPER,
    "Z": Shape.SCISSORS
}
letterGameOutcomeMapping: typing.Mapping[str, GameOutcome] = {
    "X": GameOutcome.LOOSE,
    "Y": GameOutcome.DRAW,
    "Z": GameOutcome.WIN
}
part2CombinationMapping: typing.Dict[any, Shape] = {
    (Shape.ROCK, GameOutcome.WIN): Shape.PAPER,
    (Shape.ROCK, GameOutcome.DRAW): Shape.ROCK,
    (Shape.ROCK, GameOutcome.LOOSE): Shape.SCISSORS,
    (Shape.PAPER, GameOutcome.WIN): Shape.SCISSORS,
    (Shape.PAPER, GameOutcome.DRAW): Shape.PAPER,
    (Shape.PAPER, GameOutcome.LOOSE): Shape.ROCK,
    (Shape.SCISSORS, GameOutcome.WIN): Shape.ROCK,
    (Shape.SCISSORS, GameOutcome.DRAW): Shape.SCISSORS,
    (Shape.SCISSORS, GameOutcome.LOOSE): Shape.PAPER,
}
scoreMapping: typing.Dict[Shape, typing.Dict[Shape, int]] = {
    Shape.ROCK: {
        Shape.PAPER: Shape.PAPER.value + GameOutcome.WIN.value,
        Shape.ROCK: Shape.ROCK.value + GameOutcome.DRAW.value,
        Shape.SCISSORS: Shape.SCISSORS.value + GameOutcome.LOOSE.value,
    },
    Shape.PAPER: {
        Shape.SCISSORS: Shape.SCISSORS.value + GameOutcome.WIN.value,
        Shape.PAPER: Shape.PAPER.value + GameOutcome.DRAW.value,
        Shape.ROCK: Shape.ROCK.value + GameOutcome.LOOSE.value,
    },
    Shape.SCISSORS: {
        Shape.ROCK: Shape.ROCK.value + GameOutcome.WIN.value,
        Shape.SCISSORS: Shape.SCISSORS.value + GameOutcome.DRAW.value,
        Shape.PAPER: Shape.PAPER.value + GameOutcome.LOOSE.value,
    }
}


def resolveGameLogic(opponentShape: Shape, ownShape: Shape):
    winScore = GameOutcome.WIN.value
    drawScore = GameOutcome.DRAW.value
    looseScore = GameOutcome.LOOSE.value
    score: int = ownShape.value
    return scoreMapping.get(opponentShape).get(ownShape)
    # match ownShape:
    #     case  Shape.ROCK:
    #         if opponentShape is Shape.ROCK:
    #             return score + drawScore
    #         if opponentShape is Shape.PAPER:
    #             return score + looseScore
    #         if opponentShape is Shape.SCISSORS:
    #             return score + winScore
    #     case Shape.PAPER:
    #         if opponentShape is Shape.ROCK:
    #             return score + winScore
    #         if opponentShape is Shape.PAPER:
    #             return score + drawScore
    #         if opponentShape is Shape.SCISSORS:
    #             return score + looseScore
    #     case Shape.SCISSORS:
    #         if opponentShape is Shape.ROCK:
    #             return score + looseScore
    #         if opponentShape is Shape.PAPER:
    #             return score + winScore
    #         if opponentShape is Shape.SCISSORS:
    #             return score + drawScore


def compareOneLinePart1(line: str):
    opponentPick, ownPick = line.strip().split(" ")
    opponentShape = letterShapeMappingPart1.get(opponentPick)
    ownShape = letterShapeMappingPart1.get(ownPick)
    return resolveGameLogic(opponentShape, ownShape)


def compareOneLinePart2(line: str):
    opponentPick, roundOutcome = line.strip().split(" ")
    opponentShape = letterShapeMappingPart1.get(opponentPick)
    gameOutcome = letterGameOutcomeMapping.get(roundOutcome)
    ownShape = part2CombinationMapping.get((opponentShape, gameOutcome))
    return resolveGameLogic(opponentShape, ownShape)


with open('input.txt') as f:
    lines = f.readlines()
    # Part 1
    score = 0
    for line in lines:
        score += compareOneLinePart1(line)
    print("Part 1: Score is: ", score)
    # Part 2
    score = 0
    for line in lines:
        score += compareOneLinePart2(line)
    print("Part 2: Score is: ", score)
