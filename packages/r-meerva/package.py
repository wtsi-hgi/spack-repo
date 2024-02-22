# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeerva(RPackage):
	"""Analysis of Data with Measurement Error Using a Validation
Subsample

	Sometimes data for analysis are obtained using more convenient or less expensive means yielding "surrogate" variables for what could be obtained more accurately, albeit with less convenience; or less conveniently or at more expense yielding "reference" variables, thought of as being measured without error. Analysis of the surrogate variables measured with error generally yields biased estimates when the objective is to make inference about the reference variables. Often it is thought that ignoring the measurement error in surrogate variables only biases effects toward the null hypothesis, but this need not be the case. Measurement errors may bias parameter estimates either toward or away from the null hypothesis.    If one has a data set with surrogate variable data from the full sample, and also reference variable data from a randomly selected subsample, then one can assess the bias introduced by measurement error in parameter estimation, and use this information to derive improved estimates based upon all available data. Formulaically these estimates based upon the reference variables from the validation subsample combined with the surrogate variables from the whole sample can be interpreted as starting with the estimate from reference variables in the validation subsample, and "augmenting" this with additional information from the surrogate variables. This suggests the term "augmented" estimate.    The meerva package calculates these augmented estimates in the regression setting when there is a randomly selected subsample with both surrogate and reference variables. Measurement errors may be differential or non-differential, in any or all predictors (simultaneously) as well as outcome. The augmented estimates derive, in part, from the multivariate correlation between regression model parameter estimates from the reference variables and the surrogate variables, both from the validation subset. Because the validation subsample is chosen at random any biases imposed by measurement error, whether non-differential or differential, are reflected in this correlation and these correlations can be used to derive estimates for the reference variables using data from the whole sample.    The main functions in the package are meerva.fit which calculates estimates for a dataset, and meerva.sim.block which simulates multiple datasets as described by the user, and analyzes these datasets, storing the regression coefficient estimates for inspection.  The augmented estimates, as well as how measurement error may arise in practice, is described in more detail by Kremers WK (2021) <arXiv:2106.14063> and is an extension of the works by Chen Y-H, Chen H. (2000) <doi:10.1111/1467-9868.00243>, Chen Y-H. (2002) <doi:10.1111/1467-9868.00324>, Wang X, Wang Q (2015) <doi:10.1016/j.jmva.2015.05.017> and Tong J, Huang J, Chubak J, et al. (2020) <doi:10.1093/jamia/ocz180>.
	"""
	
	cran = "meerva" 

	version("0.2-2", md5="b0169b720bdc0f1c601bd84a24a472fb")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
