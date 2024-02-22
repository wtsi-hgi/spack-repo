# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RContresppp(RPackage):
	"""Predictive Probability for a Continuous Response with an ANOVA
Structure

	A Bayesian approach to using 
    predictive probability in an ANOVA construct with a continuous normal response, 
    when threshold values must be obtained for the question of interest to be 
    evaluated as successful (Sieck and Christensen (2021) <doi:10.1002/qre.2802>). 
    The Bayesian Mission Mean (BMM) is used to evaluate a question 
    of interest (that is, a mean that randomly selects combination of factor levels 
    based on their probability of occurring instead of averaging over the factor 
    levels, as in the grand mean). Under this construct, in contrast to a Gibbs 
    sampler (or Metropolis-within-Gibbs sampler), a two-stage sampling method is 
    required. The nested sampler determines the conditional posterior distribution 
    of the model parameters, given Y, and the outside sampler determines the marginal 
    posterior distribution of Y (also commonly called the predictive distribution for Y). 
    This approach provides a sample from the joint posterior distribution of Y and 
    the model parameters, while also accounting for the threshold value that must be 
    obtained in order for the question of interest to be evaluated as successful.
	"""
	
	homepage = "https://github.com/jcliff89/ContRespPP"
	cran = "ContRespPP" 

	version("0.4.2", md5="83f82b8346162b21580014aad08fafcb")

	depends_on("r@2.10:", type=("build", "run"))
