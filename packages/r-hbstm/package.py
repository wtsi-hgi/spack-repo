# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHbstm(RPackage):
	"""Hierarchical Bayesian Space-Time Models for Gaussian Space-Time
Data

	Fits Hierarchical Bayesian space-Time models for Gaussian data. Furthermore, its functions have been implemented for analysing the fitting qualities of those models.
	"""
	
	cran = "HBSTM" 

	version("1.0.2", md5="5c2bfb933d31733e53ce2ba0698c1baf")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-fbasics", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
