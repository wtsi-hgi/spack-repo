# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScem(RPackage):
	"""Splitting-Coalescence-Estimation Method

	We introduce improved methods for statistically assessing birth seasonality and intra-annual variation. The first method we propose is a new idea that uses a nonparametric clustering procedure to group individuals with similar time series data and estimate birth seasonality based on the clusters. One can use the function SCEM() to implement this method. The second method estimates input parameters for use with a previously-developed parametric approach (Tornero et al., 2013). The relevant code for this approach is makeFits_OLS(), while makeFits_initial() is the code to implement the same method but with given initial conditions for two parameters. The latter can be used to show the disadvantage of the existing approach. One can use the function makeFits() to generate parametric birth seasonality estimates using either initialization. Detailed description can be found here: Chazin Hannah, Soudeep Deb, Joshua Falk, and Arun Srinivasan. (2019) "New Statistical Approaches to Intra-Individual Isotopic Analysis and Modeling Birth Seasonality in Studies of Herd Animals." <doi:10.1111/arcm.12432>.
	"""
	
	homepage = "https://github.com/kserkcho/SCEM"
	cran = "SCEM" 

	version("1.1.0", md5="6ba3d88e7a1c5fbbf3a0dc0ec53ce4eb")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
