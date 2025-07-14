# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpac(RPackage):
	"""Identification of Protein Amino acid Clustering

	iPAC is a novel tool to identify somatic amino acid mutation clustering within proteins while taking into account protein structure.
	"""
	
	bioc = "iPAC"

	version("1.52.0", commit="8751a8f777fc9da5a33edc20e02498a2e5dc5897")
	version("1.46.0", commit="8ca24b361603ee7a1741ca405bdd296dface84fe")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-gdata", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
