# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmars(RPackage):
	"""Implementation of the Conic Multivariate Adaptive Regression
Splines in R

	An implementation of 'Conic Multivariate Adaptive Regression Splines (CMARS)' in R.
    See Weber et al. (2011) CMARS: a new contribution to nonparametric regression with 
    multivariate adaptive regression splines supported by continuous optimization, 
    <DOI:10.1080/17415977.2011.624770>. It constructs models by using the terms
    obtained from the forward step of MARS and then estimates parameters by using 
    'Tikhonov' regularization and conic quadratic optimization. It is possible to 
    construct models for prediction and binary classification. It provides performance 
    measures for the model developed. The package needs the optimisation software 'MOSEK' 
    <https://www.mosek.com/> to construct the models. Please follow the instructions in 
    'Rmosek' for the installation. 
	"""
	
	cran = "cmaRs" 

	version("0.1.3", md5="e9ef83c923761752d50585420b2c2c09")

	depends_on("r-earth", type=("build", "run"))
	depends_on("r-rmosek", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-auc", type=("build", "run"))
	depends_on("r-ryacas0", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-mpv", type=("build", "run"))
