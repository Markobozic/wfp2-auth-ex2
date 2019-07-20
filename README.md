# wfp2-auth-ex2
Solution to the WFP2 Pentester II lab: Authentication Example 2


A simple solution to the Web For Pentester II Authorization Example 2 exercise. This isn't a very robust solution as it performs single get requests against the server until it finds the next iteration of the password. A more robust solution would likely execute requests on multiple threads concurrently in order to find the password.

To run the program, make sure you have WFP2 running locally on a virtual box, then run the program with python3 from the command line as such: `python3 program2_bozic.py your-hostname:port`
