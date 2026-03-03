# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLibstable4u(RPackage):
	"""Stable Distribution Functions...For You

	Tools for fast and accurate evaluation of skew stable distributions 
  (CDF, PDF and quantile functions), random number generation, and parameter 
  estimation.  This is 'libstableR' as per Royuela del Val, Simmross-Wattenberg, 
  and Alberola López (2017) <doi:10.18637/jss.v078.i01> under a new maintainer.  
	"""
	
	cran = "libstable4u" 

	version("1.0.3", md5="37cfe3e8310045b50dfc35469aab9846")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppgsl", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
