# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvmorph(RPackage):
	"""Multivariate Comparative Tools for Fitting Evolutionary Models
to Morphometric Data

	Fits multivariate (Brownian Motion, Early Burst, ACDC, Ornstein-Uhlenbeck and Shifts) models of continuous traits evolution on trees and time series. 'mvMORPH' also proposes high-dimensional multivariate comparative tools (linear models using Generalized Least Squares and multivariate tests) based on penalized likelihood.  See
    Clavel et al. (2015) <DOI:10.1111/2041-210X.12420>, Clavel et al. (2019) <DOI:10.1093/sysbio/syy045>, and Clavel & Morlon (2020) <DOI:10.1093/sysbio/syaa010>.
	"""
	
	homepage = "https://github.com/JClavel/mvMORPH"
	cran = "mvMORPH" 

	version("1.1.9", md5="5d2a2dcb4609f6d6b6911e46546f9d76")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-phytools", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-subplex", type=("build", "run"))
	depends_on("r-spam", type=("build", "run"))
	depends_on("r-glassofast", type=("build", "run"))
	depends_on("r-pbmcapply", type=("build", "run"))
