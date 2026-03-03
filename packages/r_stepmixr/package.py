# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStepmixr(RPackage):
	"""Interface to 'Python' Package 'StepMix'

	This is an interface for the 'Python' package
  'StepMix'. It is a 'Python' package following the scikit-learn API for
  model-based clustering and generalized mixture modeling (latent class/profile
  analysis) of continuous and categorical data. 'StepMix' handles missing values
  through Full Information Maximum Likelihood (FIML) and provides multiple stepwise
  Expectation-Maximization (EM) estimation methods based on pseudolikelihood
  theory. Additional features include support for covariates and distal outcomes,
  various simulation utilities, and non-parametric bootstrapping, which allows
  inference in semi-supervised and unsupervised settings. 
	"""
	
	homepage = "https://github.com/Labo-Lacourse/StepMixr"
	cran = "stepmixr" 

	version("0.1.2", md5="eacfe6502e28751ec6b7c55b6eb30f36")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-reticulate@1.8:", type=("build", "run"))
