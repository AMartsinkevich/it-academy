-- Find all Managers.

create function get_manager_names()
returns table(manager_name text) as $$
begin
	return query
		select name
		from employees
		where position like '%Manager%';
end;
$$ language plpgsql;


select get_manager_names();
