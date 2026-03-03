# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConttimecausal(RPackage):
	"""Continuous Time Causal Models

	Implements the semiparametric efficient estimators of 
    continuous-time causal models for time-varying treatments and confounders 
    in the presence of dependent censoring (including structural failure time 
    model and Cox proportional hazards marginal structural model). 
    S. Yang, K. Pieper, and F. Cools (2019) <doi:10.1111/biom.12845>.
	"""
	
	cran = "contTimeCausal" 

	version("1.1", md5="ae8a03ba00c24125548870e49b599175")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
