# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExpsbm(RPackage):
	"""An Exponential Stochastic Block Model for Interaction Lengths

	Given a continuous-time dynamic network, this package allows one to fit a stochastic blockmodel where nodes belonging to the same group create interactions and non-interactions of similar lengths. This package implements the methodology described by R. Rastelli and M. Fop (2019) <arXiv:1901.09828>.
	"""
	
	cran = "expSBM" 

	version("1.3.5", md5="1ffbad26027a96d6a3c6115ee4588a04")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-blockmodels", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
