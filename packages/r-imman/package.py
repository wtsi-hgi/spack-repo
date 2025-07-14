# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImman(RPackage):
	"""Interlog protein network reconstruction by Mapping and Mining ANalysis

	Reconstructing Interlog Protein Network (IPN) integrated from several Protein protein Interaction Networks (PPINs). Using this package, overlaying different PPINs to mine conserved common networks between diverse species will be applicable.
	"""
	
	bioc = "IMMAN"

	version("1.28.0", commit="64beff68a13f145c2c1b232fc44dfa752ef06d57")
	version("1.22.0", commit="561195579065e60624167f72f60f235b3bd06b55")

	depends_on("r-stringdb", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
