===========
Jeiji
===========

Jeiji is a middleware that helps you to manage any kind of cloud. You can use the ``jeiji`` command (see
below), but it's also possible to use it in a Python file::

	#!/usr/bin/env python

    	from jeiji import cloud
    	from jeiji import jeiji

    	c = new cloud.Cloud
    	c.describe("Windows Azure", "http://myapp.azure.com", 1010, "username", "sha256password")
    	j = new jeiji.Jeiji(c)
    	j.analyze()

Using jeiji
=========

You can analyze a cloud using the command line as well::

	$ jeiji init
	$ jeiji create "Windows Azure" http://myapp.azure.com 1010 username sha256password
	$ jeiji analyze
