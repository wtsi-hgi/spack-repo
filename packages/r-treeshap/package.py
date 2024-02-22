# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreeshap(RPackage):
	"""Compute SHAP Values for Your Tree-Based Models Using the
'TreeSHAP' Algorithm

	An efficient implementation of the 'TreeSHAP' algorithm
    introduced by Lundberg et al., (2020) <doi:10.1038/s42256-019-0138-9>.
    It is capable of calculating SHAP (SHapley Additive exPlanations) values 
    for tree-based models in polynomial time.  Currently supported models include 
    'gbm', 'randomForest', 'ranger', 'xgboost', 'lightgbm'.
	"""
	
	homepage = "https://modeloriented.github.io/treeshap/"
	cran = "treeshap" 

	version("0.3.1", md5="58c98288c20117cbb946c61bd957dfcc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
