# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrenchfish(RPackage):
	"""Poisson Models for Quantifying DNA Copy-number from FISH Images of Tissue Sections

	FrenchFISH comprises a nuclear volume correction method coupled with two types of Poisson models: either a Poisson model for improved manual spot counting without the need for control probes; or a homogenous Poisson Point Process model for automated spot counting.
	"""
	
	bioc = "frenchFISH"

	version("1.20.0", commit="a4db2d432a918689dcf878c58d4d1cb3fb06af82")
	version("1.14.0", commit="f7e75e5ef6586ff567bf706775b43ca552b6314f")

	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-nhpoisson", type=("build", "run"))
