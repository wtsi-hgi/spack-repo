# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSbrl(RPackage):
	"""Scalable Bayesian Rule Lists Model

	An efficient implementation of Scalable Bayesian Rule Lists Algorithm, a competitor algorithm for decision tree algorithms; see Hongyu Yang, Cynthia Rudin, Margo Seltzer (2017) <https://proceedings.mlr.press/v70/yang17h.html>. It builds from pre-mined association rules and have a logical structure identical to a decision list or one-sided decision tree. Fully optimized over rule lists, this algorithm strikes practical balance between accuracy, interpretability, and computational speed.
	"""
	
	cran = "sbrl" 

	version("1.3", md5="f454d4bc46453364ed7b083d1016c827")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-arules", type=("build", "run"))
	depends_on("gmp@4.2:", type=("build", "link", "run"))
	depends_on("gsl", type=("build", "link", "run"))
