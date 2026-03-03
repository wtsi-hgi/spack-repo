# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVsolassobag(RPackage):
	"""Variable Selection Oriented LASSO Bagging Algorithm

	A wrapped LASSO approach by integrating an ensemble learning strategy to help select efficient, stable, and high confidential variables from omics-based data. Using a bagging strategy in combination of a parametric method or inflection point search method for cut-off threshold determination. This package can integrate and vote variables generated from multiple LASSO models to determine the optimal candidates. Luo H, Zhao Q, et al (2020) <doi:10.1126/scitranslmed.aax7533> for more details.
	"""
	
	cran = "VSOLassoBag" 

	version("0.99.1", md5="fe87f2969fb523a7d7131e51a346554b")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-pot", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
