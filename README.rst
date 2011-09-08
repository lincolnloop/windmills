Stop Tilting at Windmills
=========================

Abstract
********

Performance optimization has always been a hot topic among the Django
community, and as applications become more mature and larger companies adopt
Django for high-traffic projects this issue will heat up even more. This talk
will not focus on resolving performance/scalability issues but rather on
discovering them. It will try to answer the following questions:

* How do you know where the worst problems are?
* When did the problem start, and what parts of your application are affected?
* How do you tell the difference between the giant performance monsters and the windmills that aren’t really big problems at all?

This talk will not spell out a quick and easy 5-step method to alleviating all
of your performance woes. It will, however, show you ways to measure your
site’s performance over time and spot the real trouble areas as they occur.
It’s vital to know both your application and your user well in order to create
an effective test plan. We will discuss the importance of reliable performance
measurement and realistic performance tests, and walk you through the tools we
use to identify and track problems.

* Django Debug Toolbar - get internal information about what your application is doing
* Django Debug Logging - log Debug Toolbar statistics to the database and review details and aggregated summaries.
* Creating a cron job to run automated performance tests at regular intervals
* Jmeter for external tool to create load tests with high concurrency

To close up, we’ll mention some of our favorite resources on handling the
performance problems that you encounter during your testing. We’ll also provide
links to other tools that you can use as part of your testing efforts. With
this information at your disposal you can charge boldly through the meadow on
your faithful Rocinante, attacking the real performance problems and leaving
the windmills behind.
