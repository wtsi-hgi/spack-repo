# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMinb(RPackage):
	"""Multiple-Inflated Negative Binomial Model

	Count data is prevalent and informative, with widespread
    application in many fields such as social psychology, personality, and
    public health. Classical statistical methods for the analysis of count
    outcomes are commonly variants of the log-linear model, including
    Poisson regression and Negative Binomial regression. However, a
    typical problem with count data modeling is inflation, in the sense
    that the counts are evidently accumulated on some integers. Such an
    inflation problem could distort the distribution of the observed
    counts, further bias estimation and increase error, making the classic
    methods infeasible. Traditional inflated value selection methods based
    on histogram inspection are easy to neglect true points and
    computationally expensive in addition. Therefore, we propose a
    multiple-inflated negative binomial model to handle count data
    modeling with multiple inflated values, achieving data-driven inflated
    value selection. The proposed approach provides simultaneous
    identification of important regression predictors on the target count
    response as well. More details about the proposed method are described in 
    Li, Y., Wu, M., Wu, M., & Ma, S. (2023) <arXiv:2309.15585>.
	"""
	
	cran = "minb" 

	version("0.1.0", md5="a954b56d9f6480d86a1788f7bc8cd2f1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pscl", type=("build", "run"))
