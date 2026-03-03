# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBaskepro(RPackage):
	"""Bayesian Model to Archaeological Faunal Skeletal Profiles

	Tool to perform Bayesian inference of carcass processing/transport strategy and bone attrition from archaeofaunal skeletal profiles characterized by percentages of MAU (Minimum Anatomical Units). The approach is based on a generative model for skeletal profiles that replicates the two phases of formation of any faunal assemblage: initial accumulation as a function of human transport strategies and subsequent attrition.Two parameters define this model: 1) the transport preference (alpha), which can take any value between - 1 (mostly axial contribution) and 1 (mostly appendicular contribution) following strategies constructed as a function of butchering efficiency of different anatomical elements and the results of ethnographic studies, and 2) degree of attrition (beta), which can vary between 0 (no attrition) and 10 (maximum attrition) and relates the survivorship of bone elements to their maximum bone density. Starting from uniform prior probability distribution functions of alpha and beta, a Monte Carlo Markov Chain sampling based on a random walk Metropolis-Hasting algorithm is adopted to derive the posterior probability distribution functions, which are then available for interpretation. During this process, the likelihood of obtaining the observed percentages of MAU given a pair of parameter values is estimated by the inverse of the Chi2 statistic, multiplied by the proportion of elements within a 1 percent of the observed value. See Ana B. Marin-Arroyo, David Ocio (2018).<doi:10.1080/08912963.2017.1336620>.
	"""
	
	cran = "BaSkePro" 

	version("1.1.1", md5="847025499af13fbe4ebae23489eaad52")

	depends_on("r-mass", type=("build", "run"))
