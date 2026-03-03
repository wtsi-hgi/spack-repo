# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKappalab(RPackage):
	"""Non-Additive Measure and Integral Manipulation Functions

	S4 tool box for capacity (or non-additive measure, fuzzy measure) and integral manipulation in a finite setting. It contains routines for handling various types of set functions such as games or capacities. It can be used to compute several non-additive integrals: the Choquet integral, the Sugeno integral, and the symmetric and asymmetric Choquet integrals. An analysis of capacities in terms of decision behavior can be performed through the computation of various indices such as the Shapley value, the interaction index, the orness degree, etc. The well-known Möbius transform, as well as other equivalent representations of set functions can also be computed. Kappalab further contains seven capacity identification routines: three least squares based approaches, a method based on linear programming, a maximum entropy like method based on variance minimization, a minimum distance approach and an unsupervised approach based on parametric entropies. The functions contained in Kappalab can for instance be used in the framework of multicriteria decision making or cooperative game theory.
	"""
	
	cran = "kappalab" 

	version("0.4-12", md5="cd88e018c6513b3931021f2391c6282b")

	depends_on("r@2.1:", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
