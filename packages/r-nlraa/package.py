# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlraa(RPackage):
	"""Nonlinear Regression for Agricultural Applications

	Additional nonlinear regression functions using self-start (SS) algorithms. One of the functions is the Beta growth function proposed by Yin et al. (2003) <doi:10.1093/aob/mcg029>. There are several other functions with breakpoints (e.g. linear-plateau, plateau-linear, exponential-plateau, plateau-exponential, quadratic-plateau, plateau-quadratic and bilinear), a non-rectangular hyperbola and a bell-shaped curve. Twenty eight (28) new self-start (SS) functions in total. This package also supports the publication 'Nonlinear regression Models and applications in agricultural research' by Archontoulis and Miguez (2015) <doi:10.2134/agronj2012.0506>, a book chapter with similar material <doi:10.2134/appliedstatistics.2016.0003.c15> and a publication by Oddi et. al. (2019) in Ecology and Evolution <doi:10.1002/ece3.5543>. The function 'nlsLMList' uses 'nlsLM' for fitting, but it is otherwise almost identical to 'nlme::nlsList'.In addition, this release of the package provides functions for conducting simulations for 'nlme' and 'gnls' objects as well as bootstrapping. These functions are intended to work with the modeling framework of the 'nlme' package. It also provides four vignettes with extended examples.
	"""
	
	cran = "nlraa" 

	version("1.9.7", md5="d47dedeba9c70a83770626bc70090f46")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
