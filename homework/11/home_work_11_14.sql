-- Find average salary of department.

create function get_department_average_salary(department_name text)
returns decimal(10, 2) as $$
declare
	average_salary decimal(10, 2);
begin
	select avg(salary) as average_salary
	into average_salary
	from employees
	where department = department_name;
	return average_salary;
end;
$$ language plpgsql;


select get_department_average_salary('IT');
