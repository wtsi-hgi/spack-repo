# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcenreg(RPackage):
	"""Regression Models for Interval Censored Data

	Regression models for interval censored data. Currently supports
    Cox-PH, proportional odds, and accelerated failure time models. Allows for
    semi and fully parametric models (parametric only for accelerated failure
    time models) and Bayesian parametric models. Includes functions for easy visual
    diagnostics of model fits and imputation of censored data.
	"""
	
	cran = "icenReg" 

	version("2.0.16", md5="1d39dabd1838fbf2dbf7dde2fa968000")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-mlecens", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
