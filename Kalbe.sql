-- Mengakses tabel customer 
select * 
from customer c

-- Mengakses tabel store
select * 
from store s

-- Mengakses tabel product
select * 
from product p

-- Mengakses tabel transaction
select * 
from transaction t

-- Berapa rata-rata umur customer jika dilihat dari marital statusnya?
select "Marital Status", AVG(age) as average_age
from customer
group by "Marital Status";

-- Berapa rata-rata umur customer jika dilihat dari gender nya? 
select gender, AVG(age) as average_age
from customer
group by gender;

-- Tentukan nama store dengan total quantity terbanyak! 
select s.storename, SUM(t.qty) as total_qty
from store s
join "transaction" t on s.storeid = t.storeid
group by s.storename
order by total_qty desc
limit 3;

-- Tentukan nama produk terlaris dengan total amount terbanyak!
select p."Product Name", SUM(t.totalamount) as total_amount
from product p 
join "transaction" t on p.productid = t.productid
group by p."Product Name" 
order by total_amount desc
limit 3;
