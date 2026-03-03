# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGoweragreement(RPackage):
	"""Bayesian Gower Agreement for Categorical Data

	Provides tools for applying the Bayesian Gower agreement methodology (presented in the package vignette) to nominal or ordinal data. The framework can accommodate any number of units, any number of coders, and missingness; and can handle both one-way and two-way random study designs. Influential units and/or coders can be identified easily using leave-one-out statistics.
	"""
	
	homepage = "http://www.johnhughes.org"
	cran = "goweragreement" 

	version("1.0", md5="0b3ec431fda64ffd13c687473d8a4d1b")

	depends_on("r@3.5:", type=("build", "run"))
