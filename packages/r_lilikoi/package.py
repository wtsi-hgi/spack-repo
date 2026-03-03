# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLilikoi(RPackage):
	"""Metabolomics Personalized Pathway Analysis Tool

	A comprehensive analysis tool for metabolomics data.  It consists a variety of functional modules, including several new modules: a pre-processing module for normalization and imputation, an exploratory data analysis module for dimension reduction and source of variation analysis, a classification module with the new deep-learning method and other machine-learning methods, a prognosis module with cox-PH and neural-network based Cox-nnet methods, and pathway analysis module to visualize the pathway and interpret metabolite-pathway relationships. References: H. Paul Benton <http://www.metabolomics-forum.com/index.php?topic=281.0> Jeff Xia <https://github.com/cangfengzhe/Metabo/blob/master/MetaboAnalyst/website/name_match.R> Travers Ching, Xun Zhu, Lana X. Garmire (2018) <doi:10.1371/journal.pcbi.1006076>.
	"""
	
	cran = "lilikoi" 

	version("2.1.1", md5="6295b20d9e414693d1919743cfab43a8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-h2o", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-infotheo", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-m3c", type=("build", "run"))
	depends_on("r-metrics", type=("build", "run"))
	depends_on("r-mlmetrics", type=("build", "run"))
	depends_on("r-princurve", type=("build", "run"))
	depends_on("r-pathview", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-rcy3", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-rweka", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-survminer", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
