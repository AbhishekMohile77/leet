# Write your MySQL query statement below
with mail_cnt as (
    select count(email) as cnt, email as Email
    from Person
    group by email
)
select Email from mail_cnt
where cnt>1;