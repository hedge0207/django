# django_self_pjt 2

- models.py에서 ForeignKey의 첫 번째 인자로 넘길 것이 없으면 settings를 넘겨야 한다.

  - models.CASCADE지 그냥 CASCADE가 아니다

  ```python
  from django.conf import settings
  
  class Review(models.Model):
      user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  ```

  

- forms.py를 만들 때에는 forms도 import 해야 한다.

  ```python
  from django import forms
  ```

  

- static 파일을 쓰려면 settings.py에 아래와 같이 입력해야 한다.

  ```python
  STATICFILES_DIRS = [
      os.path.join(BASE_DIR,'static')
  ]
  ```

  

- 로그인한 상태에서만 특정 내용을 보여주고 싶을 경우

  ```html
  {% if request.user.is_authenticated %}
  ```



- 실수들

  ```python
  #실수
  if reqeust.method="POST":
  
  #아래와 같이 쳐야함
  if reqeust.method=="POST":
  ```



- 로그인과 로그아웃  기본 로직

  ```python
  def login(request):
      if request.method=="POST":
          form=AuthenticationForm(request,request.POST)
          if form.is_valid():
              auth_login(request,form.get_user())
              return redirect('reviews:review_list')
      else:
          form=AuthenticationForm()
      context={
          'form':form
      }
      return render(request,'users/login.html',context)
  
  def logout(request):
      auth_logout(request)
      return redirect('reviews:review_list')
  ```

  

- 댓글 작성시 detail함수와 댓글 생성 함수

  ```python
  def detail(request,review_pk):
      review=get_object_or_404(Review,pk=review_pk)
      comments=review.comment_set.all()   #.comment_set.all()로 끌고 온다.
      form=CommentForm()
      context={
          'review':review,
          'comments':comments,
          'form':form
      }
      return render(request,'reviews/detail.html',context)
  
  
  def comment_create(request,review_pk):
      form=CommentForm(request.POST)
      review=get_object_or_404(Review,pk=review_pk)
      if form.is_valid():
          comment=form.save(commit=False)
          comment.review=review
          comment.user=request.user
          comment.save()
          return redirect('reviews:detail', review_pk)
  ```

  

- @login_required 가 있을 경우의 login 함수

  ```python
  def login(request):
      if request.method=="POST":
          form=AuthenticationForm(request,request.POST)
          if form.is_valid():
              auth_login(request,form.get_user())
              return redirect(request.GET.get('next') or 'reviews:review_list')
      else:
          form=AuthenticationForm()
      context={
          'form':form
      }
      return render(request,'users/login.html',context)
  ```

  

- @login_required를 쓸 때 settings.py에 설정된 경로대로 만들지 않았다면 settings.py에 아래의 문구를 추가해야 한다.

  ```python
  LOGIN_URL = '/앱이름/url이름/'
  ```

  