# wfp2-auth-ex2
Solution to the WFP2 Pentester II lab: Authentication Example 2


A simple solution to the Web For Pentester II Authorization Example 2 exercise. This isn't a very robust solution as it performs single get requests against the server until it finds the next iteration of the password. A more robust solution would likely execute requests on multiple threads concurrently in order to find the password.
