# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgof(RPackage):
	"""1d Goodness of Fit Tests

	Routines that allow the user to run a large number of goodness-of-fit tests.  
     It allows for data to be continuous or discrete. It includes routines to estimate
     the power of the tests and display them as a power graph.      
	"""
	
	cran = "Rgof" 

	version("1.2.2", md5="2fa9670cae78c157a0c0eaff6a140a2a")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
