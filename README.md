# Log Analysis - (UDACITY)

A python program that generates a report from a news database (Udacity's Full Stack Nano Degree [Log Analysis Project](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004))

## Requirements

- [python version 3](https://www.python.org/downloads/release/python-374/)
- [vagrant](https://www.vagrantup.com/downloads.html)
- [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
- [Git](https://git-scm.com/downloads)
- [news database .sql file](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

## Setup

1. Download any of the Requirments you are missing.

2. Download [this](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip) Udacity folder with preconfigured vagrant settings.
   or `clone https://github.com/udacity/fullstack-nanodegree-vm`

3. Clone this repository `clone https://github.com/nicolash92/log-analysis--udacity-.git`.

4. Navigate to the Udacity Virtual Machine folder in **git bash** and cd into vagrant.

5. using **git bash** and launch the virtual machine with `vagrant up`, then `vagrant ssh` to connect to the preconfigured linux instance.

6. Unpack the database folder contents downloaded above over here.

7. run `psql -d news -f newsdata.sql`

8. to run the program, while in the vm, navigate to the repo that you cloned from this one, and follow instructions in Running The Project

## Running The Project

on mac and linux based systems:
`> python3 log.py`

## `log.py` Module Functions

##### 1. `query_news(query)`

takes a query string and executes it on the news database, returns results as a list of tuples.

###### exapmle usage:

```
print(query_news('SELECT * FROM authors'))
```

###### output:

```
[('Ursula La Multa', 'Ursula La Multa is an expert on bears, bear abundance, and bear accessories.', 1),
('Rudolf von Treppenwitz', 'Rudolf von Treppenwitz is a nonprofitable disorganizer specializing in procrastinatory operations.', 2),
 ('Anonymous Contributor', "Anonymous Contributor's parents had unusual taste in names.", 3), ('Markoff Chaney', 'Markoff Chaney is the product of random genetics.', 4)]

```

##### 2. `print_result(results, append)`

takes a list of tuples as `results` and prints out the first and second element of each tuple seperated by `--` and the `append` string at the end.

###### exapmle usage:

using the first 2 tuple from the result list our previouse query as input

```
print_result([('Ursula La Multa', 'Ursula La Multa is an expert on bears, bear abundance, and bear accessories.', 1),
('Rudolf von Treppenwitz', 'Rudolf von Treppenwitz is a nonprofitable disorganizer specializing in procrastinatory operations.', 2)], ' APPENDED TEXT ')
```

###### output:

```
Ursula La Multa -- Ursula La Multa is an expert on bears, bear abundance, and bear accessories. APPENDED TEXT
Rudolf von Treppenwitz -- Rudolf von Treppenwitz is a nonprofitable disorganizer specializing in procrastinatory operations. APPENDED TEXT
```
