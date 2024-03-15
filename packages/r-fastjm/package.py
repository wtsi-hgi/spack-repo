# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastjm(RPackage):
	"""Semi-Parametric Joint Modeling of Longitudinal and Survival Data

	Maximum likelihood estimation for the semi-parametric joint modeling of competing risks and longitudinal data applying customized linear scan algorithms, proposed by Li and colleagues (2022) <doi:10.1155/2022/1362913>. 
             The time-to-event data is modelled using a (cause-specific) Cox proportional hazards regression model with time-fixed covariates. The longitudinal 
             outcome is modelled using a linear mixed effects model. The association is captured by shared random effects. The model 
             is estimated using an Expectation Maximization algorithm.
	"""
	
	cran = "FastJM" 

	version("1.4.2", md5="3f5b17d931e9ab5dc9d6e5822fbee0fd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-timeroc", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
