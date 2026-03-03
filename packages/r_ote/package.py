# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROte(RPackage):
	"""Optimal Trees Ensembles for Regression, Classification and Class
Membership Probability Estimation

	Functions for creating ensembles of optimal trees for regression, classification (Khan, Z., Gul, A., Perperoglou, A., Miftahuddin, M., Mahmoud, O., Adler, W., & Lausen, B. (2019). (2019) <doi:10.1007/s11634-019-00364-9>) and class membership probability estimation (Khan, Z, Gul, A, Mahmoud, O, Miftahuddin, M, Perperoglou, A, Adler, W & Lausen, B (2016) <doi:10.1007/978-3-319-25226-1_34>) are given. A few trees are selected from an initial set of trees grown by random forest for the ensemble on the basis of their individual and collective performance. Three different methods of tree selection for the case of classification are given. The prediction functions return estimates of the test responses and their class membership probabilities. Unexplained variations, error rates, confusion matrix, Brier scores, etc. are also returned for the test data.
	"""
	
	cran = "OTE" 

	version("1.0.1", md5="3b9fc7b6d3f259bbfd9343283693838f")

	depends_on("r-randomforest", type=("build", "run"))
