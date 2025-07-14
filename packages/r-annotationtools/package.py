# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnnotationtools(RPackage):
	"""Annotate microarrays and perform cross-species gene expression analyses using flat file databases

	Functions to annotate microarrays, find orthologs, and integrate heterogeneous gene expression profiles using annotation and other molecular biology information available as flat file database (plain text files).
	"""
	
	bioc = "annotationTools"

	version("1.82.0", commit="7bdab3c0c2b6276b51b26aa273341db4778271dd")
	version("1.76.0", commit="2b6d42d8a1dc167f1c3d269ed84059e62e6e0b93")

	depends_on("r-biobase", type=("build", "run"))
