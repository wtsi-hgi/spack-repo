# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCre(RPackage):
	"""Interpretable Discovery and Inference of Heterogeneous Treatment
Effects

	Provides a new method for interpretable heterogeneous 
    treatment effects characterization in terms of decision rules 
    via an extensive exploration of heterogeneity patterns by an 
    ensemble-of-trees approach, enforcing high stability in the 
    discovery. It relies on a two-stage pseudo-outcome regression, and 
    it is supported by theoretical convergence guarantees. Bargagli-Stoffi, 
    F. J., Cadei, R., Lee, K., & Dominici, F. (2023) Causal rule ensemble: 
    Interpretable Discovery and Inference of Heterogeneous Treatment Effects.  
    arXiv preprint <arXiv:2009.09036>.
	"""
	
	homepage = "https://github.com/NSAPH-Software/CRE"
	cran = "CRE" 

	version("0.2.5", md5="e61f82135117397b62fd7fc8739c927c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-logger", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
	depends_on("r-rrf", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-bartcause", type=("build", "run"))
	depends_on("r-stabs", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-superlearner", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-intrees", type=("build", "run"))
