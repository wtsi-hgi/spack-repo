# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKernelheaping(RPackage):
	"""Kernel Density Estimation for Heaped and Rounded Data

	In self-reported or anonymised data the user often encounters
    heaped data, i.e. data which are rounded (to a possibly different degree
    of coarseness). While this is mostly a minor problem in parametric density
    estimation the bias can be very large for non-parametric methods such as kernel
    density estimation. This package implements a partly Bayesian algorithm treating
    the true unknown values as additional parameters and estimates the rounding
    parameters to give a corrected kernel density estimate. It supports various
    standard bandwidth selection methods. Varying rounding probabilities (depending
    on the true value) and asymmetric rounding is estimable as well: Gross, M. and Rendtel, U. (2016) (<doi:10.1093/jssam/smw011>).
    Additionally, bivariate non-parametric density estimation for rounded data, Gross, M. et al. (2016) (<doi:10.1111/rssa.12179>),
    as well as data aggregated on areas is supported.
	"""
	
	cran = "Kernelheaping" 

	version("2.3.0", md5="490cd721ebbe8743f0536a45c8d667d3")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-sparr", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fastmatch", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-gb2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
