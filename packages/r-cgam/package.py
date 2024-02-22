# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCgam(RPackage):
	"""Constrained Generalized Additive Model

	A constrained generalized additive model is fitted by the cgam routine. Given a set of predictors, each of which may have a shape or order restrictions, the maximum likelihood estimator for the constrained generalized additive model is found using an iteratively re-weighted cone projection algorithm. The ShapeSelect routine chooses a subset of predictor variables and describes the component relationships with the response. For each predictor, the user needs only specify a set of possible shape or order restrictions. A model selection method chooses the shapes and orderings of the relationships as well as the variables. The cone information criterion (CIC) is used to select the best combination of variables and shapes. A genetic algorithm may be used when the set of possible models is large. In addition, the cgam routine implements a two-dimensional isotonic regression using warped-plane splines without additivity assumptions.  It can also fit a convex or concave regression surface with triangle splines without additivity assumptions. See Liao X, Meyer MC (2019)<doi:10.18637/jss.v089.i05> for more details.
	"""
	
	cran = "cgam" 

	version("1.21", md5="9eacc80dfb68f5b788f71a1667dcd5b1")

	depends_on("r-coneproj@1.12:", type=("build", "run"))
	depends_on("r-svdialogs@0.9.57:", type=("build", "run"))
	depends_on("r-statmod@1.4.36:", type=("build", "run"))
	depends_on("r-lme4@1.1.13:", type=("build", "run"))
	depends_on("r-matrix@1.2.8:", type=("build", "run"))
	depends_on("r@3.0.2:", type=("build", "run"))
