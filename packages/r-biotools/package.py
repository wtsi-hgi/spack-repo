# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiotools(RPackage):
	"""Tools for Biometry and Applied Statistics in Agricultural
Science

	Tools designed to perform and evaluate cluster analysis (including Tocher's algorithm), 
	discriminant analysis and path analysis (standard and under collinearity), as well as some 
	useful miscellaneous tools for dealing with sample size and optimum plot size calculations. 
	A test for seed sample heterogeneity is now available. Mantel's permutation test can be found in this package. 
	A new approach for calculating its power is implemented. biotools also contains tests for genetic covariance components.
	Heuristic approaches for performing non-parametric spatial predictions of generic response variables and 
	spatial gene diversity are implemented.
	"""
	
	homepage = "https://arsilva87.github.io/biotools/"
	cran = "biotools" 

	version("4.2", md5="b9eb169fc6f6a10c1df5b41f8d158341")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
