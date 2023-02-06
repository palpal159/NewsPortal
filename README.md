<<<<<<< HEAD
# Команды для запуска в Django chell:

1. Создать двух пользователей:

     > user1 = User.objects.create_user(username = "Petr", password = "1234")
    
     > user2 = User.objects.create_user(username = "Ivan", password = "4321")
   

2. Создать два объекта модели Author, связанные с пользователями:

     > author1 = Author.objects.create(user = user1)
    
     > author2 = Author.objects.create(user = user2) 

3. Добавить 4 категории в модель Category: 

     > category1 = Category.objects.create(category = "Health")
    
     > category2 = Category.objects.create(category = "Travel") 
      
     > category3 = Category.objects.create(category = "Food")
    
     > category4 = Category.objects.create(category = "Lifestyle")

4. Добавить 2 статьи и 1 новость: 

     > article1 = Post.objects.create(post = Post.article, header_post = "10 мест, ради которых стоит проснуться на рассвете", text_post = "Итак, вы в    Питере. Раннее утро. Лед с рек и каналов уже ушел, запущены фонтаны города… Музеи еще закрыты. Что посмотреть?", author = author1)
    
     > article2 = Post.objects.create(post = Post.article, header_post = "Йога для начинающих в домашних условиях", text_post = "Расскажем, какие упражнения выбрать и как сделать коврик для занятий йогой из того, что можно найти в шкафу.", author = author2) 
      
     > news1 = Post.objects.create(post = Post.news, header_post = "Лучшие музыкальные фестивали этого лета", text_post = "Лето на носу, а с ним и музыкальные фестивали. На каком же из них вы разобьёте свою палатку? Мы составили список лучших летних фестивалей по всему миру.", author = author2)
    

5. Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий): 

    > helth = Category.objects.all()[0]
    > , travel = Category.objects.all()[1]
    > , food = Category.objects.all()[2]
    > , lifestyle = Category.objects.all()[3]
    
    > article1.category.add(helth)
    > , article1.category.add(travel)

    > article2.category.add(helth)

    > news1.category.add(lifestyle)

6. Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий): 

     > comment1 = Comment.objects.create(comment_text = "Крутая подборка!", post = article1, user = user1)

     > comment2 = Comment.objects.create(comment_text = "Хочу посеть эти места", post = article1, user = user2)

     > comment3 = Comment.objects.create(comment_text = "Люблю Питер!", post = article1, user = user1)

     > comment4 = Comment.objects.create(comment_text = "Йога - классная форма релакса!", post = article2, user = user1)

     > comment5 = Comment.objects.create(comment_text = "Давно хотел начать заниматься дома", post = article2, user = user2)

     > comment6 = Comment.objects.create(comment_text = "Ю-хуу тусовка!", post = news1, user = user1)

     > comment7 = Comment.objects.create(comment_text = "Даешь больше фестов!", post = news1, user = user2)
 

7. Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов: 

    > article1.like_post()
    > , article1.like_post()
    > , article1.like_post()
    > , article1.like_post()
    > , article1.like_post()
    > , article1.like_post()
    > , article1.dislike_post()
    > , article1.dislike_post() 

    > article2.like_post()
    > , article2.like_post()
    > , article2.like_post()
    > , article2.dislike_post()

    > news1.like_post()
    > , news1.like_post()
    > , news1.like_post()

    > comment1.like_comment()
    > , comment1.like_comment()
    > , comment1.like_comment()
    > , comment1.like_comment()
    > , comment1.like_comment()
    > , comment1.like_comment()
    > , comment1.like_comment()
    > , comment1.like_comment()
    > , comment1.like_comment()
    > , comment1.like_comment()
    > , comment1.dislike_comment()
    > , comment1.dislike_comment()
    > , comment1.dislike_comment()

    > comment2.like_comment()
    > , comment2.like_comment()
    > , comment2.like_comment()
    > , comment2.like_comment()
    > , comment2.like_comment()
    > , comment2.like_comment()
    > , comment2.like_comment()
    > , comment2.dislike_comment()
    > , comment2.dislike_comment()
    > , comment2.dislike_comment()
    > , comment2.dislike_comment()

    > comment3.like_comment()
    > , comment3.like_comment()
    > , comment3.like_comment()

    > comment4.like_comment()
    > , comment4.like_comment()
    > , comment4.dislike_comment()

    > comment5.like_comment()
    > , comment5.like_comment()
    > , comment5.like_comment()
    > , comment5.like_comment()
    > , comment5.like_comment()
    > , comment5.like_comment()
    > , comment5.dislike_comment()
    > , comment5.dislike_comment()
    > , comment5.dislike_comment()

    > comment6.like_comment()
    > , comment6.like_comment()
    > , comment6.like_comment()
    > , comment6.like_comment()
    > , comment6.like_comment()
    
    > comment7.like_comment()
    > , comment7.like_comment()
    > , comment7.like_comment()
    > , comment7.like_comment()
    > , comment7.like_comment()
    > , comment7.like_comment()
    > , comment7.like_comment()
    > , comment7.like_comment()
    > , comment7.like_comment()
    > , comment7.like_comment()
    > , comment7.dislike_comment()
    > , comment7.dislike_comment()
    > , comment7.dislike_comment()
    > , comment7.dislike_comment()


8. Обновить рейтинги пользователей: 

    > author1.update_rating()

    > author2.update_rating() 

9. Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта): 

    > Author.objects.filter(rating_author__gt = 42).values('user', 'rating_author')


10. Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье: 

    > Post.objects.filter(rating_post__gt = 3).values('post_date', 'author', 'rating_post', 'header_post')
    
    > article1.preview() 

11. Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье: 

    > Comment.objects.filter(post_id = 1).values('comment_date', 'user', 'rating_comment', 'comment_text') 
=======
# Команды для запуска в Django chell:

1. Создать двух пользователей:

     > user1 = User.objects.create_user(username = "Petr", password = "1234")
    
     > user2 = User.objects.create_user(username = "Ivan", password = "4321")
   

2. Создать два объекта модели Author, связанные с пользователями:

     > author1 = Author.objects.create(user = user1)
    
     > author2 = Author.objects.create(user = user2) 

3. Добавить 4 категории в модель Category: 

     > category1 = Category.objects.create(category = "Health")
    
     > category2 = Category.objects.create(category = "Travel") 
      
     > category3 = Category.objects.create(category = "Food")
    
     > category4 = Category.objects.create(category = "Lifestyle")

4. Добавить 2 статьи и 1 новость: 

     > article1 = Post.objects.create(post = Post.article, header_post = "10 мест, ради которых стоит проснуться на рассвете", text_post = "Итак, вы в    Питере. Раннее утро. Лед с рек и каналов уже ушел, запущены фонтаны города… Музеи еще закрыты. Что посмотреть?", author = author1)
    
     > article2 = Post.objects.create(post = Post.article, header_post = "Йога для начинающих в домашних условиях", text_post = "Расскажем, какие упражнения выбрать и как сделать коврик для занятий йогой из того, что можно найти в шкафу.", author = author2) 
      
     > news1 = Post.objects.create(post = Post.news, header_post = "Лучшие музыкальные фестивали этого лета", text_post = "Лето на носу, а с ним и музыкальные фестивали. На каком же из них вы разобьёте свою палатку? Мы составили список лучших летних фестивалей по всему миру.", author = author2)
    

5. Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий): 

    > helth = Category.objects.all()[0]
    > , travel = Category.objects.all()[1]
    > , food = Category.objects.all()[2]
    > , lifestyle = Category.objects.all()[3]
    
    > article1.category.add(helth)
    > , article1.category.add(travel)

    > article2.category.add(helth)

    > news1.category.add(lifestyle)

6. Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий): 

     > comment1 = Comment.objects.create(comment_text = "Крутая подборка!", post = article1, user = user1)

     > comment2 = Comment.objects.create(comment_text = "Хочу посеть эти места", post = article1, user = user2)

     > comment3 = Comment.objects.create(comment_text = "Люблю Питер!", post = article1, user = user1)

     > comment4 = Comment.objects.create(comment_text = "Йога - классная форма релакса!", post = article2, user = user1)

     > comment5 = Comment.objects.create(comment_text = "Давно хотел начать заниматься дома", post = article2, user = user2)

     > comment6 = Comment.objects.create(comment_text = "Ю-хуу тусовка!", post = news1, user = user1)

     > comment7 = Comment.objects.create(comment_text = "Даешь больше фестов!", post = news1, user = user2)
 

7. Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов: 

    > article1.like_post()
    > , article1.like_post()
    > , article1.like_post()
    > , article1.like_post()
    > , article1.like_post()
    > , article1.like_post()
    > , article1.dislike_post()
    > , article1.dislike_post() 

    > article2.like_post()
    > , article2.like_post()
    > , article2.like_post()
    > , article2.dislike_post()

    > news1.like_post()
    > , news1.like_post()
    > , news1.like_post()

    > comment1.like_comment()
    > , comment1.like_comment()
    > , comment1.like_comment()
    > , comment1.like_comment()
    > , comment1.like_comment()
    > , comment1.like_comment()
    > , comment1.like_comment()
    > , comment1.like_comment()
    > , comment1.like_comment()
    > , comment1.like_comment()
    > , comment1.dislike_comment()
    > , comment1.dislike_comment()
    > , comment1.dislike_comment()

    > comment2.like_comment()
    > , comment2.like_comment()
    > , comment2.like_comment()
    > , comment2.like_comment()
    > , comment2.like_comment()
    > , comment2.like_comment()
    > , comment2.like_comment()
    > , comment2.dislike_comment()
    > , comment2.dislike_comment()
    > , comment2.dislike_comment()
    > , comment2.dislike_comment()

    > comment3.like_comment()
    > , comment3.like_comment()
    > , comment3.like_comment()

    > comment4.like_comment()
    > , comment4.like_comment()
    > , comment4.dislike_comment()

    > comment5.like_comment()
    > , comment5.like_comment()
    > , comment5.like_comment()
    > , comment5.like_comment()
    > , comment5.like_comment()
    > , comment5.like_comment()
    > , comment5.dislike_comment()
    > , comment5.dislike_comment()
    > , comment5.dislike_comment()

    > comment6.like_comment()
    > , comment6.like_comment()
    > , comment6.like_comment()
    > , comment6.like_comment()
    > , comment6.like_comment()
    
    > comment7.like_comment()
    > , comment7.like_comment()
    > , comment7.like_comment()
    > , comment7.like_comment()
    > , comment7.like_comment()
    > , comment7.like_comment()
    > , comment7.like_comment()
    > , comment7.like_comment()
    > , comment7.like_comment()
    > , comment7.like_comment()
    > , comment7.dislike_comment()
    > , comment7.dislike_comment()
    > , comment7.dislike_comment()
    > , comment7.dislike_comment()


8. Обновить рейтинги пользователей: 

    > author1.update_rating()

    > author2.update_rating() 

9. Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта): 

    > Author.objects.filter(rating_author__gt = 42).values('user', 'rating_author')


10. Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье: 

    > Post.objects.filter(rating_post__gt = 3).values('post_date', 'author', 'rating_post', 'header_post')
    
    > article1.preview() 

11. Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье: 

    > Comment.objects.filter(post_id = 1).values('comment_date', 'user', 'rating_comment', 'comment_text') 
>>>>>>> 97880375e970ad707278d2cc47e0645787bbbf31
