# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBbotk(RPackage):
	"""Black-Box Optimization Toolkit

	Features highly configurable search spaces via the 'paradox'
    package and optimizes every user-defined objective function. The package
    includes several optimization algorithms e.g. Random Search, Iterated
    Racing, Bayesian Optimization (in 'mlr3mbo') and Hyperband (in
    'mlr3hyperband'). bbotk is the base package of 'mlr3tuning', 'mlr3fselect'
    and 'miesmuschel'.
	"""
	
	homepage = "https://bbotk.mlr-org.com"
	cran = "bbotk" 

	version("0.8.0", md5="5aa8ad5181b56a2048598f2311662077")

	depends_on("r-paradox@0.7:", type=("build", "run"))
	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-checkmate@2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-lgr", type=("build", "run"))
	depends_on("r-mlr3misc@0.11:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
