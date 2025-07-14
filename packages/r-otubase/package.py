# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROtubase(RPackage):
	"""Provides structure and functions for the analysis of OTU data

	Provides a platform for Operational Taxonomic Unit based analysis
	"""
	
	bioc = "OTUbase"

	version("1.58.0", commit="364a17dc7e73c6dae2cf622db8931a2559a0cef7")
	version("1.52.0", commit="e02b2a4debdeae65bc6372571ee697d38df2b4be")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-shortread@1.23.15:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
