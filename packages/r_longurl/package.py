# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLongurl(RPackage):
	"""Expand Short 'URLs'

	Tools are provided to expand vectors of short URLs into long 'URLs'. 
    No 'API' services are used, which may mean that this operates more slowly than 
    'API' services do (since they usually cache results of expansions that every 
    user of the service requests). You can setup your own caching layer with the 
    'memoise' package if you wish to have a speedup during single sessions or add 
    larger dependencies, such as 'Redis', to gain a longer-term performance boost 
    at the expense of added complexity.
	"""
	
	cran = "longurl" 

	version("0.3.3", md5="429cc2bf101bdbb287cdbf568127c400")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
