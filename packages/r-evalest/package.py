# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvalest(RPackage):
	"""Dynamic Systems Estimation - Extensions

	Provides functions for evaluating (time series) model
	estimation methods. These facilitate Monte Carlo experiments of repeated
	simulations and estimations. Also provides methods for
	looking at the distribution of the results from these experiments,
	including model roots (which are an equivalence class invariant).
	"""
	
	homepage = "http://tsanalysis.r-forge.r-project.org/"
	cran = "EvalEst" 

	version("2024.2-1", md5="7af8c812f4f25d6639dfa4438597b446")

	depends_on("r@2.5:", type=("build", "run"))
	depends_on("r-tfplot", type=("build", "run"))
	depends_on("r-dse@2007.10.1:", type=("build", "run"))
	depends_on("r-setrng", type=("build", "run"))
	depends_on("r-tframe@2007.5.3:", type=("build", "run"))
