select 'url表(总条数)',count(1) from url
union all
select 'url表(state=0)',count(1) from url where state = 0
union all
select 'url表(state=1)',count(1) from url where state = 1
union all
select 'url表(state=2)',count(1) from url where state = 2
union all
select 'video表(总条数)',count(1) from video


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
select * from (
select count(url) u from video group by url) where u>1

--查询url表里的状态是1的，且在video表中数据 ，该数据量>=video表数据
select * from url where url in (select url from video) and state = 1
--查询video表中有的，url表中（状态为1）没有的数据，应该没有这样的数据
SELECT * from video where url not in (select url from url where state = 1)
--将video表中
--insert into url(url,state) 
SELECT url,1 from video where url not in (select url from url where state = 1)


select url where
