# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnvgsadata(RPackage):
	"""Data used in the vignette of the cnvGSA package

	This package contains the data used in the vignette of the cnvGSA package.
	"""
	
	bioc = "cnvGSAdata"

	version("1.44.0", commit="ea3968fb3064babb899c52c1794d03e4ba205e91")
	version("1.38.0", commit="bdd5076dc6a7d889c62332407bbdb7c36253a7f2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cnvgsa", type=("build", "run"))

