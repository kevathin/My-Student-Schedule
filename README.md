# My-Student-Schedule
a application that connects 4 different student schedule/program websites/applications. This includes my schedule builder, registration page, student program requirements, and gned courses., 

Running a live server within the network:

I was able to run the application so that anyone within the same network (ex: MRU secure) were able to access my server using a standard http request. to run the application regularly i have to use the following format: 

flask --app "local path" run

and to run a server i also include: --host=0.0.0.0 at the end of the above.

to prevent injection attacks, i have to wrap the argument provided with escape(). it is so that it causes the inputed value to be rendered as text instead of a script