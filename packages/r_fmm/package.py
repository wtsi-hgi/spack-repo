# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFmm(RPackage):
	"""Rhythmic Patterns Modeling by FMM Models

	Provides a collection of functions to fit and explore single, multi-component and restricted Frequency Modulated Moebius (FMM) models. 'FMM' is a nonlinear parametric regression model capable of fitting non-sinusoidal shapes in rhythmic patterns. Details about the mathematical formulation of 'FMM' models can be found in Rueda et al. (2019) <doi:10.1038/s41598-019-54569-1>.
	"""
	
	homepage = "https://github.com/alexARC26/FMM"
	cran = "FMM" 

	version("0.3.1", md5="9bb016f18a2709aae6c2669aa52ac65f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
