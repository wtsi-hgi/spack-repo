# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDetectseparation(RPackage):
	"""Detect and Check for Separation and Infinite Maximum Likelihood
Estimates

	Provides pre-fit and post-fit methods for detecting separation and infinite maximum likelihood estimates in generalized linear models with categorical responses. The pre-fit methods apply on binomial-response generalized liner models such as logit, probit and cloglog regression, and can be directly supplied as fitting methods to the glm() function. They solve the linear programming problems for the detection of separation developed in Konis (2007, <https://ora.ox.ac.uk/objects/uuid:8f9ee0d0-d78e-4101-9ab4-f9cbceed2a2a>) using 'ROI' <https://cran.r-project.org/package=ROI> or 'lpSolveAPI' <https://cran.r-project.org/package=lpSolveAPI>. The post-fit methods apply to models with categorical responses, including binomial-response generalized linear models and multinomial-response models, such as baseline category logits and adjacent category logits models; for example, the models implemented in the 'brglm2' <https://cran.r-project.org/package=brglm2> package. The post-fit methods successively refit the model with increasing number of iteratively reweighted least squares iterations, and monitor the ratio of the estimated standard error for each parameter to what it has been in the first iteration. According to the results in Lesaffre & Albert (1989, <https://www.jstor.org/stable/2345845>), divergence of those ratios indicates data separation.
	"""
	
	homepage = "https://github.com/ikosmidis/detectseparation"
	cran = "detectseparation" 

	version("0.3", md5="b9f9544b8bda35c85b78795c883ffda1")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-roi", type=("build", "run"))
	depends_on("r-roi-plugin-lpsolve", type=("build", "run"))
	depends_on("r-lpsolveapi", type=("build", "run"))
	depends_on("r-pkgload", type=("build", "run"))
