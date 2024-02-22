# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsvddpd(RPackage):
	"""Robust Singular Value Decomposition using Density Power
Divergence

	Computing singular value decomposition with robustness is a challenging task. 
    This package provides an implementation of computing robust SVD using density power 
    divergence (<arXiv:2109.10680>). It combines the idea of robustness and efficiency in estimation
    based on a tuning parameter. It also provides utility functions to simulate various
    scenarios to compare performances of different algorithms.
	"""
	
	homepage = "https://github.com/subroy13/rsvddpd"
	cran = "rsvddpd" 

	version("1.0.0", md5="6f2964b9a61b0ef08ef390223f45d121")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
