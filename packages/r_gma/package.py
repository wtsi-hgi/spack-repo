# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGma(RPackage):
	"""Granger Mediation Analysis

	Performs Granger mediation analysis (GMA) for time series. This package includes a single level GMA model and a two-level GMA model, for time series with hierarchically nested structure. The single level GMA model for the time series of a single participant performs the causal mediation analysis which integrates the structural equation modeling and the Granger causality frameworks. A vector autoregressive model of order p is employed to account for the spatiotemporal dependencies in the data. Meanwhile, the model introduces the unmeasured confounding effect through a nonzero correlation parameter. Under the two-level model, by leveraging the variabilities across participants, the parameters are identifiable and consistently estimated based on a full conditional likelihood or a two-stage method. See Zhao, Y., & Luo, X. (2017), Granger Mediation Analysis of Multiple Time Series with an Application to fMRI, <arXiv:1709.05328> for details.
	"""
	
	cran = "gma" 

	version("1.0", md5="a9e74bf8817eda34aea112ac0f90556e")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
