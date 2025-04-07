from settings import *
import random
from timer import Timer
class Game:
    def __init__(self, get_next_shape, update_score):
        self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.display_surface = pygame.display.get_surface()
        self.rect = self.surface.get_rect(topleft=(PADDING, PADDING))
        self.sprites = pygame.sprite.Group()
        self.get_next_shape = get_next_shape
        self.update_score = update_score
        self.game_over = False

        self.line_surface = self.surface.copy()
        self.line_surface.fill((0,255,0))
        self.line_surface.set_colorkey((0,255,0))
        self.line_surface.set_alpha(50)

        self.field_data = [[0 for x in range(COLUMNS)] for y in range(ROWS)]
        self.tetromino = Tetromino(random.choice(list(TETROMINOS.keys())), self.sprites, self.create_new_tetronimo, self.field_data)

        self.down_speed = UPDATE_START_SPEED
        self.down_speed_faster = self.down_speed * 0.3
        self.down_pressed = False
        self.timers = {
            'vertical move': Timer(self.down_speed, True, self.move_down),
            'horizontal move': Timer(MOVE_WAIT_TIME),
            'rotate': Timer(ROTATE_WAIT_TIME)
        }
        self.timers['vertical move'].activate()
        self.current_level = 1
        self.current_score = 0
        self.current_lines = 0

    def calculate_score(self, num_lines):
        self.current_lines += num_lines
        self.current_score += SCORE_DATA[num_lines] * self.current_level

        if self.current_lines / 10 > self.current_level:
            self.current_level += 1
            self.down_speed *= 0.75
            self.down_speed_faster = self.down_speed * 0.3
            self.timers['vertical move'].duration = self.down_speed
        self.update_score(self.current_lines, self.current_score, self.current_level)

    def create_new_tetronimo(self):
        self.check_finished_rows()
        self.tetromino = Tetromino(self.get_next_shape(), self.sprites,self.create_new_tetronimo, self.field_data)
        for block in self.tetromino.blocks:
            if block.vertical_collide(0, self.field_data):
                self.game_over = True
                break

    def timer_update(self):
        for timer in self.timers.values():
            timer.update()
    def move_down(self):
        self.tetromino.move_down()

    def draw_grid(self):
        for col in range(1,COLUMNS):
            x = col * CELL_SIZE
            pygame.draw.line(self.line_surface,LINE_COLOR,(x,0),(x,self.surface.get_height()),1)

        for row in range(1,ROWS):
            y = row * CELL_SIZE
            pygame.draw.line(self.line_surface,LINE_COLOR,(0,y),(self.surface.get_width(),y),1)

        self.surface.blit(self.line_surface,(0,0))

    def input(self):
        keys = pygame.key.get_pressed()
        if not self.timers['horizontal move'].active:
            if keys[pygame.K_LEFT]:
                self.tetromino.move_horizontal(-1)
                self.timers['horizontal move'].activate()
            if keys[pygame.K_RIGHT]:
                self.tetromino.move_horizontal(1)
                self.timers['horizontal move'].activate()

        if not self.timers['rotate'].active:
            if keys[pygame.K_UP]:
                self.tetromino.rotate()
                self.timers['rotate'].activate()

        if not self.down_pressed and keys[pygame.K_DOWN]:
            self.down_pressed = True
            self.timers['vertical move'].duration = self.down_speed_faster

        if self.down_pressed and not keys[pygame.K_DOWN]:
            self.down_pressed = False
            self.timers['vertical move'].duration = self.down_speed

    def check_finished_rows(self):
        delete_rows = []
        for i, row in enumerate(self.field_data):
            if all(row):
                delete_rows.append(i)
        if delete_rows:
            for del_row in delete_rows:

                for block in self.field_data[del_row]:
                    block.kill()

                for row in self.field_data:
                    for block in row:
                        if block and block.pos.y < del_row:
                            block.pos.y += 1

            self.field_data = [[0 for x in range(COLUMNS)] for y in range(ROWS)]
            for block in self.sprites:
                self.field_data[int(block.pos.y)][int(block.pos.x)] = block
            self.calculate_score(len(delete_rows))
    def run(self):
        if not self.game_over:
            self.input()
            self.timer_update()
            self.sprites.update()

            self.surface.fill(GRAY)
            self.sprites.draw(self.surface)
            self.draw_grid()
            self.display_surface.blit(self.surface, (PADDING, PADDING))
            pygame.draw.rect(self.display_surface, LINE_COLOR, self.rect, 2, 2)
        else:
            self.surface.fill(GRAY)
            font = pygame.font.Font(None, 60)
            text_surface = font.render('GAME OVER', True, 'white')
            text_rect = text_surface.get_rect(center=(self.surface.get_width() / 2, self.surface.get_height() / 2 - 50))
            self.surface.blit(text_surface, text_rect)

            score_font = pygame.font.Font(None, 40)
            score_surface = score_font.render(f'Score: {self.current_score}', True, 'white')
            score_rect = score_surface.get_rect(
                center=(self.surface.get_width() / 2, self.surface.get_height() / 2 + 10))
            self.surface.blit(score_surface, score_rect)
            self.display_surface.blit(self.surface, (PADDING, PADDING))
            pygame.draw.rect(self.display_surface, LINE_COLOR, self.rect, 2, 2)

class Tetromino:
    def __init__(self, shape, group, create_new_tetronimo,field_data):
        self.shape = shape
        self.block_positions = TETROMINOS[shape]['shape']
        self.color = TETROMINOS[shape]['color']
        self.create_new_tetronimo = create_new_tetronimo
        self.field_data = field_data
        self.blocks = [Block(group,pos,self.color) for pos in self.block_positions]

    def next_move_horizontal_collide(self,blocks,delta):
        collision_list = [block.horizontal_collide(int(block.pos.x + delta),self.field_data) for block in self.blocks]
        return True if any(collision_list) else False

    def next_move_vertical_collide(self,blocks,delta):
        collision_list = [block.vertical_collide(int(block.pos.y + delta),self.field_data) for block in self.blocks]
        return True if any(collision_list) else False

    def rotate(self):
        if self.shape != 'O':
            pivot_pos = self.blocks[0].pos
            new_block_positions = [block.rotate(pivot_pos) for block in self.blocks]
            for pos in new_block_positions:
                if pos.x < 0 or pos.x >= COLUMNS:
                    return
                if self.field_data[int(pos.y)][int(pos.x)]:
                    return
                if pos.y > ROWS:
                    return

            for i, block in enumerate(self.blocks):
                block.pos = new_block_positions[i]

    def move_down(self):
        if not self.next_move_vertical_collide(self.blocks,1):
            for block in self.blocks:
                block.pos.y += 1
        else:
            for block in self.blocks:
                self.field_data[int(block.pos.y)][int(block.pos.x)] = block
            self.create_new_tetronimo()


    def move_horizontal(self, delta):
        if not self.next_move_horizontal_collide(self.blocks,delta):
            for block in self.blocks:
                block.pos.x += delta

class Block(pygame.sprite.Sprite):
    def __init__(self, group, pos, color):
        super().__init__(group)
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(color)

        self.pos = pygame.Vector2(pos) + BLOCK_OFFSET
        # x = self.pos.x * CELL_SIZE
        # y = self.pos.y * CELL_SIZE
        # self.rect = self.image.get_rect(topleft=(x,y))
        self.rect = self.image.get_rect(topleft=self.pos * CELL_SIZE)

    def rotate(self, pivot_pos):
        # distance = self.pos - pivot_pos
        # new_pos = pivot_pos + distance.rotate(90)
        # return new_pos
        return pivot_pos + (self.pos - pivot_pos).rotate(90)
    def horizontal_collide(self, x, field_data):
        if not 0 <= x < COLUMNS:
            return True
        if field_data[int(self.pos.y)][x]:
            return True

    def vertical_collide(self, y,field_data):
        if y >= ROWS:
            return True
        if y >= 0 and field_data[y][int(self.pos.x)]:
            return True

    def update(self):
        # self.rect = self.image.get_rect(topleft=self.pos * CELL_SIZE)
        self.rect.topleft = self.pos * CELL_SIZE
