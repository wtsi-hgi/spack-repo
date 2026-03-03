# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQf(RPackage):
	"""Density, Cumulative and Quantile Functions of Quadratic Forms

	The computation of quadratic form (QF) distributions is often not trivial and it requires numerical routines. The package contains functions aimed at evaluating the exact distribution of quadratic forms (QFs) and ratios of QFs. In particular, we propose to evaluate density, quantile and distribution functions of positive definite QFs and ratio of independent positive QFs by means of an algorithm based on the numerical inversion of Mellin transforms.  
	"""
	
	cran = "QF" 

	version("0.0.6", md5="17a0ffcdfaf5eadb006f0221d42f6b34")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppgsl", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
