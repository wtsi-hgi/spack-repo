# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAccelstab(RPackage):
	"""Accelerated Stability Kinetic Modelling

	Estimate the Šesták–Berggren kinetic model (degradation model) from experimental data. A
  A closed-form (analytic) solution to the degradation model is implemented as a non-linear fit,
  allowing for the extrapolation of the degradation of a drug product - both in time and 
  temperature. Parametric bootstrap, with kinetic parameters drawn from the multivariate
  t-distribution, and analytical formulae (the delta method) are available options to calculate
  the confidence and prediction intervals.
  The results (modelling, extrapolations and statistical intervals) can be visualised
  with multiple plots. The examples illustrate the accelerated stability modelling in drugs and
  vaccines development.
	"""
	
	homepage = "https://github.com/AccelStab/AccelStab"
	cran = "AccelStab" 

	version("2.0.0", md5="3929d120fc8c6f5d539a3be686566f50")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
