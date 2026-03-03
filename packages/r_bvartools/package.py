# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBvartools(RPackage):
	"""Bayesian Inference of Vector Autoregressive and Error Correction
Models

	Assists in the set-up of algorithms for Bayesian inference of vector autoregressive (VAR) and error correction (VEC) models. Functions for posterior simulation, forecasting, impulse response analysis and forecast error variance decomposition are largely based on the introductory texts of Chan, Koop, Poirier and Tobias (2019, ISBN: 9781108437493), Koop and Korobilis (2010) <doi:10.1561/0800000013> and Luetkepohl (2006, ISBN: 9783540262398).
	"""
	
	homepage = "https://github.com/franzmohr/bvartools"
	cran = "bvartools" 

	version("0.2.4", md5="f8502f427840d20b0b1dc790f2b3b799")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
