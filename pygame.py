import pygame

col_alive = (255, 255, 255)
col_dead = (10, 10, 10)

def init(dimx, dimy):
    cells = np.zeros((dimx, dimy))
    pattern = np.array([[0,0,1,1,0,0],
                         [1,0,0,0,1,0],
                         [0,0,0,0,0,1],
                         [0,0,1,0,0,1],
                         [0,1,1,1,0,0],
                         [0,0,0,0,0,0]])
    pos = (0,0)
    patterns_shape_y = pattern.shape[0]
    patterns_shape_x = pattern.shape[1]
    
    for ix in range(dimx//patterns_shape_x):
        for iy in range(dimy//patterns_shape_y):
            start_x = ix * patterns_shape_x
            end_x = (ix + 1) * patterns_shape_x
            cells[]
    
def main(dimx, dimy, cellsize):
    pygame.init()
    surface =  pygame.display.set_module((dimx * cellsize,
                                          dimy * cellsize))
    
    while True:
        for event in pygame.event.get():
            if event == pygame.quit():
                pygame.quit()
                return
        surface.fill(col_dead)
        pygame.dispaly.update()
            
if __name__ == '__main__':
    min(150, 120, 5)    