# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultinomialci(RPackage):
	"""Simultaneous Confidence Intervals for Multinomial Proportions
According to the Method by Sison and Glaz

	An implementation of a method for building simultaneous confidence intervals for the probabilities of a multinomial distribution given a set of observations, proposed by Sison and Glaz in their paper:
        Sison, C.P and J. Glaz. Simultaneous confidence intervals and sample size determination for multinomial proportions. Journal of the American Statistical Association, 90:366-369 (1995). 
        The method is an R translation of the SAS code implemented by May and Johnson in their paper:
        May, W.L. and W.D. Johnson. Constructing two-sided simultaneous confidence intervals for multinomial proportions for small counts in a large number of cells. Journal of Statistical Software 5(6) (2000). 
        Paper and code available at <DOI:10.18637/jss.v005.i06>.
	"""
	
	homepage = "https://ccia.ugr.es/~pjvi/"
	cran = "MultinomialCI" 

	version("1.2", md5="31748907bac0c36de723d8608dbc525e")

	depends_on("r@2.15:", type=("build", "run"))
