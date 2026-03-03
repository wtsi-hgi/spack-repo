# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTmvtnsim(RPackage):
	"""Truncated Multivariate Normal and t Distribution Simulation

	Simulation of random vectors from truncated multivariate normal 
  and t distributions based on the algorithms proposed by Yifang Li and Sujit K. Ghosh (2015) <doi:10.1080/15598608.2014.996690>.
	"""
	
	cran = "tmvtnsim" 

	version("0.1.3", md5="fc3a8f68fd3c87d79c2294c354bb806a")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
