-- Write your query below
with cte as (
    select t1.name, t2.customer_id, t2.id
    from customers as t1
    left join orders as t2
    on t1.id = t2.customer_id 
)

select name
from cte 
where id is NULL 

