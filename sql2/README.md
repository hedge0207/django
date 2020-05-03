- 모든 레코드 조회

```sql
sqlite> select * from people;
id | first_name | last_name | age | country | phone | balance
1 | 병철 | 김 | 21 | 대전 | 010-7845-9865 | 120
2 | 성민 | 최 | 44 | 광주 | 010-8787-9898 | 220
3 | 병만 | 김 | 46 | 서울 | 011-1122-2233 | 480
4 | 우시 | 박 | 17 | 대구 | 010-9898-6565 | 10
5 | 은경 | 서 | 22 | 부산 | 010-7874-1251 | 220
6 | 핸재 | 박 | 38 | 울산 | 010-7814-6895 | 854
7 | 지현 | 최 | 41 | 인천 | 011-7548-2351 | 488
8 | 보람 | 송 | 37 | 서울 | 010-4814-6252 | 785
9 | 수성 | 최 | 12 | 대전 | 010-4822-4777 | 123
10 | 도윤 | 박 | 22 | 강원 | 010-9898-5465 | 284
11 | 희경 | 최 | 78 | 경북 | 019-7854-7855 | 1201
12 | 고은 | 박 | 51 | 경남 | 010-8854-2144 | 1511
13 | 영식 | 이 | 31 | 전남 | 010-7825-7845 | 100
14 | 승배 | 한 | 18 | 제주 | 010-7878-8884 | 1253
15 | 우진 | 이 | 68 | 제주 | 010-7115-6546 | 1110
16 | 예은 | 박 | 36 | 강원 | 010-1213-4754 | 750
17 | 예지 | 송 | 31 | 경북 | 010-3541-4778 | 330
18 | 호영 | 김 | 33 | 전북 | 010-8554-4787 | 310
19 | 수종 | 김 | 47 | 전남 | 010-7848-1118 | 410
20 | 재민 | 박 | 39 | 대구 | 010-7414-2455 | 840
```

- 레코드 추가

```sql
--추가
sqlite> insert into people ('first_name', 'last_name', 'age', 'country', 'phone', 'balance') values('시현','최',35,'울산','010-4669-5887',123456);

--확인
sqlite> select * from people where first_name='시현';                              
id | first_name | last_name | age | country | phone | balance
21 | 시현 | 최 | 35 | 울산 | 010-4669-5887 | 123456
```

- 특정 레코드 조회

```sql
sqlite> select * from people where id=2;
id | first_name | last_name | age | country | phone | balance
2 | 성민 | 최 | 44 | 광주 | 010-8787-9898 | 220
```

- 레코드 수정

```sql
--수정
sqlite> update people set country='대전' where first_name='호영' ;

--확인
sqlite> select * from people where first_name='호영';
id | first_name | last_name | age | country | phone | balance
18 | 호영 | 김 | 33 | 대전 | 010-8554-4787 | 310
```

- 레코드 삭제

```sql
--삭제
sqlite> delete from people where first_name='시현';

--확인
sqlite> select * from people;
id | first_name | last_name | age | country | phone | balance
1 | 병철 | 김 | 21 | 대전 | 010-7845-9865 | 120
2 | 성민 | 최 | 44 | 광주 | 010-8787-9898 | 220
3 | 병만 | 김 | 46 | 서울 | 011-1122-2233 | 480
4 | 우시 | 박 | 17 | 대구 | 010-9898-6565 | 10
5 | 은경 | 서 | 22 | 부산 | 010-7874-1251 | 220
6 | 핸재 | 박 | 38 | 울산 | 010-7814-6895 | 854
7 | 지현 | 최 | 41 | 인천 | 011-7548-2351 | 488
8 | 보람 | 송 | 37 | 서울 | 010-4814-6252 | 785
9 | 수성 | 최 | 12 | 대전 | 010-4822-4777 | 123
10 | 도윤 | 박 | 22 | 강원 | 010-9898-5465 | 284
11 | 희경 | 최 | 78 | 경북 | 019-7854-7855 | 1201
12 | 고은 | 박 | 51 | 경남 | 010-8854-2144 | 1511
13 | 영식 | 이 | 31 | 전남 | 010-7825-7845 | 100
14 | 승배 | 한 | 18 | 제주 | 010-7878-8884 | 1253
15 | 우진 | 이 | 68 | 제주 | 010-7115-6546 | 1110
16 | 예은 | 박 | 36 | 강원 | 010-1213-4754 | 750
17 | 예지 | 송 | 31 | 경북 | 010-3541-4778 | 330
18 | 호영 | 김 | 33 | 대전 | 010-8554-4787 | 310
19 | 수종 | 김 | 47 | 전남 | 010-7848-1118 | 410
20 | 재민 | 박 | 39 | 대구 | 010-7414-2455 | 840
```

- 전체 레코드 수

```sql
sqlite> select count(*) from people;
count(*)
20
```

- 나이가 47인 사람의 이름

```sql
sqlite> select first_name from people where age=47;
first_name
수종
```

- 나이가 50 이상인 사람의 인원 수

```sql
sqlite> select count(*) from people where age>=50;
count(*)
3
```

- 나이가 20 이상이면서 성이 박씨인 사람의 인원 수

```sql
select count(*) from people where age>=20 and last_name='박';

sqlite> select count(*) from people where age>=20 and last_name='박';
count(*)
5
```

- 휴대폰 앞자리가 011인 사람의 인원 수

```sql
sqlite> select count(*) from people where phone like '011-%';
count(*)
2
```

- 거주 지역이 대전 이면서 성이 최씨인 사람의 이름

```sql
sqlite> select first_name from people where last_name='최' and country='대전';
first_name
수성
```

- 나이가 많은 사람 10명(내림차순)

```sql
sqlite> select * from people order by age desc limit 10;
id | first_name | last_name | age | country | phone | balance
11 | 희경 | 최 | 78 | 경북 | 019-7854-7855 | 1201
15 | 우진 | 이 | 68 | 제주 | 010-7115-6546 | 1110
12 | 고은 | 박 | 51 | 경남 | 010-8854-2144 | 1511
19 | 수종 | 김 | 47 | 전남 | 010-7848-1118 | 410
3 | 병만 | 김 | 46 | 서울 | 011-1122-2233 | 480
2 | 성민 | 최 | 44 | 광주 | 010-8787-9898 | 220
7 | 지현 | 최 | 41 | 인천 | 011-7548-2351 | 488
20 | 재민 | 박 | 39 | 대구 | 010-7414-2455 | 840
6 | 핸재 | 박 | 38 | 울산 | 010-7814-6895 | 854
8 | 보람 | 송 | 37 | 서울 | 010-4814-6252 | 785
```

- 잔액이 적은 사람 10명(오름차순)

```sql
sqlite> select * from people order by balance limit 10;
id | first_name | last_name | age | country | phone | balance
4 | 우시 | 박 | 17 | 대구 | 010-9898-6565 | 10
13 | 영식 | 이 | 31 | 전남 | 010-7825-7845 | 100
1 | 병철 | 김 | 21 | 대전 | 010-7845-9865 | 120
9 | 수성 | 최 | 12 | 대전 | 010-4822-4777 | 123
2 | 성민 | 최 | 44 | 광주 | 010-8787-9898 | 220
5 | 은경 | 서 | 22 | 부산 | 010-7874-1251 | 220
10 | 도윤 | 박 | 22 | 강원 | 010-9898-5465 | 284
18 | 호영 | 김 | 33 | 대전 | 010-8554-4787 | 310
17 | 예지 | 송 | 31 | 경북 | 010-3541-4778 | 330
19 | 수종 | 김 | 47 | 전남 | 010-7848-1118 | 410
```

- 성, 잔액 내림차순 순으로 5번째에 있는 사람

```sql
sqlite> select * from people order by first_name desc, balance desc limit 1 offset 4;
id | first_name | last_name | age | country | phone | balance
20 | 재민 | 박 | 39 | 대구 | 010-7414-2455 | 840
```

- 전체 평균 나이

```sql
sqlite> select avg(age) from people;
avg(age)
36.6
```

- 최씨의 평균 나이

```sql
sqlite> select avg(age) from people where last_name='최';
avg(age)
43.75
```

- 계좌 잔액 중 가장 높은 값

```sql
sqlite> select max(balance) from people;
max(balance)
1511
```

- 계좌 잔액 총액

```sql
sqlite> select sum(balance) from people;
sum(balance)
11399
sqlite> 
```

- 지역별 인원 수

```sql
sqlite> select country, count(country) from people group by country;
country | count(country)
강원 | 2
경남 | 1
경북 | 2
광주 | 1
대구 | 2
대전 | 3
부산 | 1
서울 | 2
울산 | 1
인천 | 1
전남 | 2
제주 | 2
```



