# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDittodb(RPackage):
	"""A Test Environment for Database Requests

	Testing and documenting code that communicates with remote
  databases can be painful. Although the interaction with R is usually relatively 
  simple (e.g. data(frames) passed to and from a database), because they rely on 
  a separate service and the data there, testing them can be difficult to set up,
  unsustainable in a continuous integration environment, or impossible without 
  replicating an entire production cluster. This package addresses that by 
  allowing you to make recordings from your database interactions and then play 
  them back while testing (or in other contexts) all without needing to spin up 
  or have access to the database your code would typically connect to.
	"""
	
	homepage = "https://dittodb.jonkeane.com/"
	cran = "dittodb" 

	version("0.1.7", md5="5793eafcd968031194fb9da567c75b85")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
