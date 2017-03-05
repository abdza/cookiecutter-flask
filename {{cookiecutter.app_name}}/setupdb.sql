create database {{cookiecutter.app_name}}_db;
create role {{cookiecutter.app_name}} with password '{{cookiecutter.app_name}}123' login;
grant all on database {{cookiecutter.app_name}}_db to {{cookiecutter.app_name}};
