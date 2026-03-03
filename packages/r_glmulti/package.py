# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmulti(RPackage):
	"""Model Selection and Multimodel Inference Made Easy

	Automated model selection and model-averaging. Provides a
        wrapper for glm and other functions, automatically generating
        all possible models (under constraints set by the user) with
        the specified response and explanatory variables, and finding
        the best models in terms of some Information Criterion (AIC,
        AICc or BIC). Can handle very large numbers of candidate
        models. Features a Genetic Algorithm to find the best models
        when an exhaustive screening of the candidates is not feasible.
	"""
	
	cran = "glmulti" 

	version("1.0.8", md5="3c9dac72c95d255cb61a93a8b9361528")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-rjava@0.5.0:", type=("build", "run"))
	depends_on("r-leaps", type=("build", "run"))
	depends_on("openjdk@5:", type=("build", "link", "run"))
