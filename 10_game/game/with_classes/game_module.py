import time
import turtle
import random
import sprite_module
import text_module

class Game:
    ALIEN_SPAWN_INTERVAL = 1.2  # Seconds
        
    def __init__(self, dimensions, screen):
        self.dimensions = dimensions
        self.screen = screen

        self.score = 0
        self.game_running = True

        self.enemy_timer = 0

        self.enemy_array = []
        self.laser_array = []
                    
        self.text = text_module.Text(self.dimensions)
        self.cannon = sprite_module.Cannon(self.dimensions)

        self.key_bindings()

        
    def render(self):
        self.text.write_score(self.score)
        self.cannon.move()        
        self.laser_collision_test()
        self.spawn_enemies()            


    def laser_collision_test(self):           
        for laser in self.laser_array:             
            for enemy in self.enemy_array:
                if laser.sprite.distance(enemy.sprite) < 20:
                    self.remove_sprite(laser, self.laser_array)            
                    self.remove_sprite(enemy, self.enemy_array)
                    self.score += 1
                    break

            laser.move()
            # Remove laser if it goes off screen
            if laser.sprite.ycor() > self.dimensions.top:
                self.remove_sprite(laser, self.laser_array)   
                break


    def spawn_enemies(self):
        if time.time() - self.enemy_timer > self.ALIEN_SPAWN_INTERVAL:
            if(random.randint(0, 10) >= 9):
                enemy = sprite_module.Ufo(self.dimensions)
            else:
                enemy = sprite_module.Alien(self.dimensions)            
            self.enemy_array.append(enemy)
            self.enemy_timer = time.time()
        
        for enemy in self.enemy_array:
            enemy.move()
            # Check for game over
            if enemy.sprite.ycor() < self.dimensions.floor:
                self.game_running = False
                break  
               
    
    def remove_sprite(self, sprite, sprite_array):
        sprite.sprite.clear()
        sprite.sprite.hideturtle()
        self.screen.update()
        try:
            sprite_array.remove(sprite)
            turtle.turtles().remove(sprite.sprite)
        except ValueError:
            pass                        

    def key_bindings(self):
        self.screen.onkeypress(self.cannon.move_left, "Left")
        self.screen.onkeypress(self.cannon.move_right, "Right")
        self.screen.onkeyrelease(self.cannon.stop_movement, "Left")
        self.screen.onkeyrelease(self.cannon.stop_movement, "Right")
        self.screen.onkeypress(self.fire, "space")
        self.screen.onkeypress(turtle.bye, "q")
        self.screen.listen()


    def fire(self):
        laser = sprite_module.Laser(self.cannon)
        self.laser_array.append(laser)


    def game_over(self):
        self.text.write_game_over()