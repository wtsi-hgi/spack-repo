# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPre(RPackage):
	"""Prediction Rule Ensembles

	Derives prediction rule ensembles (PREs). Largely follows the
    procedure for deriving PREs as described in Friedman & Popescu (2008; 
    <DOI:10.1214/07-AOAS148>), with adjustments and improvements. The 
    main function pre() derives prediction rule ensembles consisting of 
    rules and/or linear terms for continuous, binary, count, multinomial, 
    and multivariate continuous responses. Function gpe() derives 
    generalized prediction ensembles, consisting of rules, hinge and linear 
    functions of the predictor variables.
	"""
	
	homepage = "https://github.com/marjoleinF/pre"
	cran = "pre" 

	version("1.0.7", md5="99ce1e91ea36310face37c8953f54438")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-earth", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-partykit@1.2.0:", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixmodels", type=("build", "run"))
