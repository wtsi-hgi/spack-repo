# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmoothhr(RPackage):
	"""Smooth Hazard Ratio Curves Taking a Reference Value

	Provides flexible hazard ratio curves allowing non-linear
  relationships between continuous predictors and survival.
  To better understand the effects that each continuous covariate
  has on the outcome, results are expressed in terms of hazard
  ratio curves, taking a specific covariate value as reference.
  Confidence bands for these curves are also derived.
	"""
	
	homepage = "https://github.com/arturstat/smoothHR"
	cran = "smoothHR" 

	version("1.0.5", md5="ce6aae28de56e486d59c2a10f2b57262")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
