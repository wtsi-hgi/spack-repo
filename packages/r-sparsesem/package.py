# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsesem(RPackage):
	"""Elastic Net Penalized Maximum Likelihood for Structural Equation
Models with Network GPT Framework

	Provides elastic net penalized maximum likelihood estimator for structural equation models (SEM). The package implements `lasso` and `elastic net` (l1/l2) penalized SEM and estimates the model parameters with an efficient block coordinate ascent algorithm that maximizes the penalized likelihood of the SEM.  Hyperparameters are inferred from cross-validation (CV).  A Stability Selection (STS) function is also available to provide accurate causal effect selection. The software achieves high accuracy performance through a `Network Generative Pre-trained Transformer` (Network GPT) Framework with two steps: 1) pre-trains the model to generate a complete (fully connected) graph; and 2) uses the complete graph as the initial state to fit the `elastic net` penalized SEM.
	"""
	
	cran = "sparseSEM" 

	version("4.0", md5="da8826c3571ccf3b5d7f7961747e1748")

	depends_on("r@3.5:", type=("build", "run"))
