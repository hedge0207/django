# SQLite 연습1

```
data.csv
1,홍길동,78,부산,남성
2,홍시우,48,대구,남성
3,최하윤,48,대구,여성
4,홍민준,20,대전,남성
5,홍지유,24,광주,여성
6,김하준,27,광주,남성
7,김옥연,71,광주,여성
8,최시우,44,대전,남성
9,박하은,42,대전,여성
10,최민준,18,대전,남성
```



- CRUD

```sql
--sqlite 시작
$ sqlite3 db.sqlite3

--family table 생성
sqlite> create table family (
   ...> id integer primary key autoincrement,
   ...> name text not null,
   ...> age integer not null,
   ...> address text,
   ...> gender text);

--데이터 추가
sqlite> .mode csv
sqlite> .separator ','
sqlite> .import data.csv family

--확인
sqlite> select * from family;
id,name,age,address,gender
1,"홍길동",78,"부산","남성"
2,"홍시우",48,"대구","남성"
3,"최하윤",48,"대구","여성"
4,"홍민준",20,"대전","남성"
5,"홍지유",24,"광주","여성"
6,"김하준",27,"광주","남성"
7,"김옥연",71,"광주","여성"
8,"최시우",44,"대전","남성"
9,"박하은",42,"대전","여성"
10,"최민준",18,"대전","남성"

--데이터 추가
sqlite> insert into family values (11,'박경원',45,'창원','여성');
sqlite> insert into family values (12,'이승찬',34,'양산','남성');
sqlite> insert into family values (13,'강아지',12,'양산','남성');
sqlite> insert into family values (14,'고양이',11,'인천','여성');

--확인
sqlite> select * from family;
id,name,age,address,gender
1,"홍길동",78,"부산","남성"
2,"홍시우",48,"대구","남성"
3,"최하윤",48,"대구","여성"
4,"홍민준",20,"대전","남성"
5,"홍지유",24,"광주","여성"
6,"김하준",27,"광주","남성"
7,"김옥연",71,"광주","여성"
8,"최시우",44,"대전","남성"
9,"박하은",42,"대전","여성"
10,"최민준",18,"대전","남성"
11,"박경원",45,"창원","여성"
12,"이승찬",34,"양산","남성"
13,"강아지",12,"양산","남성"
14,"고양이",11,"인천","여성"

--데이터 삭제
sqlite> delete from family where id=13;
sqlite> delete from family where id=14;

--확인
sqlite> select * from family;
id,name,age,address,gender
1,"홍길동",78,"부산","남성"
2,"홍시우",48,"대구","남성"
3,"최하윤",48,"대구","여성"
4,"홍민준",20,"대전","남성"
5,"홍지유",24,"광주","여성"
6,"김하준",27,"광주","남성"
7,"김옥연",71,"광주","여성"
8,"최시우",44,"대전","남성"
9,"박하은",42,"대전","여성"
10,"최민준",18,"대전","남성"
11,"박경원",45,"창원","여성"
12,"이승찬",34,"양산","남성"

--데이터 수정
sqlite> update family set age=22 where name="홍민준";

--확인
sqlite> select * from family where name="홍민준";
id,name,age,address,gender
4,"홍민준",22,"대전","남성
```



- 쿼리문

```sql
--전체 인원 수 조회
sqlite> select count(*) from family;
count(*)
12

--평균 연령
sqlite> select avg(age) from family;
avg(age)
41.75

--연령 합계
sqlite> select sum(age) from family;
sum(age)
501

--최고령
sqlite> select max(age) from family;
max(age)
78

--최연소
sqlite> select min(age) from family;
min(age)
18

--나이가 40 이상인 사람의 이름
sqlite> select name from family where age>=40;
name
"홍길동"
"홍시우"
"최하윤"
"김옥연"
"최시우"
"박하은"
"박경원"

--나이가 40 이상이면서 성별이 남성인 사람의 수
sqlite> select count(*) from family where age>=40 and gender='남성';
count(*)
3

--성이 홍씨인 사람의 수
sqlite> select count(*) from family where name like '홍%';
count(*)
4

--거주 지역이 대전이면서 성이 홍씨인 사람의 이름
sqlite> select name from family where name like '홍%' and address='대전'
name
"홍민준"

--나이가 어린 사람 3명(오름차순)
sqlite> select age,name from family order by age asc limit 3;
age,name
18,"최민준"
22,"홍민준"
24,"홍지유"

--나이가 많은 사람 3명(내림차순)
sqlite> select age,name from family order by age desc limit 3;
age,name
78,"홍길동"
71,"김옥연"
48,"홍시우"  --동갑인 최하윤이 아닌 홍시우가 들어간 이유(db등록순?)

--나이가 내림차순 순으로 3번째 있는 사람
sqlite> select name from family order by age desc limit 1 offset 2;
name
"홍시우"
```



- gruop by

```sql
--지역별 인원수
select address, count(address) from family group by address
sqlite> select address, count(address) from family group by address;
address,count(address)
"광주",3
"대구",2
"대전",4
"부산",1
"양산",1
"창원",1
```



- review
  - 처음 데이터 추가시에 `attempt to write a readonly database` 에러 발생, 이후 터미널 종료 후 다시 실행해보니 정상적으로 추가 되었음

    - c9의 오류로 보임

  - offset, gruop by 정리

    - 정리 완료

  - 나이가 많은 사람 3명(내림차순)을 했을 때 동갑인 최하윤도 있는데 홍시우가 들어간 이유
  
    - 등록순?,  id순?
  
    ```sql
    --데이터를 아래와 같이(홍시우와 최하윤의 id를 바꿈) 바꾼 후 확인
    1,홍길동,78,부산,남성
    3,홍시우,48,대구,남성
    2,최하윤,48,대구,여성
    4,홍민준,20,대전,남성
    5,홍지유,24,광주,여성
    6,김하준,27,광주,남성
    7,김옥연,71,광주,여성
    8,최시우,44,대전,남성
    9,박하은,42,대전,여성
    10,최민준,18,대전,남성
    
    --확인 결과 이번에는 홍시우가 아닌 최하윤이 들어가게 됨.id값이 더 큰 것이 들어가는 것으로 보임
    sqlite> select age,name from family order by age desc limit 3;
    age,name
  78,"홍길동"
    71,"김옥연"
    48,"최하윤"
    ```
  
    