import pygame
import time
import random

width, height = 400,500

class Snake:
    def __init__(self, screen):
        self.len_snake = 1
        self.x = [100] * self.len_snake
        self.y = [100] * self.len_snake
        self.x_change = 0
        self.y_change = 0
        self.block = 20
        self.screen = screen


    def draw(self):
        for i in range (self.len_snake):
          pygame.draw.rect(self.screen, (255, 0, 0), [self.x[i], self.y[i], self.block, self.block])
          pygame.display.update()
        self.screen.fill((255, 255, 255))

    def move(self):
        for i in range(self.len_snake -1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        self.x[0] += self.x_change
        self.y[0] += self.y_change

    def change(self, dir, unit):
        if dir == "u":
            self.y_change = -unit
            self.x_change = 0
        if dir == "d":
            self.y_change = unit
            self.x_change = 0
        if dir == "r":
            self.y_change = 0
            self.x_change = unit
        if dir == "l":
            self.y_change = 0
            self.x_change = -unit

    def is_collision(self):
        if self.x[0] == (int(width/20)-2)*20 or self.x[0]==20 or self.y[0] == (int(height/20)-2)*20 or self.y[0] ==20:
            return True
        return False


class Food:
    def __init__(self, screen):
        self.screen = screen
        self.x = random.randrange(4, (int(width/20)-2)) * 20
        self.y = random.randrange(4, (int(height/20)-2)) * 20

    def draw(self):
        pygame.draw.rect(self.screen, (0,255,0), [self.x, self.y, 20, 20])
        pygame.display.update()

    def move(self):
        self.x = random.randrange(4, (int(width/20)-2)) * 20
        self.y = random.randrange(4, (int(height/20)-2)) * 20


class Grid:
    def __init__(self, screen):
        self.screen = screen

    def draw(self):
        for x in range (round(width/20)):
            pygame.draw.rect(self.screen, (0,0,0), [x*20, 0*20, 20 , 20])
            pygame.draw.rect(self.screen, (0, 0, 0), [x * 20, (round(height/20)-1)*20, 20, 20])
        for y in range (round(height/20)):
            pygame.draw.rect(self.screen, (0,0,0), [0*20, y*20, 20 , 20])
            pygame.draw.rect(self.screen, (0,0,0), [(round(width/20)-1)*20, y*20, 20 , 20])
        pygame.display.update()


class Game:
    width, height = 400,500

    def __init__(self):
        self.screen = pygame.display.set_mode((Game.width, Game.height))
        pygame.display.set_caption("snake game with OOP")
        self.screen.fill((255,255,255))
        pygame.display.update()
        self.len = 1
        self.snake = Snake(self.screen)
        Snake.draw(self.snake)  #or self.snake.draw()
        self.food = Food(self.screen)
        self.food.draw()
        self.snake_speed = 5
        self.grid = Grid(self.screen)


    def run(self):
        running = True
        while running:
            self.grid.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.change("u", 20)
                    if event.key == pygame.K_DOWN:
                        self.snake.change("d", 20)
                    if event.key == pygame.K_RIGHT:
                        self.snake.change("r", 20)
                    if event.key == pygame.K_LEFT:
                        self.snake.change("l", 20)

            if self.snake.x[0] == self.food.x and self.snake.y[0] == self.food.y:
                self.food.move()
                self.snake.len_snake +=1
                self.snake.x.append(self.snake.x[-1])
                self.snake.y.append(self.snake.y[-1])
                self.snake_speed+=0.25


            self.snake.move()
            if Snake.is_collision(self.snake) == True:
                running = False

            self.food.draw()
            self.snake.draw()

            pygame.time.Clock().tick(self.snake_speed)
        quit()


main = Game()
main.run()