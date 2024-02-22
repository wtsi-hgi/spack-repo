# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLongke(RPackage):
	"""Nonparametric Predictive Model for Sparse and Irregular
Longitudinal Data

	The proposed method aims at predicting the longitudinal mean response trajectory by a 
              kernel-based estimator. The kernel estimator is constructed by imposing weights based on 
              subject-wise similarity on L2 metric space between predictor trajectories as well as time proximity. 
              Users could also perform variable selections to derive functional predictors with predictive significance
              by the proposed multiplicative model with multivariate Gaussian kernels.
	"""
	
	cran = "longke" 

	version("0.1.0", md5="4c1477f063149bc0b273c7ccce8bdc90")

	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-bvls", type=("build", "run"))
	depends_on("r-fdapace", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
