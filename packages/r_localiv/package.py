# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLocaliv(RPackage):
	"""Estimation of Marginal Treatment Effects using Local
Instrumental Variables

	In the generalized Roy model, the marginal treatment effect (MTE) can be used as
  a building block for constructing conventional causal parameters such as the average treatment
  effect (ATE) and the average treatment effect on the treated (ATT). Given a treatment selection
  equation and an outcome equation, the function mte() estimates the MTE via the semiparametric
  local instrumental variables method or the normal selection model. The function mte_at() evaluates
  MTE at different values of the latent resistance u with a given X = x, and the function mte_tilde_at()
  evaluates MTE projected onto the estimated propensity score. The function ace() estimates
  population-level average causal effects such as ATE, ATT, or the marginal policy relevant
  treatment effect.
	"""
	
	homepage = "https://github.com/xiangzhou09/localIV"
	cran = "localIV" 

	version("0.3.1", md5="27aeb329ba7d1c506e3e8b965b689ff8")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-kernsmooth@2.5:", type=("build", "run"))
	depends_on("r-mgcv@1.8.19:", type=("build", "run"))
	depends_on("r-rlang@0.4.4:", type=("build", "run"))
	depends_on("r-sampleselection@1.2.0:", type=("build", "run"))
