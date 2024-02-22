# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCortest(RPackage):
	"""Robust Tests for Equal Correlation

	There are 6 novel robust tests for equal correlation. They are all based on logistic regressions. The score statistic U is proportion to difference of two correlations based on different types of correlation in  6 methods. The ST1() is based on Pearson correlation. ST2() improved ST1() by using median absolute deviation. ST3() utilized type M correlation and ST4() used Spearman correlation.  ST5() and ST6() used two different ways to combine ST3() and ST4().  We highly recommend ST5() according to the article titled ''New Statistical Methods for Constructing Robust Differential Correlation Networks to characterize the interactions among microRNAs'' published in Scientific Reports.  Please see the reference: Yu et al. (2019) <doi:10.1038/s41598-019-40167-8>. 
	"""
	
	cran = "corTest" 

	version("1.0.7", md5="f9b25bc93fba0b99ac874320889b06f0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-clustergeneration", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
