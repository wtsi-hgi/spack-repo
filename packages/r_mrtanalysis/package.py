# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrtanalysis(RPackage):
	"""Primary and Secondary Analyses for Micro-Randomized Trials

	
    Estimates marginal causal excursion effects and moderated causal excursion effects for micro-randomized trial (MRT). Applicable to MRT with binary treatment options and continuous or binary outcomes. The method for MRT with continuous outcomes is the weighted centered least squares (WCLS) by Boruvka et al. (2018) <doi:10.1080/01621459.2017.1305274>. The method for MRT with binary outcomes is the estimator for marginal excursion effect (EMEE) by Qian et al. (2021) <doi:10.1093/biomet/asaa070>.
	"""
	
	cran = "MRTAnalysis" 

	version("0.1.2", md5="6f236e8e50052fc80a7f951b6e6b9e7b")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-geepack", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
