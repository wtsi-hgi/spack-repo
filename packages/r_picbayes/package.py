# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPicbayes(RPackage):
	"""Bayesian Models for Partly Interval-Censored Data

	Contains functions to fit proportional hazards (PH) model to partly interval-censored (PIC) data (Pan et al. (2020) <doi:10.1177/0962280220921552>), PH model with spatial frailty to spatially dependent PIC data (Pan and Cai (2021) <doi:10.1080/03610918.2020.1839497>), and mixed effects PH model to clustered PIC data. Each random intercept/random effect can follow both a normal prior and a Dirichlet process mixture prior. It also includes the corresponding functions for general interval-censored data.
	"""
	
	cran = "PICBayes" 

	version("1.0", md5="4e4d312150149d937c756bf19247b7b2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
