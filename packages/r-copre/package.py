# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCopre(RPackage):
	"""Tools for Nonparametric Martingale Posterior Sampling

	Performs Bayesian nonparametric density estimation using Martingale
 posterior distributions including the Copula Resampling (CopRe) algorithm. 
 Also included are a Gibbs sampler for the marginal Gibbs-type mixture model and
 an extension to include full uncertainty quantification via a predictive 
 sequence resampling (SeqRe) algorithm. The CopRe and SeqRe samplers generate 
 random nonparametric distributions as output, leading to complete nonparametric 
 inference on posterior summaries. Routines for calculating arbitrary 
 functionals from the sampled distributions are included as well as an important 
 algorithm for finding the number and location of modes, which can then be used 
 to estimate the clusters in the data using, for example, k-means.
 Implements work developed in Moya B., Walker S. G. (2022).
 <doi:10.48550/arxiv.2206.08418>, Fong, E., Holmes, C., Walker, S. G. (2021) 
 <doi:10.48550/arxiv.2103.15671>, and Escobar M. D., West, M. (1995) 
 <doi:10.1080/01621459.1995.10476550>.
	"""
	
	cran = "copre" 

	version("0.2.0", md5="d95789e18ae1f63605d65c7b4ea64bf8")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-dirichletprocess", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
