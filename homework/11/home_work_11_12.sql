-- Find all employees with a salary of more than 70000.

create function get_whale_names()
returns table(whale_name text) as $$
begin
	return query
		select name
		from employees
		where salary > 70000;
end;
$$ language plpgsql;


select get_whale_names();
