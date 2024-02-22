# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvreg(RPackage):
	"""Evidential Regression

	An implementation of the 'Evidential Neural Network for Regression' model recently introduced in Denoeux (2023) <doi:10.36227/techrxiv.21791831.v1>. In this model, prediction uncertainty is quantified by Gaussian random fuzzy numbers as introduced in Denoeux (2023) <doi:10.1016/j.fss.2022.06.004>. The package contains functions for training the network, tuning hyperparameters by cross-validation or the hold-out method, and making predictions. It also contains utilities for making calculations with Gaussian random fuzzy numbers (such as, e.g., computing the degrees of belief and plausibility of an interval, or combining Gaussian random fuzzy numbers).
	"""
	
	cran = "evreg" 

	version("1.0.3", md5="acb6128f970c03d8a28c755670f9b934")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-evclust", type=("build", "run"))
