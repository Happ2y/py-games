# It's like a table tennis game where a player gets an score when the opponent misses the hit
import turtle

# create an window for the game
window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)
# prevents auto updation of the window
window.tracer(0)


# Paddle A
paddleA = turtle.Turtle()
# paddle animation speed, shape & color
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
# 5 * defaultWidth(=20), 1 * defaultLength(=20)
paddleA.shapesize(stretch_wid=5, stretch_len=1)
# prevents drawing lines while movement
paddleA.penup()
# initial coordinates
paddleA.goto(x=-350, y=0)


# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(x=350, y=0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(x=0, y=0)

# change of pixels in every movement of the ball in x & y directions
ball.dx = 0.2
ball.dy = 0.2


# create pen for updating scores
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)


def paddleA_UP():
    # move paddle A up
    paddleA.sety(paddleA.ycor() + 20)


def paddleA_DOWN():
    # move paddle A down
    paddleA.sety(paddleA.ycor() - 20)


def paddleB_UP():
    # move paddle B up
    paddleB.sety(paddleB.ycor() + 20)


def paddleB_DOWN():
    # move paddle B down
    paddleB.sety(paddleB.ycor() - 20)


# keyboard binding
window.listen()
window.onkeypress(paddleA_UP, "e")
window.onkeypress(paddleA_DOWN, "s")
window.onkeypress(paddleB_UP, "o")
window.onkeypress(paddleB_DOWN, "k")


# drive code
if __name__ == "__main__":
    playerA_score = playerB_score = 0
    pen.write(
        f"Player A: {playerA_score} \t Player B: {playerB_score}",
        align="center",
        font=("Courier", 24, "normal")
    )

    while True:
        window.update()

        # ball movement
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # when the ball hits window's right border
        if ball.xcor() > 390:
            ball.setx(390)
            ball.dx *= -1
            playerA_score += 1
            pen.clear()
            pen.write(
                f"Player A: {playerA_score} \t Player B: {playerB_score}",
                align="center",
                font=("Courier", 24, "normal")
            )

        # when the ball hits window's left border
        if ball.xcor() < -390:
            ball.setx(-390)
            ball.dx *= -1
            playerB_score += 1
            pen.clear()
            pen.write(
                f"Player A: {playerA_score} \t Player B: {playerB_score}",
                align="center",
                font=("Courier", 24, "normal")
            )

        # when the ball hits window's top border
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        # when the ball hits window's bottom border
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        # paddle & ball collisions
        if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < (paddleB.ycor() + 50) and ball.ycor() > (paddleB.ycor() - 50):
            ball.setx(340)
            ball.dx *= -1

        if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < (paddleA.ycor() + 50) and ball.ycor() > (paddleA.ycor() - 50):
            ball.setx(-340)
            ball.dx *= -1
