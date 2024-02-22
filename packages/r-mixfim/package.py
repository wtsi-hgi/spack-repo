# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixfim(RPackage):
	"""Evaluation of the FIM in NLMEMs using MCMC

	Evaluation and optimization of the Fisher Information Matrix in NonLinear Mixed Effect Models using Markov Chains Monte Carlo for continuous and discrete data.
	"""
	
	cran = "MIXFIM" 

	version("1.1", md5="f3304350d00e8c14b54622119fc864be")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rstan@2.7.0.1:", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.2:", type=("build", "run"))
	depends_on("r-ggplot2@1.0.1:", type=("build", "run"))
