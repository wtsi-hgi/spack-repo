# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVgamextra(RPackage):
	"""Additions and Extensions of the 'VGAM' Package

	Extending the functionalities of the 'VGAM' package with
         additional functions and datasets. At present, 'VGAMextra'
         comprises new family functions (ffs) to estimate several time
         series models by maximum likelihood using Fisher scoring, 
         unlike popular packages in CRAN relying on optim(), including
         ARMA-GARCH-like models, the Order-(p, d, q) ARIMAX model (non-
         seasonal), the Order-(p) VAR model, error correction models
         for cointegrated time series, and ARMA-structures with Student-t 
         errors. For independent data, new ffs to estimate the inverse-
         Weibull, the inverse-gamma, the generalized beta of the second
         kind and the general multivariate normal distributions are
         available. In addition, 'VGAMextra' incorporates new VGLM-links
         for the mean-function, and the quantile-function (as an alternative
         to ordinary quantile modelling) of several 1-parameter distributions,
         that are compatible with the class of VGLM/VGAM family functions.
         Currently, only fixed-effects models are implemented. All functions
         are subject to change; see the NEWS for further details on the
         latest changes.
	"""
	
	cran = "VGAMextra" 

	version("0.0-6", md5="7abf738d9b09a501606c5d43fac5842b")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-vgam@1:", type=("build", "run"))
