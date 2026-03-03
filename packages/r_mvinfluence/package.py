# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvinfluence(RPackage):
	"""Influence Measures and Diagnostic Plots for Multivariate Linear
Models

	Computes regression deletion diagnostics for multivariate linear models and provides some associated
	diagnostic plots.  The diagnostic measures include hat-values (leverages), generalized Cook's distance, and
	generalized squared 'studentized' residuals.  Several types of plots to detect influential observations are
	provided.
	"""
	
	homepage = "https://github.com/friendly/mvinfluence"
	cran = "mvinfluence" 

	version("0.9.0", md5="94a0118a86ebebc8b5f8f2e06e643b18")

	depends_on("r-car", type=("build", "run"))
	depends_on("r-heplots", type=("build", "run"))
