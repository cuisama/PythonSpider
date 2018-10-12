select 'url表(总条数)',count(1) from url
union all
select 'url表(state=0)',count(1) from url where state = 0
union all
select 'url表(state=1)',count(1) from url where state = 1
union all
select 'url表(state=2)',count(1) from url where state = 2
union all
select 'video表(总条数)',count(1) from video
union all
select 'javli(条数)',count(url) from url where url like '%javli%'
union ALL
select '目录条数',count(1) from url where url not in (select url from video)

--alter table video add column img VARCHAR(200)
alter table video add CONSTRAINT 'CONSTRAINT_URL'  UNIQUE(url)

select url from url
--update url set state=0
where url not like '%javli%'

select * from url where url in ('http://www.o23g.com/cn/?v=javlil3l5a')

select url from url where 
url not in (select url from video)
and url like '%javli%'





select url from url where url like '%javli%'

select count(1) from video where img is null
--select * from video where url = ''

--update video set img = null where img in (
select 
--select c,
img from (
select count(img) c,max(img) img from video group by img)
where c>1
)
--VACUUM

select * from video where url not in (select url from url)

update url set state = 0 where url in(
select url from url where url not in (select url from video) and url like '%javli%')

SELECT name FROM sqlite_master WHERE type='table' ORDER BY name

--查询url表中状态为1的url重复的数据
select * from (
select count(url) u from url where state = 1 group by url) where u>1
--查询url表中状态为0的url重复的数据
select * from (
select count(url) u from url where state = 0 group by url) where u>1
--查询url表中url重复的数据
select * from (
select count(url) c ,min(url) from url group by url) where c>1

select * from url where url in ('','')
--删除重复的数据中状态是0或2的数据
select *
--delete 
from url 
where url in (
	select u from (
	select count(url) c,max(url) u,min(state) state from url group by url) where c>1 and state = 0
) or url in(
	select u from (
	select count(url) c,max(url) u,max(state) state from url group by url) where c>1 and state = 2
)

--
--删除重复的数据中状态是1的数据（先把重复的0，2的数据删掉再把1里重复的删掉）
select *
--delete
from url 
where url in(
	select u from (
	select count(url) c,max(url) u from url where state = 1 group by url) where c>1
) and id not in (
	select id from (
	select count(url) c,max(url) u,min(id) id from url where state = 1 group by url) where c>1
)and state = 1




--查询video表中url重复的数据
select * from video where url in (
select u from (
select count(url) c,max(url) u from video group by url) where c>1
)
delete from video where id in(96824,98726)

--查询url表里的状态是1的，且在video表中数据 ，该数据量>=video表数据
select * from url where url in (select url from video) and state = 1
--查询video表中有的，url表中（状态为1）没有的数据，应该没有这样的数据
SELECT * from video where url not in (select url from url where state = 1)
--将video表中
--insert into url(url,state) 
SELECT url,1 from video where url not in (select url from url where state = 1)

--将在video表中，也在url表中（但state！=1）的数据的状态更新成1
SELECT * from url
--update url set state=1 
where 
url not in(select url from url where state=1) 
and url in (select url from video) 


