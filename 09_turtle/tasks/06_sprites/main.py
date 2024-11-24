import turtle
import block_sprite

# create instance BlockSprite
b1 = block_sprite.BlockSprite(10, 20)
# create another instance BlockSprite
b2 = block_sprite.BlockSprite(100, 200)

# class draw functions
b1.draw()
b2.draw()

# deletes instances
del b1
del b2

turtle.done()