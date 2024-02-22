# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKosel(RPackage):
	"""Variable Selection by Revisited Knockoffs Procedures

	Performs variable selection for many types of L1-regularised regressions using the revisited knockoffs procedure. This procedure uses a matrix of knockoffs of the covariates independent from the response variable Y. The idea is to determine if a covariate belongs to the model depending on whether it enters the model before or after its knockoff. The procedure suits for a wide range of regressions with various types of response variables. Regression models available are exported from the R packages 'glmnet' and 'ordinalNet'. Based on the paper linked to via the URL below: Gegout A., Gueudin A., Karmann C. (2019) <arXiv:1907.03153>.
	"""
	
	homepage = "https://arxiv.org/pdf/1907.03153.pdf"
	cran = "kosel" 

	version("0.0.1", md5="cf868dacc48b118e022a68afdbd2bf8e")

	depends_on("r@1.1:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-ordinalnet", type=("build", "run"))
