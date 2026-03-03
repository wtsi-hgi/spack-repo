# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrinroc(RPackage):
	"""Statistical Tests for Assessing Trinormal ROC Data

	Several statistical test functions as well as a function for exploratory data analysis to investigate classifiers allocating individuals to one of three disjoint and ordered classes. In a single classifier assessment the discriminatory power is compared to classification by chance. In a comparison of two classifiers the null hypothesis corresponds to equal discriminatory power of the two classifiers.
	"""
	
	homepage = "https://math.uzh.ch/pages/trinROC/"
	cran = "trinROC" 

	version("0.6", md5="5aba0cbe4697abb7cf76019f66b84630")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
