# 어려웠던 점

- 좋아요 기능을 구현하는데 시간이 굉장히 오래 걸렸다.

  - 처음에는 로그인 하지 않은 상태로 좋아요 버튼을 눌러 아래 에러가 발생했다.

    > int() argument must be a string, a bytes-like object or a number, not 'SimpleLazyObject'

    - 좋아요를 구현한 코드는 다음과 같다.

    ```python
    def like(request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        if article.like_users.filter(id=request.user.pk).exists():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
        return redirect('memories:detail', article.pk)
    ```

    - 로그인을 하지 않은 상태이므로 위 코드에서 `request.user`에 유저 정보가 들어갈 수 없었고 이로인해 에러가 발생했다. 이후 상단에 `@login_required`를 붙여 해결했다.

  - 다음에는 코드 자체를 이해하지 못하고 교수님의 코드를 따라치다 발생한 에러로 에러가 발생한 코드는 다음과 같다.

    ```html
    {% if request.user in article.like_users %}
    <a href="{% url 'memories:like' article.pk %}"><i class="fas fa-heart" style='color:red'></i></a>
    {% else %}
    <a href="{% url 'memories:like' article.pk %}"><i class="far fa-heart" style='color:red'></i></a>
    {% endif %}
    <p>{{ article.like_users.all|length }}명이 좋아합니다.</p>
    
    <!--{% if request.user in article.like_users %}가 아닌 {% if request.user in article.like_users %}를 입력해야 했으나 교수님의 코드를 따라치는 과정에서 잘못 입력하여 좋아요를 한 유저의 수가 증가는 하는데 하트 표시가 바뀌지는 않는 에러가 발생했다. 이후 코드를 충분히 이해한 후에 수정함으로써 고칠 수 있었다.-->
    ```

  - 마지막으로 함수가 잘못된 것은 아닌지 확인하던 중 `remove`부분을 지웠던 것을 깜빡하여 아무리 좋아요 취소를 눌러도 `remove`가 되지 않았던 문제가 있었다.

    ```python
    @login_required
    def like(request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        article.like_users.add(request.user)
        return redirect('memories:detail', article.pk)
    ```

    - 평소같으면 금방 찾았을 오류였지만 이미 앞의 두 문제로 집중력이 떨어져 이 문제를 해결하는데도 오랜 시간이 걸렸다.

  - 개선사항: 코드로 구현한 후 작동하는 것을 보면서 이해하려 하지 말고 이해하고 구현할 것, 집중력이 떨어졌다면 잠시 쉴 것



# 알게된 점

- `forms.py`에 대해 여러 사실을 새롭게 알게 되었고 잘못 알고 있었던 것들을 바로 알게 되었다.

  - `models.py`에서 모델을 새로 생성하거나 모델에 새로운 필드를 추가할 경우 migrate를 해야 하지만 이미 생성된 필드의 속성을 바꿀 때에는 추가적인 migrate가 필요 없는 것으로 보인다.

  ```python
  class MyUser(AbstractUser):
      family_followers = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='family_followings')
      father = models.CharField(max_length=30)
      mather = models.CharField(max_length=30)
      child = models.CharField(max_length=30,blank=True)
  #위와 같이 모델을 정의하고 migrate를 한 후
  
  
  class MyUser(AbstractUser):
      family_followers = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='family_followings')
      father = models.CharField(max_length=30)
      mather = models.CharField(max_length=30)
      child = models.CharField(max_length=30,blank=True,help_text="자식이 없을 경우 입력하지 말아주세요")
#위와 같이 코드를 수정하고 migrate를 하지 않았음에도 help_text가 표시됐다.
  ```
  
- `Meta`클래스 밖에 정의한 것들(이하 form클래스 내부에 정의한 것들)은 `Meta`클래스 내부의 `fields` 리스트에 넣지 않아도 된다고 생각했는데, 넣지 않아도 되는 것이 아니라 넣을 수 없는 것이다. 애초에 `Meta`클래스는 `models.py`에서 정의한 모델 중 하나를 선택해 그 모델의 내부에 정의한 필드들 중 어떤 것들을 form으로 나타낼 것인지를 선택한 것인데 form클래스 내부에 정의한 것들은 `models.py`에서 정의한 모델의 필드가 아니므로 `Meta`클래스 내부의 `fields`에 넣을 수가 없다.
  - 만일 form클래스 내부에 정의한 것과 `Meta`클래스의 `fields`리스트에 들어간 필드명이 동일할 경우 form클래스 내부에 정의한 것이 form에서 표현된다.
  
    ```python
    class MyUser(AbstractUser):
        family_followers = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='family_followings')
        father = models.CharField(max_length=30)
        mather = models.CharField(max_length=30)
        child = models.CharField(max_length=30,blank=True)
        
    
    class MyUserCreationForm(UserCreationForm):
        child = forms.CharField(
                    max_length=30,
                    help_text="자식이 없을 경우 입력하지 말아주세요",
                )
        class Meta:
            model = get_user_model()
            fields = ['username','father','mather']
    #위 코드에 따라 회원가입을 진행할 경우 "자식이 없을 경우 입력하지 말아주세요"라는 help_text는 뜨는데 MyUser의 child에 정의된 blank=True는 적용되지 않았다.
    
    #또한 아래와 같이 form을 변경할 경우에도 여전히 help_text는 뜨는데 MyUser의 child에 정의된 blank=True는 적용되지 않았다. 따라서 form 클래스 내부에 정의된 child가 넘어갔음을 알 수 있다.
    class MyUserCreationForm(UserCreationForm):
        child = forms.CharField(
                    max_length=30,
                    help_text="자식이 없을 경우 입력하지 말아주세요",
                )
        class Meta:
            model = get_user_model()
            fields = ['username','father','mather','child']
    ```





# 추가적인 확인이 필요한 점

- 새롭게 알게된점에서 적은 내용을 다시 천천히 해볼 필요가 있을 것 같다.

  - 예를 들면 form 클래스 내부에 정의한 필드와 동일한 이름의 필드가 fields 리스트로 넘길 때뿐만 아니라 `'__all__'`로 넘길 때에도 우선적으로 넘어가는지를 확인해 볼 필요가 있을 것 같다.

  ```python
  #즉, 아래의 경우에도 form 클래스 내부에 정의한 필드가 먼저 넘어가는지 확인
  #단, 아래와 같은 User 모델은 모델 내부에 정의된 것이 너무 많으므로 모델을 하나 만들어서 해볼 것
  class MyUser(AbstractUser):
      family_followers = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='family_followings')
      father = models.CharField(max_length=30)
      mather = models.CharField(max_length=30)
      child = models.CharField(max_length=30,blank=True)
      
  
  class MyUserCreationForm(UserCreationForm):
      child = forms.CharField(
                  max_length=30,
                  help_text="자식이 없을 경우 입력하지 말아주세요",
              )
      class Meta:
          model = get_user_model()
          fields = '__all__'
  ```

  





# 추가해야 할 기능

- login_required
- message



# 추가하고 싶은 기능

- 회원가입 시 자동으로 로그인 되는 기능
- 여러개의 이미지를 추가하는 기능

