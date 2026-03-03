# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPromor(RPackage):
	"""Proteomics Data Analysis and Modeling Tools

	A comprehensive, user-friendly package for label-free proteomics data analysis and machine learning-based modeling. Data generated from 'MaxQuant' can be easily used to conduct differential expression analysis, build predictive models with top protein candidates, and assess model performance. promor includes a suite of tools for quality control, visualization, missing data imputation (Lazar et. al. (2016) <doi:10.1021/acs.jproteome.5b00981>), differential expression analysis (Ritchie et. al. (2015) <doi:10.1093/nar/gkv007>), and machine learning-based modeling (Kuhn (2008) <doi:10.18637/jss.v028.i05>).
	"""
	
	homepage = "https://github.com/caranathunge/promor"
	cran = "promor" 

	version("0.2.1", md5="2f152bf6ecee4afd2ad6e935f769cb65")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-pcamethods", type=("build", "run"))
	depends_on("r-vim", type=("build", "run"))
	depends_on("r-missforest", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
	depends_on("r-naivebayes", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
