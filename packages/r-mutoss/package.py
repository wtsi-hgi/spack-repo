# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMutoss(RPackage):
	"""Unified Multiple Testing Procedures.

	Designed to ease the application and comparison of multiple hypothesis
	testing procedures for FWER, gFWER, FDR and FDX. Methods are standardized
	and usable by the accompanying 'mutossGUI'."""

	cran = "mutoss"
	version("0.1-12", sha256="2889ae3d502157592697124eb86adc14911e2b7fdaa7204743a376b1eeb967fa")
	version("0.1-13", md5="4384e17eb4ebf0f3370e232dbebe39b5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-multtest@2.2:", type=("build", "run"))
	depends_on("r-multcomp@1.1.0:", type=("build", "run"))
