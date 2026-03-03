# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhasetype(RPackage):
	"""Inference for Phase-Type Distributions

	Functions to perform Bayesian inference on absorption time data for
             Phase-type distributions. The methods of Bladt et al (2003)
             <doi:10.1080/03461230110106435> and Aslett (2012)
             <https://www.louisaslett.com/PhD_Thesis.pdf> are provided.
	"""
	
	homepage = "https://www.louisaslett.com/PhaseType/"
	cran = "PhaseType" 

	version("0.2.1", md5="c0f155211da2095b272b96a5ccbbbddc")

	depends_on("r-coda", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
