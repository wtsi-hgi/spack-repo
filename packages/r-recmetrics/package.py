# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRecmetrics(RPackage):
	"""Psychometric Evaluation Using Relative Excess Correlations

	Modern results of psychometric theory are implemented to provide users with a way of evaluating the internal structure of a set of items guided by theory. These methods are discussed in detail in VanderWeele and Padgett (2024) <doi:10.31234/osf.io/rnbk5>. The relative excess correlation matrices will, generally, have numerous negative entries even if all of the raw correlations between each pair of indicators are positive. The positive deviations of the relative excess correlation matrix entries help identify clusters of indicators that are more strongly related to one another, providing insights somewhat analogous to factor analysis, but without the need for rotations or decisions concerning the number of factors. A goal similar to exploratory/confirmatory factor analysis, but 'recmetrics' uses novel methods that do not rely on assumptions of latent variables or latent variable structures. 
	"""
	
	homepage = "https://noah-padgett.github.io/recmetrics/"
	cran = "recmetrics" 

	version("0.1.0", md5="86a3f0f926bd5f2ddbb4fac79126f29f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
