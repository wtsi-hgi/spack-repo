# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesmixsurv(RPackage):
	"""Bayesian Mixture Survival Models using Additive
Mixture-of-Weibull Hazards, with Lasso Shrinkage and
Stratification

	Bayesian Mixture Survival Models using Additive Mixture-of-Weibull Hazards, with Lasso Shrinkage and
        Stratification. As a Bayesian dynamic survival model, it relaxes the proportional-hazard assumption. Lasso shrinkage controls
        overfitting, given the increase in the number of free parameters in the model due to presence of two Weibull components
        in the hazard function.
	"""
	
	cran = "BayesMixSurv" 

	version("0.9.1", md5="5a4d193c7b9e3b29a27381dc7e9beac8")

	depends_on("r-survival", type=("build", "run"))
