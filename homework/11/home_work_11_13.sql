-- Find all employees from IT Department.

create function get_department_names(department_name text)
returns table(employee_name text) as $$
begin
	return query
		select name
		from employees
		where department = department_name;
end;
$$ language plpgsql;


select get_department_names('IT');
