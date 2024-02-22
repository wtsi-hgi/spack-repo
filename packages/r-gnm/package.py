# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGnm(RPackage):
	"""Generalized Nonlinear Models

	Functions to specify and fit generalized nonlinear models,
    including models with multiplicative interaction terms such as the
    UNIDIFF model from sociology and the AMMI model from crop science, and
    many others.  Over-parameterized representations of models are used
    throughout; functions are provided for inference on estimable
    parameter combinations, as well as standard methods for diagnostics
    etc.
	"""
	
	homepage = "https://github.com/hturner/gnm"
	cran = "gnm" 

	version("1.1-5", md5="9f281639da06726027e78b0465563d0c")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-qvcalc@0.8.3:", type=("build", "run"))
	depends_on("r-relimp", type=("build", "run"))
