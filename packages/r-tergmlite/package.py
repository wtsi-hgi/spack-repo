# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTergmlite(RPackage):
	"""Fast Simulation of Simple Temporal Exponential Random Graph
Models

	Provides functions for the computationally efficient simulation of 
    dynamic networks estimated with the statistical framework of temporal 
    exponential random graph models, implemented in the 'tergm' package.
	"""
	
	cran = "tergmLite" 

	version("2.6.1", md5="07d8cae5cdf2143a905d7a109685f61f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ergm", type=("build", "run"))
	depends_on("r-tergm@4:", type=("build", "run"))
	depends_on("r-statnet-common@4.4:", type=("build", "run"))
	depends_on("r-network@1.17:", type=("build", "run"))
	depends_on("r-networkdynamic@0.11:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
