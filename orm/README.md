- shell_plus 사용 가능한 상태로 만들기
  - 설치 및 앱 등록
- 테이블 생성

```python
#models.py
class People(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    age = models.IntegerField()
    country = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    balance = models.IntegerField()
```

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

- 레코드 생성

```sql
People.objects.create(
	first_name='공자',
    last_name='김',
    age=44,
    country='대전',
    phone='010-1234-1234',
    balance=123456789
)
```

- 모든 레코드 조회

```python
people=People.objects.all()
```

- 특정 레코드 조회

```python
In [6]: People.objects.get(id=12)                                                                       
Out[6]: <People: People object (12)>
```

- 레코드 수정

```python
In [7]: people=People.objects.get(id=1)  

In [8]: people.last_name='홍'                                                                           
In [9]: people.save()  
```

- 레코드 삭제

```python
In [10]: People.objects.get(id=21).delete()                                                             
Out[10]: (1, {'people.People': 1})

In [12]: People.objects.get(id=22).delete()                                                             
Out[12]: (1, {'people.People': 1})

In [13]: People.objects.get(id=20).delete()                                                             
Out[13]: (1, {'people.People': 1})

# 확인
In [14]: People.objects.all()                                                                           
Out[14]: <QuerySet [<People: People object (1)>, <People: People object (2)>, <People: People object (3)>, <People: People object (4)>, <People: People object (5)>, <People: People object (6)>, <People: People object (7)>, <People: People object (8)>, <People: People object (9)>, <People: People object (10)>, <People: People object (11)>, <People: People object (12)>, <People: People object (13)>, <People: People object (14)>, <People: People object (15)>, <People: People object (16)>, <People: People object (17)>, <People: People object (18)>, <People: People object (19)>]>
 #원래 22번 object까지 있었으나 삭제됨 20~22는 삭제됨
```

- 전체 인원 수

```python
In [15]: People.objects.count()                                                                         
Out[15]: 19
```

- 나이가 47인 사람의 이름

```python
In [16]: People.objects.filter(age=47).values('first_name')                                             
Out[16]: <QuerySet [{'first_name': '수종'}]>
```

- 나이가 50 이상인 사람의 인원 수

```python
In [24]: People.objects.filter(age__gte=50).count()                                                     
Out[24]: 3
```

- 나이가 20 이상이면서 성이 박씨인 사람의 인원 수

```python
In [31]: People.objects.filter(age__gte=20).filter(last_name='박').count()                              
Out[31]: 4
```

- 나이가 20 이상이거나 성이 박씨인 사람의 인원 수

```python
In [29]: from django.db.models import Q

In [30]: People.objects.filter(Q(age__gte=20)|Q(last_name='박')).count()                                
Out[30]: 17
```

- 휴대폰 앞자리가 011인 사람의 인원 수

```python
In [32]: People.objects.filter(phone__startswith='011').count()                                         
Out[32]: 2
```

- 거주 지역이 대전 이면서 성이 최씨인 사람의 이름

```python
In [34]: People.objects.filter(country='대전').filter(last_name='최').values('first_name')              
Out[34]: <QuerySet [{'first_name': '수성'}]>
```

- 나이가 많은 사람 10명(내림차순)

```python
In [36]: People.objects.order_by('-age')[:10]                                                           
Out[36]: <QuerySet [<People: People object (11)>, <People: People object (15)>, <People: People object (12)>, <People: People object (19)>, <People: People object (3)>, <People: People object (2)>, <People: People object (7)>, <People: People object (6)>, <People: People object (8)>, <People: People object (16)>]>
```

- 잔액이 적은 사람 10명(오름차순)

```python
In [37]: People.objects.order_by('balance')[:10]                                                        
Out[37]: <QuerySet [<People: People object (4)>, <People: People object (13)>, <People: People object (1)>, <People: People object (9)>, <People: People object (2)>, <People: People object (5)>, <People: People object (10)>, <People: People object (18)>, <People: People object (17)>, <People: People object (19)>]>
```

- 성, 잔액 내림차순 순으로 5번째에 있는 사람

```python
In [38]: People.objects.order_by('-last_name','-first_name')[4]                                         
Out[38]: <People: People object (9)>
```

- 전체 평균 나이

```python
In [41]: People.objects.aggregate(Avg('age'))                                                           
Out[41]: {'age__avg': 36.473684210526315}
```

- 최씨의 평균 나이

```python
In [42]: People.objects.filter(last_name='최').aggregate(Avg('age'))                                    
Out[42]: {'age__avg': 43.75}
```

- 계좌 잔액 중 가장 높은 값

```python
In [43]: People.objects.aggregate(Max('balance'))                                                       
Out[43]: {'balance__max': 1511}
```

- 계좌 잔액 총액

```python
In [44]: People.objects.aggregate(Sum('balance'))                                                       
Out[44]: {'balance__sum': 10559}
```

- 지역별 인원 수

```python
In [45]: People.objects.values('country').annotate(Count('country'))                                    
Out[45]: <QuerySet [{'country': '강원', 'country__count': 2}, {'country': '경남', 'country__count': 1}, {'country': '경북', 'country__count': 2}, {'country': '광주', 'country__count': 1}, {'country': '대구', 'country__count': 1}, {'country': '대전', 'country__count': 2}, {'country': '부산', 'country__count': 1}, {'country': '서울', 'country__count': 2}, {'country': '울산', 'country__count': 1}, {'country': '인천', 'country__count': 1}, {'country': '전남', 'country__count': 2}, {'country': '전북', 'country__count': 1}, {'country': '제주', 'country__count': 2}]>
```

