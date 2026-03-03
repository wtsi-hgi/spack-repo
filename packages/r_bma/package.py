# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBma(RPackage):
	"""Bayesian Model Averaging

	Package for Bayesian model averaging and variable selection for linear models,
        generalized linear models and survival models (cox
        regression).
	"""
	
	homepage = "http://stats.research.att.com/volinsky/bma.html"
	cran = "BMA" 

	version("3.18.17", md5="b2b0e7b205cb85a9a0905278327020d3")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-leaps", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-inline", type=("build", "run"))
	depends_on("r-rrcov", type=("build", "run"))
