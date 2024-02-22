# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlcirtwithin(RPackage):
	"""Latent Class Item Response Theory (LC-IRT) Models under
Within-Item Multidimensionality

	Framework for the Item Response Theory analysis of dichotomous and ordinal polytomous outcomes under the assumption of within-item multidimensionality and discreteness of the latent traits. The fitting algorithms allow for missing responses and for different item parametrizations and are based on the Expectation-Maximization paradigm. Individual covariates affecting the class weights may be included in the new version together with possibility of constraints on all model parameters.
	"""
	
	cran = "MLCIRTwithin" 

	version("2.1.1", md5="7ed87515fc6ee911bd5686affd008043")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-limsolve", type=("build", "run"))
	depends_on("r-multilcirt", type=("build", "run"))
