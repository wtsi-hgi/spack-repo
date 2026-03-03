# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdnp(RPackage):
	"""Robust Test for Complete Independence in High-Dimensions

	Test Statistics for Independence in High-Dimensional Datasets. This package consists of two functions to perform the complete independence test based on test statistics proposed by Bulut (unpublished yet) and suggested by Najarzadeh (2021) <doi: 10.1080/03610926.2019.1702699>. The Bulut's statistic is not sensitive to outliers in high-dimensional data, unlike one of Najarzadeh (2021) <doi: 10.1080/03610926.2019.1702699>. So, the Bulut's statistic can be performed robustly by using RDnp function.  
	"""
	
	cran = "RDnp" 

	version("1.3", md5="93e56e2b561fbb3607cd04a0378dec23")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cellwise", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
