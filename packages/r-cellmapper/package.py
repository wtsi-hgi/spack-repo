# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCellmapper(RPackage):
	"""Predict genes expressed selectively in specific cell types

	Infers cell type-specific expression based on co-expression similarity with known cell type marker genes. Can make accurate predictions using publicly available expression data, even when a cell type has not been isolated before.
	"""
	
	bioc = "CellMapper"

	version("1.34.0", commit="1d8ae527c83831702ff75d77fa728255e8f92a6b")
	version("1.28.0", commit="995d67d72a956114cd1283ed1a4ceee06071c5bd")

	depends_on("r-s4vectors", type=("build", "run"))
