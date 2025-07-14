# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REgseadata(RPackage):
	"""Gene set collections for the EGSEA package

	This package includes gene set collections that are used for the Ensemble of Gene Set Enrichment Analyses (EGSEA) method for gene set testing. It includes Human and Mouse versions of the MSidDB (Subramanian, et al. (2005) PNAS, 102(43):15545-15550) and GeneSetDB (Araki, et al. (2012) FEBS Open Bio, 2:76-82) collections.
	"""
	
	bioc = "EGSEAdata"

	version("1.36.0", commit="800de29240cd6d8a07e1c9715bf03a5ea36f3159")
	version("1.30.0", commit="ce4ef290eafb049f1f4959cf0642dd7933320207")

	depends_on("r@3.4:", type=("build", "run"))

