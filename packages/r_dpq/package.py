# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDpq(RPackage):
	"""Density, Probability, Quantile ('DPQ') Computations

	Computations for approximations and alternatives for the 'DPQ'
  (Density (pdf), Probability (cdf) and Quantile) functions for probability
  distributions in R.
  Primary focus is on (central and non-central) beta, gamma and related
  distributions such as the chi-squared, F, and t.
  --
  For several distribution functions, provide functions implementing formulas from
  Johnson, Kotz, and Kemp (1992) <doi:10.1002/bimj.4710360207>  and
  Johnson, Kotz, and Balakrishnan (1995) for discrete or continuous
  distributions respectively.
  This is for the use of researchers in these numerical approximation
  implementations, notably for my own use in order to improve standard
  R pbeta(), qgamma(), ..., etc: {'"dpq"'-functions}.
	"""
	
	homepage = "https://specfun.r-forge.r-project.org/"
	cran = "DPQ" 

	version("0.5-8", md5="653e0afc54603c1d168ad90261e358c5")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-sfsmisc@1.1.14:", type=("build", "run"))
