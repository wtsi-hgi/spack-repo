# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQwdap(RPackage):
	"""Quantum Walk-Based Data Analysis and Prediction

	The modeling and prediction of graph-associated time series(GATS) based on continuous time quantum walk. This software is mainly used for feature extraction, modeling, prediction and result evaluation of GATS, including continuous time quantum walk simulation, feature selection, regression analysis, time series prediction, and series fit calculation.
	"""
	
	cran = "QWDAP" 

	version("1.1.17", md5="8e088d97d5605f953b24dd2f2a27cc13")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-corelearn", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
