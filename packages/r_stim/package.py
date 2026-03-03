# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStim(RPackage):
	"""Incorporating Stability Information into Cross-Sectional
Estimates

	The goal of 'stim' is to provide a function for estimating the Stability Informed Model. The Stability Informed Model integrates stability information (how much a variable correlates with itself in the future) into cross-sectional estimates. Wysocki and Rhemtulla (2022) <https://psyarxiv.com/vg5as>. 
	"""
	
	cran = "stim" 

	version("1.0.0", md5="2d5fd926904003207825b5a370e21d5f")

	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-ryacas", type=("build", "run"))
