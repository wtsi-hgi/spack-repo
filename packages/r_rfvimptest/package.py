# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfvimptest(RPackage):
	"""Sequential Permutation Testing of Random Forest Variable
Importance Measures

	Sequential permutation testing for statistical
  significance of predictors in random forests. The main function
  of the package is rfvimptest(), which allows to test for the
  statistical significance of predictors in random forests using different 
  (sequential) permutation test strategies. The advantage of
  sequential over conventional permutation tests is that they
  are computationally considerably less intensive, as the sequential
  procedure is stopped as soon as there is sufficient evidence
  for either the null or the alternative hypothesis.
	"""
	
	cran = "rfvimptest" 

	version("0.1.3", md5="bf6da3829cf9b393e649f2cd86a86012")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-party", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-permimp", type=("build", "run"))
