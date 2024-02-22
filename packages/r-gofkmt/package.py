# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGofkmt(RPackage):
	"""Khmaladze Martingale Transformation Goodness-of-Fit Test

	Consider a goodness-of-fit (GOF) problem of testing whether a random sample comes from one sample location-scale model where location and scale parameters are unknown. It is well known that Khmaladze martingale transformation method - which was proposed by Khmaladze (1981) <DOI:10.1137/1126027> - provides asymptotic distribution free test for the GOF problem. This package contains one function: KhmaladzeTrans(). In this version, KhmaladzeTrans() provides test statistic and critical value of GOF test for normal, Cauchy, and logistic distributions. This package used the main algorithm proposed by Kim (2020) <DOI:10.1007/s00180-020-00971-7> and tests for other distributions will be available at the later version.
	"""
	
	cran = "GofKmt" 

	version("2.2.0", md5="981941815c7f67c427cc83d91a74fbdd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
