# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSbde(RPackage):
	"""Semiparametric Bayesian Density Estimation

	Offers Bayesian semiparametric density estimation 
             and tail-index estimation for heavy tailed data, by
             using a parametric, tail-respecting transformation
             of the data to the unit interval and then modeling
             the transformed data with a purely nonparametric
             logistic Gaussian process density prior. Based on 
             Tokdar et al. (2022) <doi:10.1080/01621459.2022.2104727>.
	"""
	
	cran = "sbde" 

	version("1.0-1", md5="d0ab5c0ac509600d976136406ce3a3e2")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-extremefit", type=("build", "run"))
