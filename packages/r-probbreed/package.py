# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProbbreed(RPackage):
	"""Probability Theory for Selecting Candidates in Plant Breeding

	Use probability theory under the Bayesian framework for calculating the risk of selecting candidates in a multi-environment context [Dias et al. (2022) <doi:10.1007/s00122-022-04041-y>]. Contained are functions used to fit a Bayesian multi-environment model (based on the available presets), extract posterior values and maximum posterior values, compute the variance components, check the model’s convergence, and calculate the probabilities. For both across and within-environments scopes, the package computes the probability of superior performance and the pairwise probability of superior performance. Furthermore, the probability of superior stability and the pairwise probability of superior stability across environments is estimated. A joint probability of superior performance and stability is also provided. 
	"""
	
	homepage = "https://github.com/saulo-chaves/ProbBreed"
	cran = "ProbBreed" 

	version("1.0.3.1", md5="67177c855ce1c69be5601dc26466fae9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rstan", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
