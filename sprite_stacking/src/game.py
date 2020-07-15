import pygame as pg 
from object_3d import Object3D


class Game:
	""" Класс, содержащий метод для инициализации игры и запуска игрового цикла. 
	
	Атрибуты:
	----------
	caption : str
		Название проекта и заголовок окна игры.
	screen_width : int
		Ширина экрана игры (в пикселях).
	screen_height : int
		Высота экрана игры (в пикселях).
	fps : int
		Максимальное число FPS игры.
	"""
	def __init__(self):
		self.caption = 'Sprite Stacking viewer'
		self.screen_width = 1280
		self.screen_height = 720
		self.fps = 60


	def run(self):
		""" Метод для инициализация игры и запуска игрового цикла."""
		pg.init()
		screen = pg.display.set_mode((self.screen_width, self.screen_height))
		pg.display.set_caption(self.caption)

		clock = pg.time.Clock()

		# Создаем объекты и делаем так, чтобы они вращались против часовой стрелки
		obj1 = Object3D(self.screen_width//4, self.screen_height//2, '../res/tank/', 7, screen)
		obj1.turn_counterclockwise = True

		obj2 = Object3D(self.screen_width//2, self.screen_height//2, '../res/van/', 12, screen)
		obj2.turn_counterclockwise = True

		obj3 = Object3D(self.screen_width - self.screen_width//4, self.screen_height//2, '../res/birch/', 30, screen)
		obj3.turn_counterclockwise = True

		# Добавляем в игру шрифт и создаем подписи для объектов
		font = pg.font.SysFont('Arial', 20, bold=True)

		text1 = font.render('Танк', True, [250, 250, 250])
		text1_rect = text1.get_rect()
		text1_rect.center = (self.screen_width//4, self.screen_height - self.screen_height//4)

		text2 = font.render('Грузовик', True, [250, 250, 250])
		text2_rect = text2.get_rect()
		text2_rect.center = (self.screen_width//2, self.screen_height - self.screen_height//4)

		text3 = font.render('в стиле NIUM', True, [250, 250, 250])
		text3_rect = text3.get_rect()
		text3_rect.center = (self.screen_width - self.screen_width//4, self.screen_height - self.screen_height//4)

		while True:
			for event in pg.event.get():
				if event.type == pg.QUIT:
					quit()
				if event.type == pg.KEYDOWN:
					if event.key == pg.K_ESCAPE:
						quit()

			#print(str(clock.get_fps()))

			# Изменяем угол поворота объектов
			obj1.rotate_me()
			obj2.rotate_me()
			obj3.rotate_me()

			screen.fill((50, 50, 50))

			# Выводим объекты на экран
			obj1.blit_me_3d()
			obj2.blit_me_3d()
			obj3.blit_me_3d()

			# Выводим подписи для объектов
			screen.blit(text1, text1_rect)
			screen.blit(text2, text2_rect)
			screen.blit(text3, text3_rect)

			pg.display.flip()
			clock.tick(self.fps)




if __name__ == '__main__':
	game = Game()
	game.run()
