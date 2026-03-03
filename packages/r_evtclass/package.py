# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvtclass(RPackage):
	"""Extreme Value Theory for Open Set Classification - GPD and GEV
Classifiers

	Two classifiers for open set recognition and novelty detection based on extreme value theory. The first classifier is based on the generalized Pareto distribution (GPD) and the second classifier is based on the generalized extreme value (GEV) distribution. For details, see Vignotto, E., & Engelke, S. (2018) <arXiv:1808.09902>.
	"""
	
	cran = "evtclass" 

	version("1.0", md5="fe5cb8a678d2270c209c703dca18b9bb")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-evd", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
