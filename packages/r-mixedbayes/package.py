# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixedbayes(RPackage):
	"""Bayesian Longitudinal Regularized Quantile Mixed Model

	In longitudinal studies, the same subjects are measured repeatedly over time, leading to correlations among the repeated measurements. Properly accounting for the intra-cluster correlations in the presence of data heterogeneity and long tailed distributions of the disease phenotype is challenging, especially in the context of high dimensional regressions. Here, we aim at developing novel Bayesian regularized quantile mixed effect models to tackle these challenges. We have proposed a Bayesian variable selection in the mixed effect models for longitudinal genomics studies. To dissect important gene - environment interactions, our model can simultaneously identify important main and interaction effects on the individual and group level, which have been facilitated by imposing the spike- and -slab priors through Laplacian shrinkage in the Bayesian quantile hierarchical models. The within - subject dependence among data can be accommodated by incorporating the random effects. An efficient Gibbs sampler has been developed to facilitate fast computation. The Markov chain Monte Carlo algorithms of the proposed and alternative methods are efficiently implemented in 'C++'. The development of this software package and the associated statistical methods have been partially supported by an Innovative Research Award from Johnson Cancer Research Center, Kansas State University.
	"""
	
	homepage = "https://github.com/kunfa/mixedBayes"
	cran = "mixedBayes" 

	version("0.1.2", md5="0b7bc3f6eb28d7f12900850aae8093cc")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
