# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpldv(RPackage):
	"""Spatial Models for Limited Dependent Variables

	The current version of this package estimates spatial autoregressive models for binary dependent variables using GMM estimators <doi:10.18637/jss.v107.i08>. It supports one-step (Pinkse and Slade, 1998) <doi:10.1016/S0304-4076(97)00097-3> and two-step GMM estimator along with the linearized GMM estimator proposed by Klier and McMillen (2008) <doi:10.1198/073500107000000188>. It also allows for either Probit or Logit model and compute the average marginal effects. All these models are presented in Sarrias and Piras (2023) <doi:10.1016/j.jocm.2023.100432>. 
	"""
	
	homepage = "https://github.com/gpiras/spldv"
	cran = "spldv" 

	version("0.1.3", md5="776cd2da5177e87fc9d7b2c89bc6534a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-maxlik", type=("build", "run"))
	depends_on("r-sphet", type=("build", "run"))
	depends_on("r-memisc", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-spatialreg", type=("build", "run"))
