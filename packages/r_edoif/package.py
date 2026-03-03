# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdoif(RPackage):
	"""Empirical Distribution Ordering Inference Framework (EDOIF)

	A non-parametric framework based on  estimation statistics principle. Its main purpose is to  infer orders of empirical distributions from different categories based on a probability of finding a value in one distribution that is greater than an expectation of another distribution. Given a set of ordered-pair of real-category values the framework is capable of 1) inferring orders of  domination  of  categories  and  representing  orders  in  the form of a graph; 2) estimating  magnitude  of  difference  between  a  pair  of categories in forms of mean-difference confidence intervals; and 3) visualizing  domination  orders  and  magnitudes  of  difference of categories. The publication of this package is at Chainarong Amornbunchornvej, Navaporn Surasvadi, Anon Plangprasopchok, and Suttipong Thajchayapong (2020) <doi:10.1016/j.heliyon.2020.e05435>.
	"""
	
	homepage = "https://github.com/DarkEyes/EDOIF"
	cran = "EDOIF" 

	version("0.1.3", md5="fb92ddea3bf0362b57967ff788aab11a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-distr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ellipsis", type=("build", "run"))
	depends_on("r-simpleboot", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
