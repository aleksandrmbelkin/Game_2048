# "Игра 2048"
## Структура проекта:
### data
В этой папке находятся всё данные, используемые в проекте.  
       
__Папка разделена на 3 основных раздела:__  
      
   #### I. __locations__
       
   В этой папке хранятся расположения клеток на игровом поле для каждого вида поля.  
        
    - loc_4x4.csv - расположение клеток для поля 4 на 4.
    - loc_5x5.csv - расположение клеток для поля 5 на 5.
    - loc_6x6.csv - расположение клеток для поля 6 на 6.
    - loc_8x8.csv - расположение клеток для поля 8 на 8.
       
      
   #### II. __pictures__  

  В этой папке хранятся изображения.   
            
  __Папка разделена на 4 раздела:__  
   1. __buttons__  
         
   В этой папке хранятся изображения для кнопок.   
            
      - back.png - изображение для кнопок назад.
      - down.png - изображение для кнопки вниз.
      - exit.png - изображение для кнопки выход.
      - left.png - изображение для кнопки влево.
      - move_back.png - изображение для кнопки шаг назад.
      - no.png - изображение для кнопки нет.
      - play.png - изображение для кнопки играть.
      - records.png - изображение для кнопки рекорды.
      - restart.png - изображение для кнопки сначала.
      - right.png - изображение для кнопки вправо.
      - up.png - изображение для кнопки вверх.
      - yes.png - изображение для кнопки да.
        
   2. __cells__
        
   В этой папке хранятся изображения для клеток.   
          
      - cell_1024.png - изображение для клетки 1024.
      - cell_128.png - изображение для клетки 128.
      - cell_16.png - изображение для клетки 16.
      - cell_16384.png - изображение для клетки 16384.
      - cell_2.png - изображение для клетки 2.
      - cell_2048.png - изображение для клетки 2048.
      - cell_256.png - изображение для клетки 256.
      - cell_32.png - изображение для клетки 32.
      - cell_32768.png - изображение для клетки 32768.
      - cell_4.png - изображение для клетки 4.
      - cell_4096.png - изображение для клетки 4096.
      - cell_512.png - изображение для клетки 512.
      - cell_64.png - изображение для клетки 64.
      - cell_8.png - изображение для клетки 8.
      - cell_8192.png - изображение для клетки 8192.
      
   3. __design__
     
   В этой папке хранятся дополнительные изображения для дизайна.   
           
      - logo_2048.png - изображение для иконки игры. 
      - title.jpg - изображение для заголовка. 
       
   4. __examples_of_fields__
    
   В этой папке хранятся изображения примеров игровых полей.   
         
      - 4x4.jpg - пример игрового поля 4 на 4.
      - 5x5.jpg - пример игрового поля 4 на 4.
      - 6x6.jpg - пример игрового поля 4 на 4.
      - 8x8.jpg - пример игрового поля 4 на 4.
         
   #### III. __records__  
       
   В этой папке изображения рекорды, добавляющиеся по мере игры.

      - rec_4x4.csv - рекорды для поля 4 на 4.
      - rec_5x5.csv - рекорды для поля 5 на 5.
      - rec_6x6.csv - рекорды для поля 6 на 6.
      - rec_8x8.csv - рекорды для поля 8 на 8.
            
            
            
### src
В этой папке находится исходный код игры и дизайны из QtDesigner.

__Папка разделена на 2 основных раздела:__   
   
   #### I. __python_files__    
   
   В этой папке хранятся __pycache__ и исходный код игры.

      - __pycache__ - хранит скомпилированные версии моих скриптов.
      - game.py - исходный код для окна "Game"  
      - main.py - исходный код для окна "Main"  
      - records.py - исходный код для окна "Records"  

   #### II. __ui_files__    

   В этой папке хранятся дизайны из QtDesigner.

      - game.ui - дизайн окна "Game"  
      - main.ui - дизайн окна "Main"  
      - records.ui - дизайн окна "Records"  
     
     
     
## Логика связи классов:
Классы лежат в разных файлах. Есть главный класс - Main, лежащий в файле main.py, в этот файл импортируются классы Records из файла records.py и класс Game из файла game.py.
Поэтому, при нажатии кнопки для открытия другого окна, вызываются импортированные классы Game или Records. Если же пользователь хочет перейти обратно в главное окно, то, при нажатии кнопки, программа будем заного запускать программу main.py, закрывая предыдущую.





      
   

    
   
