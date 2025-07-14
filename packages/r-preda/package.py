# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPreda(RPackage):
	"""Position Related Data Analysis

	Package for the position related analysis of quantitative functional genomics data.
	"""
	
	bioc = "PREDA"

	version("1.54.0", commit="895e6ba8ff5250a4f821242d9dd565b90570a5eb")
	version("1.48.0", commit="8c10ef8d499ecd6e673b2993c6f027fa0a987fe7")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-lokern@1.0.9:", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
