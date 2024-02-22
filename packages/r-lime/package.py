# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLime(RPackage):
	"""Local Interpretable Model-Agnostic Explanations

	When building complex models, it is often difficult to explain why
    the model should be trusted. While global measures such as accuracy are
    useful, they cannot be used for explaining why a model made a specific
    prediction. 'lime' (a port of the 'lime' 'Python' package) is a method for
    explaining the outcome of black box models by fitting a local model around
    the point in question an perturbations of this point. The approach is
    described in more detail in the article by Ribeiro et al. (2016) 
    <arXiv:1602.04938>.
	"""
	
	homepage = "https://lime.data-imaginist.com"
	cran = "lime" 

	version("0.5.3", md5="6aeb440c71ce4027fbf42c8840771226")

	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-gower", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
