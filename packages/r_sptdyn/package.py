# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSptdyn(RPackage):
	"""Spatially Varying and Spatio-Temporal Dynamic Linear Models

	Fits, spatially predicts, and temporally forecasts space-time data using Gaussian Process (GP): (1) spatially varying coefficient process models and (2) spatio-temporal dynamic linear models. Bakar et al., (2016). Bakar et al., (2015).
	"""
	
	cran = "spTDyn" 

	version("2.0.2", md5="05084d70699a07e7cbff5874f7562b18")

	depends_on("r@3.4.1:", type=("build", "run"))
	depends_on("r-sptimer", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-spacetime", type=("build", "run"))
