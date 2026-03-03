# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMbmethpred(RPackage):
	"""Medulloblastoma Subgroups Prediction

	Utilizing a combination of machine learning models (Random Forest, Naive Bayes, K-Nearest Neighbor, Support Vector Machines, Extreme Gradient Boosting, and Linear Discriminant Analysis) and a deep Artificial Neural Network model, 'MBMethPred' can predict medulloblastoma subgroups, including wingless (WNT), sonic hedgehog (SHH), Group 3, and Group 4 from DNA methylation beta values. See Sharif Rahmani E, Lawarde A, Lingasamy P, Moreno SV, Salumets A and Modhukur V (2023), MBMethPred: a computational framework for the accurate classification of childhood medulloblastoma subgroups using data integration and AI-based approaches. Front. Genet. 14:1233657. <doi: 10.3389/fgene.2023.1233657> for more details.
	"""
	
	homepage = "https://github.com/sharifrahmanie/MBMethPred"
	cran = "MBMethPred" 

	version("0.1.4.2", md5="5340283d22c69c1ca09eeb27b06fb5b9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-keras", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-snftool", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-tensorflow", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
