# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbw(RPackage):
	"""Residual Balancing Weights for Marginal Structural Models

	Residual balancing is a robust method of constructing weights for
  marginal structural models, which can be used to estimate (a) the average treatment effect in 
  a cross-sectional observational study, (b) controlled direct/mediator effects in causal mediation
  analysis, and (c) the effects of time-varying treatments in panel data (Zhou and Wodtke 2020
  <doi:10.1017/pan.2020.2>). This package provides three functions, rbwPoint(), rbwMed(), and rbwPanel(),
  that produce residual balancing weights for estimating (a), (b), (c), respectively.
	"""
	
	homepage = "https://github.com/xiangzhou09/rbw"
	cran = "rbw" 

	version("0.3.2", md5="f2f1379c4702601b984c896124c53025")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@0.8.4:", type=("build", "run"))
	depends_on("r-rlang@0.4.4:", type=("build", "run"))
