# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyposterior(RPackage):
	"""Bayesian Analysis to Compare Models using Resampling Statistics

	Bayesian analysis used here to answer the question: "when
    looking at resampling results, are the differences between models
    'real'?" To answer this, a model can be created were the performance
    statistic is the resampling statistics (e.g. accuracy or RMSE). These
    values are explained by the model types. In doing this, we can get
    parameter estimates for each model's affect on performance and make
    statistical (and practical) comparisons between models. The methods
    included here are similar to Benavoli et al (2017)
    <https://jmlr.org/papers/v18/16-305.html>.
	"""
	
	homepage = "https://tidyposterior.tidymodels.org"
	cran = "tidyposterior" 

	version("1.0.1", md5="6ca2614951f898190e3d0c7ffad1ced6")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rsample@0.0.2:", type=("build", "run"))
	depends_on("r-rstanarm@2.21.1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr@0.7.1:", type=("build", "run"))
	depends_on("r-tune@0.2:", type=("build", "run"))
	depends_on("r-vctrs@0.3:", type=("build", "run"))
	depends_on("r-workflowsets", type=("build", "run"))
