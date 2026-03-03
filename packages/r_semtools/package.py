# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemtools(RPackage):
	"""Useful Tools for Structural Equation Modeling

	Provides tools for structural equation modeling, many of which extend the 'lavaan' package; for example, to pool results from multiple imputations, probe latent interactions, or test measurement invariance.
	"""
	
	homepage = "https://github.com/simsem/semTools/wiki"
	cran = "semTools" 

	version("0.5-6", md5="65c8934f32d8a192ac411117671d5735")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-lavaan@0.6.11:", type=("build", "run"))
	depends_on("r-pbivnorm", type=("build", "run"))
