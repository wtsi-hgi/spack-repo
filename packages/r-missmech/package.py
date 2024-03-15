# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMissmech(RPackage):
	"""Testing Homoscedasticity, Multivariate Normality, and Missing
Completely at Random

	To test whether the missing data mechanism, in a set of incompletely observed data, is one of missing completely at random (MCAR). 
    For detailed description see Jamshidian, M. Jalal, S., and Jansen, C. (2014). "MissMech: An R Package for Testing Homoscedasticity, Multivariate Normality, and Missing Completely at Random (MCAR)", Journal of Statistical Software, 56(6), 1-31. <https://www.jstatsoft.org/v56/i06/> <doi:10.18637/jss.v056.i06>.
	"""
	
	homepage = "https://github.com/indenkun/MissMech"
	cran = "MissMech" 

	version("1.0.4", md5="5148e8fa34997468c288c4d3dc05d3d4")

	depends_on("r@2.10:", type=("build", "run"))
