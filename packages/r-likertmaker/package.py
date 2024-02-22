# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLikertmaker(RPackage):
	"""Synthesise and Correlate Rating-Scale Data

	Synthesise and correlate rating-scale data with 
  predefined first & second moments and, optionally, predefined 
  correlation matrix. 
  The function, `lexact()`, uses the 'DEoptim' 
  <https://CRAN.R-project.org/package=DEoptim> package, described in 
  Mullen, Ardia, Gil, Windover, & Cline (2011) <doi:10.18637/jss.v040.i06>,
  to synthesise a vector of discrete values with predefined mean and 
  standard deviation exact to two decimal places, if feasible. 
  The function, `lfast()`, draws a random sample from a _Beta_ distribution 
  which is rescaled to give a vector with approximate first and second moments. 
  It is much faster than `lexact()` but not as precise. 
  The function, `lcor()`, systematically swaps values within each column of a 
  data-frame so that they are correlated to fit a predefined correlation matrix.
	"""
	
	homepage = "https://github.com/WinzarH/LikertMakeR"
	cran = "LikertMakeR" 

	version("0.1.5", md5="43d5cbce23011073f490aedee6cb0917")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-deoptim@2.2.0:", type=("build", "run"))
