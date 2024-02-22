# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpfsr(RPackage):
	"""Feature Selection and Ranking via Simultaneous Perturbation
Stochastic Approximation

	An implementation of feature selection, weighting and ranking via simultaneous perturbation
    stochastic approximation (SPSA). The SPSA-FSR algorithm searches for a locally optimal set of
    features that yield the best predictive performance using some error measures such as mean 
    squared error (for regression problems) and accuracy rate (for classification problems).
	"""
	
	homepage = "https://www.featureranking.com/"
	cran = "spFSR" 

	version("2.0.4", md5="b72fd251ad93a09daad01eba278d2f06")

	depends_on("r-mlr3@0.14:", type=("build", "run"))
	depends_on("r-future@1.28:", type=("build", "run"))
	depends_on("r-tictoc@1:", type=("build", "run"))
	depends_on("r-mlr3pipelines@0.4.2:", type=("build", "run"))
	depends_on("r-mlr3learners@0.5.4:", type=("build", "run"))
	depends_on("r-ranger@0.14.1:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-lgr@0.4.4:", type=("build", "run"))
