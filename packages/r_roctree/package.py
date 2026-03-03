# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoctree(RPackage):
	"""Receiver Operating Characteristic (ROC)-Guided Classification
and Survival Tree

	Receiver Operating Characteristic (ROC)-guided survival trees and ensemble algorithms are implemented, providing a unified framework for tree-structured analysis with censored survival outcomes. A time-invariant partition scheme on the survivor population was considered to incorporate time-dependent covariates. Motivated by ideas of randomized tests, generalized time-dependent ROC curves were used to evaluate the performance of survival trees and establish the optimality of the target hazard/survival function. The optimality of the target hazard function motivates us to use a weighted average of the time-dependent area under the curve (AUC) on a set of time points to evaluate the prediction performance of survival trees and to guide splitting and pruning. A detailed description of the implemented methods can be found in Sun et al. (2019) <arXiv:1809.05627>.
	"""
	
	homepage = "http://github.com/stc04003/rocTree"
	cran = "rocTree" 

	version("1.1.1", md5="1b08a4103a2a26bf20cb732553330652")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-diagrammer@1:", type=("build", "run"))
	depends_on("r-data-tree@0.7.5:", type=("build", "run"))
	depends_on("r-survival@2.38:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-flexsurv", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
