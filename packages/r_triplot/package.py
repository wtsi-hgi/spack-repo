# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTriplot(RPackage):
	"""Explaining Correlated Features in Machine Learning Models

	Tools for exploring effects of correlated features in predictive 
    models. The predict_triplot() function delivers instance-level explanations 
    that calculate the importance of the groups of explanatory variables. The 
    model_triplot() function delivers data-level explanations. The generic plot 
    function visualises in a concise way importance of hierarchical groups of 
    predictors. All of the the tools are model agnostic, therefore works for any
    predictive machine learning models. Find more details in Biecek (2018) 
    <arXiv:1806.08915>.
	"""
	
	homepage = "https://github.com/ModelOriented/triplot"
	cran = "triplot" 

	version("1.3.0", md5="04952070951632e42f9e78e4fde8a0a9")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dalex@1.3:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-ggdendro", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
