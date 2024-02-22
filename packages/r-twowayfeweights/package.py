# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTwowayfeweights(RPackage):
	"""Estimation of the Weights Attached to the Two-Way Fixed Effects
Regressions

	
    Estimates the weights and measure of robustness to treatment effect heterogeneity attached to two-way fixed effects regressions.
    Clément de Chaisemartin, Xavier D'Haultfœuille (2020) <DOI: 10.1257/aer.20181169>.
	"""
	
	cran = "TwoWayFEWeights" 

	version("2.0.0", md5="cf45a6f8becb4306533be156b2c77a92")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-fixest", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
