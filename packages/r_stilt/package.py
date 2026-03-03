# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStilt(RPackage):
	"""Separable Gaussian Process Interpolation (Emulation)

	Functions for simplified emulation of time series computer model output in model parameter space using Gaussian processes. Stilt can be used more generally for Kriging of spatio-temporal fields. There are functions to predict at new parameter settings, to test the emulator using cross-validation (which includes information on 95% confidence interval empirical coverage), and to produce contour plots over 2D slices in model parameter space.
	"""
	
	cran = "stilt" 

	version("1.3.0", md5="9043c4a91c81c778e73d9fc480ca0f49")

	depends_on("r@3.2.4:", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
