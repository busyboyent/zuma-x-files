Игра "Zuma"

Автор: Матушкин Никита

Описание:

Данное приложение является реализацией игры "Zuma"
Требования:

1)Python версии ни ниже 3.7.4
2)Pygame последней версии
3)requirements

Запуск: 

./main.py

Управление:

Рядом с лягушкой показан шарик, который заряжен в данный момент
Игрок вращается за положением мыши

Клавиши:

Пробел = выстрел(если зажать то можно стрелять очередью)

Подробности реализации: 

Файл main.py содержит в себе игровой цикл
player.py описывает взаимодействия с лягушкой и наследует от шаров
		  логику шарика, которым плюется лягушка
constant.py содержит все константы используемые в проекте,
			в том числе графическое оформление окна pygame
ball.py описывает логику шаров
skull.py описывает логику "поедающей головы"
game.py объединяет в себе логику поведения шаров, проверяет наличие цепочек
        шаров одинакового цвета, отрисовывает игровое окно
В папке images находятся все графические изображения
в папке sounds находятся все используемые композиции