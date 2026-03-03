# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicoptcm(RPackage):
	"""Promotion Time Cure Model with Mis-Measured Covariates

	Fits Semiparametric Promotion Time Cure Models, taking into account (using a 
			 corrected score approach or the SIMEX algorithm) or not the measurement error
			 in the covariates, using a backfitting approach to maximize the likelihood.
	"""
	
	cran = "miCoPTCM" 

	version("1.1", md5="9c000c8837042f6e694aa35a9ff9fa6e")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-distr", type=("build", "run"))
