# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStochblock(RPackage):
	"""Stochastic Blockmodeling of One-Mode and Linked Networks

	Stochastic blockmodeling of one-mode and linked networks as implemented in Škulj and Žiberna (2022) <doi:10.1016/j.socnet.2022.02.001>. The optimization is done via CEM (Classification Expectation Maximization) algorithm that can be initialized by random partitions or the results of k-means algorithm. The development of this package is financially supported by the Slovenian Research Agency (<https://www.arrs.si/>) within the research programs P5-0168 and the research projects J7-8279 (Blockmodeling multilevel and temporal networks) and J5-2557 (Comparison and evaluation of different approaches to blockmodeling dynamic networks by simulations with application to Slovenian co-authorship networks).
	"""
	
	cran = "StochBlock" 

	version("0.1.2", md5="4e23bd5f0a30c9601dd9573edbcfdeaf")

	depends_on("r-blockmodeling", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
