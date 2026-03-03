# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDnetfinder(RPackage):
	"""Estimating Differential Networks under Semiparametric Gaussian
Graphical Models

	Provides a modified hierarchical test (Liu (2017) <doi:10.1214/17-AOS1539>) for detecting the structural difference between two Semiparametric Gaussian graphical models. The multiple testing procedure asymptotically controls the false discovery rate (FDR) at a user-specified level. To construct the test statistic, a truncated estimator is used to approximate the transformation functions and two R functions including lassoGGM() and lassoNPN() are provided to compute the lasso estimates of the regression coefficients. 
	"""
	
	cran = "DNetFinder" 

	version("1.1", md5="85e699257ac904feb4d432a475bfa0c6")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-flare", type=("build", "run"))
