"""

    This solution is not mine. 

    It is an adapted code from 

    https://topaz.github.io/paste/#XQAAAQDYBgAAAAAAAAARmknGRw8TogB3OyW56zkJNAnj1YapbqOnYw6+vS5kUM9H/WrqKcnh8YFzYrKUk5PHWEEt7R3wOd2jnSDhRacpfpoezlT0AqzBOUTzTVZ4WrUECuvW9iqw4MtDoKmyO3Kq+qlVJtOziMBQHNjhPg6ty5F94Eegy3wmqeqy2fq+ZZRRRItk2K7ywvDPqkAf31jySVV4ooWcnuOLUEnjI3ndnvysR8B2CCvDQomo3Oxvzh1e+l3W1PYFqkXWAi1VV3voNpg+6tTC5vS1cTABDLt7D4ZL5YDRHWvF0J8mRYTzfia1p1fMWZJ7sFD88k6Mem4AdkDwPMpjFkqUGfAfaMmHpepE9IoPvLG2TFBzOLS1JAsvQnJJWVx3zQUFt0RXVfUdFI9k+kHvh91nighnJ6jUILGIQxR2ya9fvnjmDy+dZDA237IvsxcIiTSCXlS2z9r5tBNjt25Hr5vIGqoneFWTlIRExoqgFsQ+/6ExxTGFsrdcue636dMgRaZQLhQKLqjCICeLul/bWPN1ZpKPN+zuMWzj1K8kDp1cMYkyhgvhrPXIjr7QALojx9rNZ+q1BdQ0qcWH6TRJUTJPH2ptGbc0kIXc2c5pCl2R/qcJKZl3/MJkL6bov2c13Cmhjf76Phjk3n+7ga+t0vMWL0qkBSSYYvHbQ1XDyYi1IrIgCboiSf8bSTmpFO8Sn4elc+mlhZ1AK645pByLMMqFo+CdVI/SYOKxpgDhFXOQci25kR5eYTx0UPYJcsSgMVjF/8sC2NUmTqruEsKnLy1J8ShHXMh4S0cWFXjV3/v6YALSPg4JNsTnr1YGf8/CFddOzfko/MWSR9JxqELhtGj/p345Sf9hVx7HWH2TSoxAQP//luxqfA==

  from: https://www.reddit.com/r/adventofcode/comments/18ey1s7/comment/kcrl36f

It is a clever solution further explained by its author here: https://www.reddit.com/r/adventofcode/comments/18f518b/2023_day_10_efficient_approach_to_part_2_math/

The formula is from 

https://en.wikipedia.org/wiki/Shoelace_formula

Didn't like this second part after all.

"""


from enum import IntEnum


class Direction(IntEnum):
    None_ = 0
    Up = 1
    Down = 2
    Left = 4
    Right = 8


direction = {
    "|": Direction.Up | Direction.Down,
    "-": Direction.Left | Direction.Right,
    "L": Direction.Up | Direction.Right,
    "J": Direction.Up | Direction.Left,
    "7": Direction.Down | Direction.Left,
    "F": Direction.Down | Direction.Right,
    ".": Direction.None_,
    "S": Direction.Up | Direction.Down | Direction.Left | Direction.Right,
}

FILE = "input.txt"


def load():
    return [
        [col for col in row] for row in [row.strip() for row in open(FILE).readlines()]
    ]


def main():
    data = load()
    r, u = len(data[0]), len(data)

    sx, x, sy, y = 0, 0, 0, 0
    for k in range(len(data)):
        for i in range(len(data[k])):
            if data[k][i] == "S":
                sx = k
                x = k
                sy = i
                y = i

    area, circ = 0, 0
    while True:
        circ += 1

        # Current symbol
        c = data[x][y]

        # Save old x,y to deactivate cell
        old_x = x
        old_y = y

        # Now we search for a route to explore
        if (  # It means we came from left and want to go right
            y < r  # Do we have cells to the right?
            and direction[c] & Direction.Right
            and direction[data[x][y + 1]] & Direction.Left
        ):
            area += x  # Area is expanding to the right
            y += 1  # Also y is expanding
        elif (
            x < u
            and direction[c] & Direction.Down
            and direction[data[x + 1][y]] & Direction.Up
        ):
            area -= y
            x += 1
        elif (
            y > 0
            and direction[c] & Direction.Left
            and direction[data[x][y - 1]] & Direction.Right
        ):
            area -= x
            y -= 1
        elif (
            x > 0
            and direction[c] & Direction.Up
            and direction[data[x - 1][y]] & Direction.Down
        ):
            area += y
            x -= 1

        # At this point there is no route to go further
        else:
            break

        # Deactivate cell
        data[old_x][old_y] = "."

    area += x * sy - y * sx

    print("Part 1:", circ // 2)
    print("Part 2:", (abs(area) - circ) // 2 + 1)


if __name__ == "__main__":
    main()
