# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrfa(RPackage):
	"""Fitting and Predicting Large-Scale Nonlinear Regression Problems
using Multi-Resolution Functional ANOVA (MRFA) Approach

	Performs the MRFA approach proposed by Sung et al. (2020) <doi:10.1080/01621459.2019.1595630> to fit
    and predict nonlinear regression problems, particularly for large-scale and
    high-dimensional problems. The application includes deterministic or stochastic
    computer experiments, spatial datasets, and so on.
	"""
	
	cran = "MRFA" 

	version("0.6", md5="b354c09de763256f66c151f418967523")

	depends_on("r@2.14.1:", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-grplasso", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-randtoolbox", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
